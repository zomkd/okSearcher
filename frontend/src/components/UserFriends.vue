<template>
    <div>
        <div v-if="getLoading && getUserFriendsTaskID != ''">
            <ProgressBar :task_id="getUserFriendsTaskID" @stopLoading="stopLoading">
            </ProgressBar>
          </div>
          <section v-else-if="!loading">
            <UserTable :users="getUserFriends" :headers="headers"></UserTable>
          </section>
    </div>
</template>

<script>
import UserTable from "./UserTable";
import ProgressBar from "./ProgressBar";

export default {
    name: "UserFriends",
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
    getUserFriendsTaskID() {
      return this.$store.getters.USER_FRIENDS_TASK_ID;
    },
    getUserFriends() {
      return this.$store.getters.USER_FRIENDS;
    },
  },
  methods: {
    stopLoading(data) {
      // this.loading = false;
      this.$store.commit('SET_USER_FRIENDS',data)
      this.$store.commit('SET_USER_FRIENDS_TASK_ID','')
      this.loading = false
      // this.$store.commit('SET_LOADING', false)
    },
  
  },
}
</script>
