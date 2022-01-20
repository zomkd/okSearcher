<template>
  <div id="app">
    <v-app app>
      <Navbar> </Navbar>
      <Sidebar></Sidebar>
      <!-- <v-content>
         <UserTable></UserTable>
      </v-content> -->
    </v-app>
  </div>
</template>

<script>
// import SearchByUrl from "./search/SearchByUrl";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
// import UserTable from "./UserTable";
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
