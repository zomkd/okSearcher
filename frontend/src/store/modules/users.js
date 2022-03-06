const state = {
    users: JSON.parse(localStorage.getItem('users') || '[]'),
    selected: JSON.parse(localStorage.getItem('selected') || '[]'),
    task_id: "",
    user_friends_task_id: "",
    user_active_task_id: "",
    user_common_friends_task_id: "",
    user_obvious_connections_task_id: "",
    user_unobvious_connections_task_id: "",
    loading: true,
    user_friends: [],
    user_active: [],
    common_friends: [],
    obvious_connections: [],
    unobvious_connections: [],

};

const getters = {
  USERS: state => {
    return state.users;
  },
  SELECTED: state => {
    return state.selected;
  },
  USERS_TASK_ID: state => {
    return state.task_id
  },
  LOADING: state => {
    return state.loading
  },
  USER_FRIENDS: state => {
    return state.user_friends
  },
  USER_ACTIVE: state => {
    return state.user_active
  },
  USER_OBVIOUS_CONNECTIONS: state => {
    return state.obvious_connections
  },
  USER_UNOBVIOUS_CONNECTIONS: state => {
    return state.unobvious_connections
  },
  USER_COMMON_FRIENDS: state => {
    return state.common_friends
  },
  USER_FRIENDS_TASK_ID: state => {
    return state.user_friends_task_id
  },
  USER_ACTIVE_TASK_ID: state => {
    return state.user_active_task_id
  },
  USER_COMMON_FRIENDS_TASK_ID: state => {
    return state.user_common_friends_task_id
  },
  USER_OBVIOUS_CONNECTIONS_TASK_ID: state => {
    return state.user_obvious_connections_task_id
  },
  USER_UNOBVIOUS_CONNECTIONS_TASK_ID: state => {
    return state.user_unobvious_connections_task_id
  },
};

const mutations = {
  SET_USERS: (state, payload) => {
    state.users = payload
    localStorage.removeItem('users')
    localStorage.setItem('users', JSON.stringify(state.users))
  },
  SET_SELECTED: (state, payload) => {
    state.selected = payload

    localStorage.removeItem('selected')
    localStorage.setItem('selected', JSON.stringify(state.selected))
  },
  SET_SEARCH_TASK_ID: (state, payload) => {
    state.task_id = ''
    state.task_id = payload
  },
  SET_USER_FRIENDS_TASK_ID: (state, payload) => {
    // state.user_friends_task_id = ''
    state.user_friends_task_id = payload
  },
  SET_USER_ACTIVE_TASK_ID: (state, payload) => {
    // state.user_friends_task_id = ''
    state.user_active_task_id = payload
  },
  SET_USER_COMMON_FRIENDS_TASK_ID: (state, payload) => {
    // state.user_friends_task_id = ''
    state.user_common_friends_task_id = payload
  },
  SET_USER_OBVIOUS_CONNECTIONS_TASK_ID: (state, payload) => {
    // state.user_friends_task_id = ''
    state.user_obvious_connections_task_id = payload
  },
  SET_USER_UNOBVIOUS_CONNECTIONS_TASK_ID: (state, payload) => {
    // state.user_friends_task_id = ''
    state.user_unobvious_connections_task_id = payload
  },
  SET_LOADING: (state, payload) => {
    state.loading = payload
  },
  SET_USER_FRIENDS: (state, payload) => {
    state.user_friends = payload
  },
  SET_USER_ACTIVE: (state, payload) => {
    state.user_active = payload
  },
  SET_COMMON_FRIENDS: (state, payload) => {
    state.common_friends = payload
  },
  SET_OBVIOUS_CONNECTIONS: (state, payload) => {
    state.obvious_connections = payload
  },
  SET_UNOBVIOUS_CONNECTIONS: (state, payload) => {
    state.unobvious_connections = payload
  },
};


export default {
  state,
  getters,
  mutations,
};