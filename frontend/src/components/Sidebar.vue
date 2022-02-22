<template>
  <v-card class="mx-auto">
    <v-navigation-drawer permanent clipped app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Параметры поиска
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list>
        <v-list-item>
          <v-text-field
            v-model="secondname"
            name="secondname"
            label="Фамилия"
            type="text"
          ></v-text-field>
        </v-list-item>
        <v-list-item>
          <v-text-field
            v-model="firstname"
            name="firstname"
            label="Имя"
            type="text"
          ></v-text-field>
        </v-list-item>
        <v-list-item>
          <v-autocomplete
            v-model="country"
            :items="countries"
            label="Страна"
            placeholder="Выберите..."
          ></v-autocomplete>
        </v-list-item>
        <v-list-item>
          <v-text-field
            v-model="city"
            name="city"
            label="Город"
            type="text"
          ></v-text-field>
        </v-list-item>
        <v-list-item>
          <v-list-item-title>От</v-list-item-title>
          <v-autocomplete
            v-model="fromAge"
            :items="age"
            label="Возраст"
            placeholder="Выберите..."
          ></v-autocomplete>
          <v-list-item-title>До</v-list-item-title>
          <v-autocomplete
            v-model="tillAge"
            :items="age"
            label="Возраст"
            placeholder="Выберите..."
          ></v-autocomplete>
        </v-list-item>
        <v-list-item >
        <form ref="form" @submit.prevent="search()">
         <v-btn block type="submit" color="primary" value="поиск">Поиск</v-btn>
        </form>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
import axios from 'axios'
export default {
  name: "Sidebar",
  data() {
    return {
      age: ["14", "15", "16","17","18","19","20","21","22","23"],
      fromAge: "",
      tillAge: "",
      city: "",
      country: "",
      countries: ["Russia", "USA",],
      firstname: "",
      secondname: "",
    };
  },
  methods: {
    async search() {
      let data = new FormData();
      data.set('firstname', this.firstname)
      data.set('secondname', this.secondname)
      data.set('fromAge', this.fromAge)
      data.set('tillAge', this.tillAge)
      data.set('city', this.city)
      data.set('country', this.country)
      this.$store.commit('SET_LOADING', true)
      await axios({
        method: "post",
          url: "http://localhost:8000/search/",
          data: data,
          config: {
            headers: {
              "Content-Type": "application/json",
            },
          },
      }).then((res) => {
          console.log(res);
          // this.SET_TASK_ID(res.data.task_id);

          this.$store.commit('SET_SEARCH_TASK_ID',res.data.task_id)
        });
    }
  },
};
</script>
