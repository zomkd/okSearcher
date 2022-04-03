<template>
    <div>
        <div v-if="getLoading && getAnalysActiveUsersTaskID != ''">
            <ProgressBar :task_id="getAnalysActiveUsersTaskID" @stopLoading="stopLoading">
            </ProgressBar>
          </div>
          <section v-else-if="!loading">
            <UserGraph :graphData="getAnalysActiveUsers"></UserGraph>
          </section>
    </div>
</template>

<script>
import UserGraph from "./UserGraph";
import ProgressBar from "./ProgressBar";

export default {
    name:"ActiveUsersAnalys",
    components: {
    UserGraph,
    ProgressBar,
  },
  data() {
    return {
      nodes: [],
      edges: [],
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
    getAnalysActiveUsersTaskID() {
      return this.$store.getters.ANALYS_ACTIVE_USERS_TASK_ID;
    },
    getAnalysActiveUsers() {
      return this.$store.getters.ANALYS_ACTIVE_USERS;
    },
  },
  methods: {
    stopLoading(data) {
      // this.loading = false;
      this.$store.commit('SET_ANALYS_ACTIVE_USERS', data)
      this.$store.commit('SET_ANALYS_ACTIVE_USERS_TASK_ID','')
      this.loading = false
      // this.$store.commit('SET_LOADING', false)
    },
  
  },

}
</script>

<style>

</style>