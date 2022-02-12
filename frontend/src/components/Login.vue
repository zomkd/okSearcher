<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Вход в Одноклассники</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <form ref="form" @submit.prevent="login()">
                  <v-text-field
                    v-model="username"
                    name="username"
                    label="Username"
                    type="text"
                    placeholder="username"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    name="password"
                    label="Password"
                    type="password"
                    placeholder="password"
                    required
                  ></v-text-field>

                  <v-btn
                    type="submit"
                    class="mt-4"
                    color="primary"
                    value="log in"
                    >Login</v-btn
                  >
                </form>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapMutations } from "vuex";
import axios from 'axios'
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapMutations([
      "SET_AUTH",
      // "SET_TASK_ID", // `this.increment()` будет вызывать `this.$store.commit('increment')`
    ]),
    async login() {
      if (this.username.length != 0 && this.password.length != 0) {
        this.SET_AUTH(true);
        let data = new FormData();
        data.set("username", this.username);
        data.set("password", this.password);
        await axios({
          method: "post",
          url: "http://localhost:8000/login/",
          data: data,
          config: {
            headers: {
              "Content-Type": "application/json",
            },
          },
        }).then((res) => {
          // console.log(res);
          // this.SET_TASK_ID(res.data.task_id);
          this.$store.commit('SET_TASK_ID',res.data.task_id)
        });
        // this.$store.dispatch("setAuth", {
        //   username: this.username,
        //   password: this.password,
        // });
        console.log(this.$store.getters.TASK_ID);
        this.$router.push("/index");
      } else {
        console.log("The username and / or password are incorrect");
      }
    },
  },
};
</script>

<style >
</style>