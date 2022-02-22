<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col v-for="action in actions" :key="action.key">
          <v-card>
            <v-card-text>
              <div class="text--primary">
                {{ action.name }}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                @click="showFriendsTable(action.name)"
                color="blue lighten-3"
                >Старт</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
        <v-snackbar v-model="isEnoughUsers">
          <p>Нужно вырать только одного пользователя</p>
          <template v-slot:action="{ attrs }">
            <v-btn
              color="pink"
              text
              v-bind="attrs"
              @click="isEnoughUsers = false"
            >
              Close
            </v-btn>
          </template>
        </v-snackbar>
        <v-col cols="12" v-if="isFriends">
          <UserFriends> </UserFriends>
          <!-- <div v-if="getLoading && getUserFriendsTaskID != ''">
            <ProgressBar :task_id="getUserFriendsTaskID" @stopLoading="stopLoading">
            </ProgressBar>
          </div>
          <section v-else-if="!loading">
            <UserTable :users="getUserFriends" :headers="headers"></UserTable>
          </section> -->
        </v-col>
        <v-col cols="12" v-if="isActiveUsers">
          <!-- <UserTable></UserTable> -->
          <p>2222</p>
        </v-col>
        <v-col cols="12" v-if="isCommonFriends">
          <p>3333</p>
          <!-- <UserTable></UserTable> -->
        </v-col>
        <v-col cols="12" v-if="isCommonActiveUsers">
          <p>4444</p>
          <!-- <UserTable></UserTable> -->
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import UserTable from "./UserTable";
import axios from "axios";
// import UserTable from "./UserTable";
// import ProgressBar from "./ProgressBar";
import UserFriends from "./UserFriends";
export default {
  name: "TableActions",
  components: {
    // UserTable,
    // ProgressBar,
    UserFriends
  },
  data() {
    return {
      actions: [
        {
          name: "Друзья пользователя",
          size: 1,
          show: false,
        },
        {
          name: "Активные пользователи",
          size: 1,
          show: false,
        },
        {
          name: "Общие друзья",
          size: 2,
          show: false,
        },
        {
          name: "Общие активные пользователи",
          size: 2,
          show: false,
        },
      ],
      headers: [
        {
          text: "ID",
          align: "start",
          filterable: false,
          value: "id",
        },
        {
          text: "Полное имя",
          value: "name",
        },
        { text: "Количество друзей", value: "friendsCount" },
        { text: "Дата рождения", value: "birthDate" },
        { text: "Приватность", value: "isPrivate" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      isFriends: false,
      isEnoughUsers: false,
      isActiveUsers: false,
      isCommonFriends: false,
      isCommonActiveUsers: false,
      users_id: [],
      loading: true,
    };
  },

  computed: {
    getLoading() {
      return this.$store.getters.LOADING;
    },
    getUserFriendsTaskID() {
      return this.$store.getters.USER_FRIENDS_TASK_ID;
    },
    getUserFriends() {
      return this.$store.getters.USER_FRIENDS;
    },
  },

  //TODO обработать случай на беке если пользователь всего 1 для общих активностей
  methods: {
    showFriendsTable(action) {
      if (action == this.actions[0].name) {
        if (this.$store.getters.SELECTED.length === 1) {
          console.log(this.$store.getters.SELECTED)
          this.isActiveUsers = false;
          this.isCommonFriends = false;
          this.isCommonActiveUsers = false;
          this.isFriends = !this.isFriends;
          console.log(this.isFriends)
          if (this.isFriends){
            this.getFriends()} //нужен дабл клик на старт
        } else {
          this.isEnoughUsers = !this.isEnoughUsers;
        }
      }
      if (action == this.actions[1].name) {
        if (this.$store.getters.SELECTED.length === 1) {
          this.isFriends = false;
          this.isCommonFriends = false;
          this.isCommonActiveUsers = false;
          this.isActiveUsers = !this.isActiveUsers;
        } else {
          this.isActiveUsers = !this.isActiveUsers;
        }
      }
    },
    getFriends() {
      let data = new FormData();
      // let selected_users = [] 
      // selected_users = this.$store.getters.SELECTED
      this.getUsersID(localStorage.getItem('selected'))
      console.log(this.users_id)
      data.set('selected_users', this.users_id); //я хз почему так криво передаются данные, по всей видимости передается тольео строка
      console.log(data)
      axios({
        method: "post",
        url: "http://localhost:8000/user_friends/",
        data: data,
        config: {
          headers: {
            "Content-Type": "application/json",
          },
        },
      }).then((res) => {
        console.log(res);
        // this.SET_TASK_ID(res.data.task_id);
        this.$store.commit("SET_LOADING", true);
        this.$store.commit("SET_USER_FRIENDS_TASK_ID", res.data.task_id);
      });
    },
    getUsersID(usersString){
      this.users_id = []
      let users = JSON.parse(usersString)
      for (let i = 0; i < users.length; ++i){
        this.users_id.push(users[i]['id'])
      }
    },
    // stopLoading(usersData) {
    //   // this.loading = false;
    //   console.log(usersData)
    //   this.$store.commit('SET_USER_FRIENDS', usersData);
    //   // this.$store.commit('SET_USER_FRIENDS_TASK_ID', '')

    //   this.loading = false;
    //   // this.$store.commit('SET_LOADING', false);
    // },
  },
};
</script>

<style>
</style>
