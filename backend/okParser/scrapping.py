# from .tasks import search_ok
import time
from .api_ok import Odnoklassniki
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import undetected_chromedriver as uc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = uc.Chrome(options=chrome_options)
driver = uc.Chrome()

ok = Odnoklassniki('CNOCGEKGDIHBABABA', 'tkn1EhliRxCEAvwDOeURwKjZU3ArOtKp15kUfrs4IkgZknRO3FNiQpBqGETq4tuK4FnC3', '61db37441d2c3d823f7aee91a1104b97')


def enter_login_params(credentials):
    driver.get('https://ok.ru/')
    driver.find_element_by_id("field_email").send_keys(credentials['username'])
    driver.find_element_by_id("field_password").send_keys(credentials['password'])
    driver.find_element_by_xpath("//input[@value='Log in to OK']").click()


def enter_search_params(search_params):
    # driver.get('https://ok.ru/dk?st.cmd=searchResult&st.mode=Users&st.grmode=Groups')
    driver.find_element_by_xpath("//input[@placeholder='Search site']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[contains(@class, 'button-clean__0wfyv search__mofy2 input-right-icon__on39s js-toolbar-search-btn')]").click()
    time.sleep(3)
    fullname = _create_fullname(search_params)
    
    driver.find_element_by_xpath("//input[@placeholder='Enter name']").send_keys(fullname)
    if len(search_params['fromAge']) != 0:
        select = Select(driver.find_element_by_name('st.fromAge'))
        select.select_by_value(search_params['fromAge'])
    if len(search_params['tillAge']) != 0:
        select = Select(driver.find_element_by_name('st.tillAge'))
        select.select_by_value(search_params['tillAge'])
    
    lis = driver.find_elements_by_class_name("disable-list-type__kht0y")
    if len(search_params['country']) != 0:
        for li in lis:
            if li.text == 'Another place':
                li.click()
        select = Select(driver.find_element_by_name('st.country'))
        select.select_by_visible_text(search_params['country'])
    if len(search_params['city']) != 0:
        driver.find_element_by_xpath("//input[@placeholder='Enter city name']").send_keys(search_params['city'])
    driver.find_element_by_xpath("//button[contains(@class, 'button__pe9qo button-core-container__0ej09 squared-button__w4hf7')]").click()
    time.sleep(5)

def scroll_users_page():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #TODO подумать над пагинацией

def _create_fullname(search_params):
    return search_params['firstname'] + ' ' + search_params['secondname'] 

def get_users_info():
    users_profile_url = get_users_profile_url()
    users_id = get_users_id(users_profile_url)
    users_info = get_info(users_id)

    return users_info


def get_users_profile_url():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    users = soup.find_all("div", class_="card__kq7ru __h__kq7ru")
    users_profile_url = []
    for user in users:
        profile_url = user.find("a").get("href")
        users_profile_url.append(profile_url)
    return users_profile_url

def get_users_id(users_profile_url: list = None):
    users_id = []
    print(users_profile_url)
    for user_profile_url in users_profile_url:
        url = 'https://ok.ru' + user_profile_url
        resp = ok.url.getInfo(url=url)
        print(resp)
        users_id.append(resp['objectId'])
    return users_id

def get_info(users_id: list = None):
    users_info = []
    print(users_id)
    fields = 'NAME,BIRTHDAY,PRIVATE'
    for user_id in users_id:
        user_info = {}
        info = ok.users.getInfo(uids=user_id, fields=fields)
        print(info)
        try:    
            friends = ok.friends.get(fid=user_id)
        except Exception:
            friends = []
        print(friends)
        user_info['id'] = user_id
        user_info['name'] = info[0]['name']
        user_info['birthDate'] = info[0]['birthday']
        user_info['isPrivate'] = info[0]['private']
        user_info['friendsCount'] = len(friends)
        users_info.append(user_info)
    return users_info


def get_friends(users_id: list = None):
    for user_id in users_id:
        try:    
            friends = ok.friends.get(fid=user_id)
        except Exception:
            friends = []
    return friends

