<template>
  <div>
    <div v-if="getLoading && getTaskID != ''">
      <ProgressBar :task_id="getTaskID" @stopLoading="stopLoading">
      </ProgressBar>
    </div>
    <section v-else-if="!loading">
      <UserTable :users="getUsers" :headers="headers"></UserTable>
    </section>
    <section v-else>

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
    stopLoading(data) {
      // this.loading = false;
      this.$store.commit('SET_USERS',data)
      this.$store.commit('SET_SEARCH_TASK_ID','')
      this.loading = false
      // this.$store.commit('SET_LOADING', false)
    },
  
  },
};
</script>
