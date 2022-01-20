const state = {
    authenticated: false,
};

const getters = {
  AUTH: state => {
    return state.authenticated;
  },
};

const mutations = {
  SET_AUTH: (state, payload) => {
    state.authenticated = payload
  },
};


export default {
  state,
  getters,
  mutations,
};