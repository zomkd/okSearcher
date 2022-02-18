const state = {
    users: JSON.parse(localStorage.getItem('users') || '[]'),
    selected: JSON.parse(localStorage.getItem('selected') || '[]'),
    task_id: "",
    loading: true,
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
  SET_LOADING: (state, payload) => {
    state.loading = payload
  },
};


export default {
  state,
  getters,
  mutations,
};