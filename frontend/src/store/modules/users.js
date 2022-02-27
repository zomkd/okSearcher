const state = {
    users: JSON.parse(localStorage.getItem('users') || '[]'),
    selected: JSON.parse(localStorage.getItem('selected') || '[]'),
    task_id: "",
    user_friends_task_id: "",
    user_active_task_id: "",
    loading: true,
    user_friends: [],
    user_active: [],
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
  USER_FRIENDS_TASK_ID: state => {
    return state.user_friends_task_id
  },
  USER_ACTIVE_TASK_ID: state => {
    return state.user_active_task_id
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
  SET_LOADING: (state, payload) => {
    state.loading = payload
  },
  SET_USER_FRIENDS: (state, payload) => {
    state.user_friends = payload
  },
  SET_USER_ACTIVE: (state, payload) => {
    state.user_active = payload
  },
};


export default {
  state,
  getters,
  mutations,
};