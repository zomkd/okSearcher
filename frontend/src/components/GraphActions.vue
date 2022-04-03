<template>
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
            <v-btn @click="showGraph(action.name)" color="blue lighten-3"
              >Старт</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
      <v-snackbar v-model="isEnoughUsers">
        <p>Нужно вырать больше одного пользователя</p>
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
      <v-col cols="12" v-if="isObviousConnections">
        <ObviousConnections> </ObviousConnections>
      </v-col>
      <v-col cols="12" v-if="isUnobviousConnections">
        <UnobviousConnections> </UnobviousConnections>
      </v-col>
      <v-col cols="12" v-if="isActiveUsersAnalys">
        <ActiveUsersAnalys> </ActiveUsersAnalys>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import ObviousConnections from "./ObviousConnections";
import UnobviousConnections from "./UnobviousConnections";
import ActiveUsersAnalys from "./ActiveUsersAnalys";

export default {
  name: "GraphActions",
  components: {
    ObviousConnections,
    UnobviousConnections,
    ActiveUsersAnalys,
  },
  data() {
    return {
      actions: [
        {
          name: "Явные связи",
        },
        { name: "Неявные связи" },
        { name: "Анализ активности пользователя" },
      ],
      isObviousConnections: false,
      isUnobviousConnections: false,
      isActiveUsersAnalys: false,
      // isCommonActiveUsers: false,
      users_id: [],
      loading: true,
      isEnoughUsers: false,
    };
  },
  methods: {
    showGraph(action) {
      if (action === this.actions[0].name) {
        if (this.$store.getters.SELECTED.length > 1) {
          console.log(this.$store.getters.SELECTED);
          this.isUnobviousConnections = false;
          this.isActiveUsersAnalys = false;
          // this.isCommonActiveUsers = false;
          this.isObviousConnections = !this.isObviousConnections;
          if (this.isObviousConnections) {
            this.getObviousConnections();
          } //нужен дабл клик на старт
        } else {
          this.isEnoughUsers = !this.isEnoughUsers;
        }
      }
      if (action === this.actions[1].name) {
        if (this.$store.getters.SELECTED.length > 1) {
          this.isObviousConnections = false;
          this.isActiveUsersAnalys = false;
          // this.isCommonActiveUsers = false;
          this.isUnobviousConnections = !this.isUnobviousConnections;
          if (this.isUnobviousConnections) {
            this.getUnobviousConnections();
          }
        } else {
          this.isEnoughUsers = !this.isEnoughUsers;
        }
      }
      if (action === this.actions[2].name) {
        if (this.$store.getters.SELECTED.length > 1) {
          this.isObviousConnections = false;
          // this.isCommonActiveUsers = false;
          this.isUnobviousConnections = false
          this.isActiveUsersAnalys = !this.isActiveUsersAnalys;
          if (this.isActiveUsersAnalys) {
            this.getActiveUsersAnalys();
          }
        } else {
          this.isEnoughUsers = !this.isEnoughUsers;
        }
      }
    },
    getObviousConnections() {
      let data = new FormData();
      this.getUsersID(localStorage.getItem("selected"));
      data.set("selected_users", this.users_id); //я хз почему так криво передаются данные, по всей видимости передается тольео строка
      console.log(data);
      axios({
        method: "post",
        url: "http://localhost:8000/user_obvious_connections/",
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
        this.$store.commit(
          "SET_USER_OBVIOUS_CONNECTIONS_TASK_ID",
          res.data.task_id
        );
      });
    },
    getUnobviousConnections() {
      let data = new FormData();
      this.getUsersID(localStorage.getItem("selected"));
      data.set("selected_users", this.users_id); //я хз почему так криво передаются данные, по всей видимости передается тольео строка
      console.log(data);
      axios({
        method: "post",
        url: "http://localhost:8000/user_unobvious_connections/",
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
        this.$store.commit(
          "SET_USER_UNOBVIOUS_CONNECTIONS_TASK_ID",
          res.data.task_id
        );
      });
    },
    getActiveUsersAnalys() {
      let data = new FormData();
      
      data.set("analys_users", JSON.stringify(this.$store.getters.USER_UNOBVIOUS_CONNECTIONS))
      // console.log(data);
      axios({
        method: "post",
        url: "http://localhost:8000/analys_active_users/",
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
        this.$store.commit(
          "SET_ANALYS_ACTIVE_USERS_TASK_ID",
          res.data.task_id
        );
      });
    },
    getUsersID(usersString) {
      this.users_id = [];
      let users = JSON.parse(usersString);
      for (let i = 0; i < users.length; ++i) {
        this.users_id.push(users[i]["id"]);
      }
    },
  },
};
</script>

<style>
</style>
