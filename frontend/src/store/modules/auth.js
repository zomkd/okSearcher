// import axios from 'axios'
// import apiURL from '../../api/api'


const state = {
    authenticated: JSON.parse(localStorage.getItem('authenticated') || 'false'),
    credentials: {
      username: "",
      password: "",
    },
    task_id: "",
};

const getters = {
  AUTH: state => {
    return state.authenticated;
  },
  TASK_ID: state => {
    return state.task_id
  },
};

const mutations = {
  SET_AUTH: (state, payload) => {
    state.authenticated = payload

    localStorage.setItem('authenticated', JSON.stringify(state.authenticated))
  },
  SET_TASK_ID: (state, payload) => {
    state.task_id = payload
  },
};

// const actions = {
//     setAuth: ({commit},credentials) => {
//     let data = new FormData();
//     data.set("username", credentials.username);
//     data.set("password", credentials.password);
//     axios({
//       method: 'post',
//       url: 'http://localhost:8000/login/',
//       data: data,
//       config: {
//         headers: {
//           'Content-Type': 'application/json'
//         }
//       }
//     }).then((res) => {
//       console.log(res)
//       commit('SET_TASK_ID', res.task_id)
//     })
//     // axios.post("http://localhost:8000/login/", {
//     //   username: credentials.username,
//     //   password: credentials.password,
//     // })

//   }
// }

export default {
  state,
  getters,
  mutations,
  // actions,
};