def get_friends_info(users_id):
    friends = get_friends(users_id)
    friends_info = get_info(friends)
    return friends_info

def get_user_active_info(selected_user_id):
    user_albums_info = ok.photos.getAlbums(fid = selected_user_id[0])#return list
    print(user_albums_info['albums'])
    album_photos = get_user_album_photos(user_albums_info['albums'])
    likers = get_photo_likers(album_photos)
    likers_id = extract_likers_id(likers)
    likers_info = get_info(list(tuple(likers_id)))
    user_active_info =  count_likers(likers_info, likers_id)

    return user_active_info

def get_user_album_photos(user_albums_info):
    album_photos =[]
    user_photos = ok.photos.getUserPhotos(fid = user_albums_info[0]['user_id'])
    print(user_photos)
    album_photos.extend(user_photos['photos'])
    for album in user_albums_info:
        print(album)
        photos = ok.photos.getUserAlbumPhotos(aid = album['aid'])
        
        album_photos.extend(photos['photos'])
        
    return album_photos

def get_photo_likers(album_photos):
    likers = []
    print(album_photos)
    for photo in album_photos:
        print(photo)
        users = ok.photos.getPhotoLikes(photo_id = photo['fid'])
        if users.get('users', '') != '':
            likers.extend(users['users'])

    return likers

def extract_likers_id(likers):
    likers_id = []
    for liker in likers:
        likers_id.append(liker['uid'])
    return likers_id

def count_likers(likers_info, likers_id):
    for liker in likers_info:
        like_count = likers_id.count(liker['id'])
        liker['likeCount'] = like_count

    return likers_info

def get_users_info_by_id(userIDs: list):
    return get_info(userIDs)

def get_users_common_friends(user_friends_ids):
    all_friends = get_all_friends(user_friends_ids)
    common_friends = set_duplicated_elements(all_friends, len(user_friends_ids))
    user_common_friends_info = get_info(common_friends)
    return user_common_friends_info

def get_all_friends(user_friends_ids):
    all_friends = []
    for friends_id in user_friends_ids:
        friends = ok.friends.get(fid=friends_id)
        all_friends.extend(friends)
    return all_friends
    
def set_duplicated_elements(data: list, common_num: int) -> list:
    """
    Извлекает только повторяющиеся элементы
    На вход: data: list ([1,1,3,3,4,4,5,6,7])
    На выход: duplicate: list
    duplicates = [1,3,4]
    """
    duplicates = []
    for elem in data:
        if data.count(elem) == common_num and elem not in duplicates:
            duplicates.append(elem)

    return duplicates

def get_users_obvious_connection(user_obvious_connections_ids):
    common_friends = get_users_common_friends(user_obvious_connections_ids)
    nodes = get_nodes(user_obvious_connections_ids, common_friends)
    links = get_links(nodes,user_obvious_connections_ids)
    obvious_connection = [nodes,links]
    return obvious_connection

def get_nodes(username: list, nodes_users: list) -> list:
    """
    Формирует nodes
    На вход: username: list (нужен для формирования главных node, 
    от которых строится граф), nodes_users: list
    На выход: nodes: list
    nodes = [{'id':12312, 'name': user1, ...}, ...]
    """
    try:
        main_node_info = get_info(username)
        nodes = []
        for user in main_node_info:
            main_node = {'id': user['id'],
                        'group': user['id'],
                        'title': user['id'],
                        'label': user['name'],
                        'value': 10,
                        }
            nodes.append(main_node)

        for usual_node in nodes_users:  # формирует nodes специально для работы с графом
            node = {}
            node['id'] = usual_node['id']  # не везде pk
            node['title'] = usual_node['id']
            node['label'] = usual_node['name']
            node['value'] = 0
            # node['group'] = group
            # node['_color'] = _color
            nodes.append(node)
    except Exception:
        print(nodes_users)

    return nodes

