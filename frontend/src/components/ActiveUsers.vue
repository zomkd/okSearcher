<template>
  <div>
    <div v-if="getLoading && getUserActiveTaskID != ''">
      <ProgressBar :task_id="getUserActiveTaskID" @stopLoading="stopLoading">
      </ProgressBar>
    </div>
    <section v-else-if="!loading">
      <UserTable :users="getUserActive" :headers="headers"></UserTable>
    </section>
  </div>
</template>

<script>
import UserTable from "./UserTable";
import ProgressBar from "./ProgressBar";

export default {
  name: "ActiveUsers",
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
        {
          text: "Количество лайков под фотографиями пользователя",
          value: "likeCount",
        },
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
    getUserActiveTaskID() {
      return this.$store.getters.USER_ACTIVE_TASK_ID;
    },
    getUserActive() {
      return this.$store.getters.USER_ACTIVE;
    },
  },
  methods: {
    stopLoading(data) {
      // this.loading = false;
      this.$store.commit("SET_USER_ACTIVE", data);
      this.$store.commit("SET_USER_ACTIVE_TASK_ID", "");
      this.loading = false;
      // this.$store.commit('SET_LOADING', false)
    },
  },
};
</script>
