<template>
   <v-app >
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
                           
                           <v-btn type="submit" class="mt-4" color="primary" value="log in">Login</v-btn>
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
import { mapMutations } from 'vuex';

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
      'SET_AUTH', // `this.increment()` будет вызывать `this.$store.commit('increment')`
    ]),
    login() {
      if(this.username.length != 0 && this.password.length != 0) {
            this.SET_AUTH(true);
            this.$router.push('/index');
        } else {
            console.log("The username and / or password is incorrect");
        }
    },
  },
};
</script>

<style >

</style>