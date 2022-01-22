<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col v-for="action in actions" :key="action.key">
          <v-card>
            <v-card-text>
              <div class="text--primary">
                {{ action.name }}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                @click="showFriendsTable(action.name)"
                color="blue lighten-3"
                >Старт</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
        <v-snackbar v-model="isEnoughUsers">
          <p>Нужно вырать только одного пользователя</p>

          <template v-slot:action="{ attrs }">
            <v-btn
              color="pink"
              text
              v-bind="attrs"
              @click="isEnoughUsers = false"
            >
              Close
            </v-btn>
          </template>
        </v-snackbar>
        <v-col cols="12" v-if="isFriends">
          <p>1111</p>
          <!-- <UserTable></UserTable> -->
        </v-col>
        <v-col cols="12" v-if="isActiveUsers">
          <!-- <UserTable></UserTable> -->
          <p>2222</p>
        </v-col>
        <v-col cols="12" v-if="isCommonFriends">
          <p>3333</p>
          <!-- <UserTable></UserTable> -->
        </v-col>
        <v-col cols="12" v-if="isCommonActiveUsers">
          <p>4444</p>
          <!-- <UserTable></UserTable> -->
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import UserTable from "./UserTable";

export default {
  name: "TableActions",
  //   components: {
  //       UserTable,
  //   },
  data() {
    return {
      actions: [
        {
          name: "Друзья пользователя",
          size: 1,
          show: false,
        },
        {
          name: "Активные пользователи",
          size: 1,
          show: false,
        },
        {
          name: "Общие друзья",
          size: 2,
          show: false,
        },
        {
          name: "Общие активные пользователи",
          size: 2,
          show: false,
        },
      ],
      isFriends: false,
      isEnoughUsers: false,
      isActiveUsers: false,
      isCommonFriends: false,
      isCommonActiveUsers: false,
    };
  },
  //TODO обработать случай на беке если пользователь всего 1 для общих активностей
  methods: {
    showFriendsTable(action) {
      if (action == this.actions[0].name) {
        if (this.$store.getters.SELECTED.length === 1) {
          this.isActiveUsers = false;
          this.isCommonFriends = false;
          this.isCommonActiveUsers = false;
          this.isFriends = !this.isFriends;
        } else {
          this.isEnoughUsers = !this.isEnoughUsers;
        }
      }
      if (action == this.actions[1].name) {
        if (this.$store.getters.SELECTED.length === 1) {
          this.isFriends = false;
          this.isCommonFriends = false;
          this.isCommonActiveUsers = false;
          this.isActiveUsers = !this.isActiveUsers;
        } else {
          this.isActiveUsers = !this.isActiveUsers;
        }
      }
    },
  },
};
</script>

<style>
</style>
