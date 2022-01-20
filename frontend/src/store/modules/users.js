const state = {
    users: [],
};

const getters = {
  USERS: state => {
    return state.users;
  },
};

const mutations = {
  SET_AUTH: (state, payload) => {
    state.users.push(payload)
  },
};


export default {
  state,
  getters,
  mutations,
};