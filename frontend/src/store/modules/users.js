const state = {
    users: JSON.parse(localStorage.getItem('users') || '[]'),
    selected: JSON.parse(localStorage.getItem('selected') || '[]'),
};

const getters = {
  USERS: state => {
    return state.users;
  },
  SELECTED: state => {
    return state.selected;
  }
};

const mutations = {
  SET_USERS: (state, payload) => {
    state.users.push(payload)

    localStorage.setItem('users', JSON.stringify(state.users))
  },
  SET_SELECTED: (state, payload) => {
    state.selected = payload

    localStorage.removeItem('selected')
    localStorage.setItem('selected', JSON.stringify(state.selected))
  },
};


export default {
  state,
  getters,
  mutations,
};