def get_links(nodes: list, main_node: list) -> list:
    """
    Формирует links для отображения 
    На вход: nodes: list, main_node: links
    На выход: links: list
    links = [{'sid':12312, 'tid': 11, ...}, ...]
    """
    links = []
    for node in main_node:
        for usual_node in nodes:
            if usual_node['id'] not in main_node:
                link = {}
                link['to'] = usual_node['id']
                link['from'] = node
                links.append(link)

    return links

def get_users_unobvious_connection(user_unobvious_connections_ids):
    start_node = user_unobvious_connections_ids.pop(0)
    start_node_friends = get_friends(start_node.split(' '))
    # print(start_node_friends)
    start_depth_nodes = get_start_depth_nodes(start_node_friends, start_node,user_unobvious_connections_ids)
    # print(start_depth_nodes)
    continue_depth_nodes = get_continue_depth_nodes(start_depth_nodes, user_unobvious_connections_ids, start_node, 2)
    
    nodes = get_unobvious_connection_nodes(continue_depth_nodes, user_unobvious_connections_ids, start_node)
    links = get_unobvious_connection_links(continue_depth_nodes)
    return [nodes,links]

def get_start_depth_nodes(start_node_friends, start_node, user_unobvious_connections_ids):
    start_depth_nodes = {}
    checked_users = []
    start_depth_nodes['straight_link'] = []
    start_depth_nodes['friends'] = []
    checked_users.append(start_node)
    for user_unobvious_connections_id in user_unobvious_connections_ids: #проверка на то есть ли у изначального плоьзователя свзяь с интересующими
        if user_unobvious_connections_id in start_node_friends:
            connection = {}
            straight_link = []
            connection['start'] = start_node
            connection['previous'] = []
            connection['end'] = user_unobvious_connections_id
            straight_link.append(connection)
            start_depth_nodes['straight_link'] = straight_link
            start_node_friends.remove(user_unobvious_connections_id)
            # checked_users.append(user_unobvious_connections_id)

    for node_friend in start_node_friends:
        previous = []
        node_history = {}
        previous.append(node_friend)
        node_history['previous'] = previous
        node_history['start'] = start_node
        # friends = get_friends(node_friend.split(' '))
        # if start_node in friends: # удаляю изначального пользователя из спсика друзей
        #     friends.remove(start_node)
        start_depth_nodes['friends'].append(node_history)
        checked_users.append(node_friend)
    
    start_depth_nodes['checked'] = checked_users

    return start_depth_nodes

def get_continue_depth_nodes(start_depth_nodes, user_unobvious_connections_ids, start_node, depths: int = 2): # если глубина будет больше
    new_checked_nodes = []
    node_history = {}
    previous = []
    for depth in range(2):
        for friend in start_depth_nodes['friends']:
            previous_id = friend['previous'][-1]
            previous_id_friends = get_friends(previous_id.split(' '))

            if previous_id_friends != []:
                unchecked_nodes = remove_checked_nodes(start_depth_nodes['checked'], previous_id_friends)
                previous_unchecked_nodes = check_to_start_users(user_unobvious_connections_ids, unchecked_nodes, friend, start_node)
                start_depth_nodes['straight_link'] = start_depth_nodes['straight_link'] + previous_unchecked_nodes['straight_link']
                # print(previous_unchecked_nodes)
                
                for unchecked_node in previous_unchecked_nodes['unchecked_nodes']:        
                    previous = friend.get('previous', []).copy()
                    previous.append(unchecked_node)
                    node_history['previous'] = previous
                    node_history['start'] = start_node
                    new_checked_nodes.append(node_history)
                    start_depth_nodes['checked'].append(unchecked_node)
                    node_history = {}
                    previous = []
        start_depth_nodes['friends'] = new_checked_nodes
        # print(new_checked_nodes)
        # print('asdasd')
        # print(start_depth_nodes)
        # print(start_depth_nodes['friends']) 
        new_checked_nodes = []
    return start_depth_nodes

