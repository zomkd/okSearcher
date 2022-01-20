<template>
  <div>
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon
        @click="drawer = true"
        class="d-flex d-sm-none"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>OKSearch</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs v-model="tab" grow>
          <v-tabs-slider color="orange"></v-tabs-slider>

          <v-tab v-for="item in items" :key="item.key">
            {{ item.forUser }}
          </v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <!-- Add a navigation bar -->
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group>
          <v-list-item v-for="(item, index) in items" :key="index">
            <v-list-item-title @click="tab = index">
         </v-list-item-title
            >
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <!-- Navigation bar ends -->

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="item in items" :key="item.key">
        <v-main>
          <component :is="item.vueName"> </component>
          <!-- <UserTable></UserTable> -->
        </v-main>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import UserTable from "./UserTable";
import TableActions from "./TableActions";
import GraphActions from "./GraphActions";
export default {
  name: "Navbar",
  components: {
    UserTable,
    TableActions,
    GraphActions
    // SearchByUrl,
  },
  data() {
    return {
      drawer: false,
      tab: null,
      // items: ["Общее", "Таблицы", "Графы"],
      // items: ["UserTable","TableActions","GraphActions"]
      items: [
        {
          vueName: "UserTable",
          forUser: "Общее",
        },
        {
          vueName: "TableActions",
          forUser: "Таблицы",
        },
        {
          vueName: "GraphActions",
          forUser: "Графы",
        },
      ],
    };
  },
};
</script>

<style>
</style>