import undetected_chromedriver as uc


driver = uc.Chrome()

def login_ok(credentials):
    driver.get('https://ok.ru/')
    driver.find_element_by_id("field_email").send_keys(credentials.dict()['username'])
    driver.find_element_by_id("field_password").send_keys(credentials.dict()['password'])
    driver.find_element_by_xpath("//input[@value='Log in to OK']").click()