def remove_checked_nodes(checked_nodes, depth_nodes):
    for checked_node in checked_nodes:
        if checked_node in depth_nodes:
            depth_nodes.remove(checked_node)
    return depth_nodes

def check_to_start_users(user_unobvious_connections_ids, unchecked_nodes, nodes, start_node):
    straight_link = []
    checked = {}
    # if start_node in unchecked_nodes:
    #     unchecked_nodes.remove(start_node)
    for user_unobvious_connections_id in user_unobvious_connections_ids:
        if user_unobvious_connections_id in unchecked_nodes:
            connection = {}
            connection['start'] = nodes['start']
            previous = nodes.get('previous', []).copy()
            connection['previous'] = previous
            connection['end'] = user_unobvious_connections_id
            straight_link.append(connection)
            unchecked_nodes.remove(user_unobvious_connections_id)
    checked = {'straight_link': straight_link, 'unchecked_nodes': unchecked_nodes}
    return checked

# def check_connection_in_same_depth(users_id):
#     straight_links = []
#     for user_id in users_id:
#         friends = get_friends(user_id.split(' '))
#         for checked_user in users_id:
#             if checked_user in friends:
#                 straight_link = []
#                 link = {}
#                 straight_link.append(checked_user)
#                 straight_link.append(user_id)
#                 link['straight_link'] = straight_link
#                 straight_links.append(link)
#     return straight_links
                    
def get_unobvious_connection_nodes(continue_depth_nodes, user_unobvious_connections_ids, start_node):
    unobvious_connection_node = []
    start_node_info = get_info(start_node.split(' '))
    start_node = {'id': start_node,
                'group': start_node,
                'title': start_node,
                'label': start_node_info[0]['name'],
                'value': 10,
                }
    unobvious_connection_node.append(start_node)
    nodes = []
    for continue_depth_node in continue_depth_nodes['straight_link']:
        if continue_depth_node['previous'] != []:
            for previous_node in continue_depth_node['previous']:
                nodes.append(previous_node)
        nodes.append(continue_depth_node['end'])
    nodes = list(set(nodes))
    for node in nodes:
        for end in user_unobvious_connections_ids:
            if end == node:
                node_info = get_info(end.split(' '))
                end_node = {'id': end,
                    'group': end,
                    'title': end,
                    'label': node_info[0]['name'],
                    'value': 10,
                }
                unobvious_connection_node.append(end_node)
            else:
                node_info = get_info(node.split(' '))
                usual_node = {}
                usual_node['id'] = node  # не везде pk
                usual_node['title'] = node
                usual_node['label'] = node_info[0]['name']
                usual_node['value'] = 0
                # node['group'] = group
                # node['_color'] = _color
                unobvious_connection_node.append(usual_node)
    return unobvious_connection_node

def get_unobvious_connection_links(continue_depth_nodes):
    unobvious_connection_links = []
    for continue_depth_node in continue_depth_nodes['straight_link']:
        if continue_depth_node['previous'] == []:
            start_link = start_link = {
            'from': continue_depth_node['start'],
            'to': continue_depth_node['end'],
            }
            unobvious_connection_links.append(start_link)
        else:
            start_link = {
            'from': continue_depth_node['start'],
            'to': continue_depth_node['previous'][0],
            }
            unobvious_connection_links.append(start_link)
        if len(continue_depth_node['previous']) == 1:
            link = {
                    'from': continue_depth_node['previous'][0],
                    'to': continue_depth_node['end'],
            }
            unobvious_connection_links.append(link)


        if len(continue_depth_node['previous']) > 1:
            index = 1
            for previous in continue_depth_node['previous']:
                if index != len(continue_depth_node['previous']):
                    link = {
                        'from': previous,
                        'to': continue_depth_node['previous'][index],
                    }
                else: 
                    link = {
                        'from': previous,
                        'to': continue_depth_node['end'],
                    }
                unobvious_connection_links.append(link)
                index = index + 1
    return unobvious_connection_links
