const state = {
    authenticated: JSON.parse(localStorage.getItem('authenticated') || 'false'),
};

const getters = {
  AUTH: state => {
    return state.authenticated;
  },
};

const mutations = {
  SET_AUTH: (state, payload) => {
    state.authenticated = payload

    localStorage.setItem('authenticated', JSON.stringify(state.authenticated))
  },
};


export default {
  state,
  getters,
  mutations,
};