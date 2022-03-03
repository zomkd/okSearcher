<template>
    <div>
        <div v-if="getLoading && getUserObviousConnectionsTaskID != ''">
            <ProgressBar :task_id="getUserObviousConnectionsTaskID" @stopLoading="stopLoading">
            </ProgressBar>
          </div>
          <section v-else-if="!loading">
            <UserGraph :graphData="getUserObviousConnections"></UserGraph>
          </section>
    </div>
</template>

<script>
import UserGraph from "./UserGraph";
import ProgressBar from "./ProgressBar";

export default {
    name:"ObviousConnections",
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
    getUserObviousConnectionsTaskID() {
      return this.$store.getters.USER_OBVIOUS_CONNECTIONS_TASK_ID;
    },
    getUserObviousConnections() {
      return this.$store.getters.USER_OBVIOUS_CONNECTIONS;
    },
  },
  methods: {
    stopLoading(data) {
      // this.loading = false;
      this.$store.commit('SET_USER_OBVIOUS_CONNECTIONS', data)
      this.$store.commit('SET_USER_OBVIOUS_CONNECTIONS_TASK_ID','')
      this.loading = false
      // this.$store.commit('SET_LOADING', false)
    },
  
  },

}
</script>

<style>

</style>