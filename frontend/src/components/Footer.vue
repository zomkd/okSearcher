<template>
  <div>
    <v-footer app :height="100">
        <div class="names-title"><strong>Выбранные пользователи: </strong></div>
      <div
        class="selected-list"
        v-for="(users, idx) in getSelectedUsers"
        :key="users.id"
      >
        <div class="names">
          <span> {{ idx + 1 }}. </span>{{ users.name }}
        </div>
      </div>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      selectedUsers: [],
    };
  },
  computed: {
    getSelectedUsers() {
      return this.$store.getters.SELECTED;
    },
  },
};
</script>

<style>
.selected-list {
  position: flex;
}
.names {
  margin: 5px;
}
</style>