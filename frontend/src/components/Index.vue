<template>
  <div id="app">
    <v-app app>
      <div v-if="loading">
        <ProgressBar :task_id="task_id" @stopLoading="stopLoading"> </ProgressBar>
      </div>
      <section v-else>
        <Navbar> </Navbar>
        <Sidebar></Sidebar>
        <Footer></Footer>
      </section>
      
    </v-app>
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import ProgressBar from "./ProgressBar";
import Footer from "./Footer";

export default {
  name: "Index",
  components: {
    Navbar,
    Sidebar,
    ProgressBar,
    Footer,
    // UserTable,
    // SearchByUrl,
  },
  data() {
    return {
      loading: true,
      status: "",
      task_id: "",
    };
  },
  created() {
    this.task_id = this.$store.getters.TASK_ID
    console.log(this.task_id);
  },
  methods: {
    stopLoading() {
      this.loading = false;
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
