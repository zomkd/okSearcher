<template>
  <div id="app">
    <v-app app>
      <Navbar> </Navbar>
      <Sidebar></Sidebar>

    </v-app>
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

export default {
  name: "Index",
  components: {
    Navbar,
    Sidebar,
    // UserTable,
    // SearchByUrl,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
