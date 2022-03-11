<template>
    <div>
        <div v-if="getLoading && getUserUnobviousConnectionsTaskID != ''">
            <ProgressBar :task_id="getUserUnobviousConnectionsTaskID" @stopLoading="stopLoading">
            </ProgressBar>
          </div>
          <section v-else-if="!loading">
            <UserGraph :graphData="getUserUnobviousConnections"></UserGraph>
          </section>
    </div>
</template>

<script>
import UserGraph from "./UserGraph";
import ProgressBar from "./ProgressBar";

export default {
    name:"UnobviousConnections",
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
    getUserUnobviousConnectionsTaskID() {
      return this.$store.getters.USER_UNOBVIOUS_CONNECTIONS_TASK_ID;
    },
    getUserUnobviousConnections() {
      return this.$store.getters.USER_UNOBVIOUS_CONNECTIONS;
    },
  },
  methods: {
    stopLoading(data) {
      // this.loading = false;
      this.$store.commit('SET_UNOBVIOUS_CONNECTIONS', data)
      this.$store.commit('SET_USER_UNOBVIOUS_CONNECTIONS_TASK_ID','')
      this.loading = false
      // this.$store.commit('SET_LOADING', false)
    },
  
  },

}
</script>

<style>

</style>