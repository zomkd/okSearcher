<template>
  <div>
    <div v-if="getLoading && getTaskID != ''">
      <ProgressBar :task_id="getTaskID" @stopLoading="stopLoading">
      </ProgressBar>
    </div>
    <section v-else-if="!getLoading">
      <UserTable :users="getUsers" :headers="headers"></UserTable>
    </section>
    <section v-else>
    <p>123</p>
    </section>
  </div>
</template>
<!-- eslint-disable -->
<script>
import UserTable from "./UserTable";
import ProgressBar from "./ProgressBar";
import { mapMutations } from "vuex";
export default {
  name: "GeneralInfo",
  components: {
    UserTable,
    ProgressBar,
  },
  data() {
    return {
      headers: [
        {
          text: "Полное имя",
          align: "start",
          filterable: false,
          value: "name",
        },
        { text: "Количество друзей", value: "friendsCount" },
        { text: "Дата рождения", value: "birthDate" },
        { text: "Приватность", value: "isPrivate" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      users: [],
      loading: true,
      status: "",
      task_id: "",
    };
  },
  computed: {
    getLoading() {
      return this.$store.getters.LOADING;
    },
    getTaskID() {
      return this.$store.getters.USERS_TASK_ID;
    },
    getUsers() {
      return this.$store.getters.USERS;
    },
  },
  methods: {
    ...mapMutations([
      "SET_USERS", // `this.increment()` будет вызывать `this.$store.commit('increment')`
    ]),
    stopLoading() {
      // this.loading = false;
      this.$store.commit('SET_LOADING', false)
    },
  
  },
};
</script>
