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
          <v-list-item-title>От</v-list-item-title>
          <v-autocomplete
            v-model="ageFrom"
            :items="age"
            label="Возраст"
            placeholder="Выберите..."
          ></v-autocomplete>
          <v-list-item-title>До</v-list-item-title>
          <v-autocomplete
            v-model="ageBefore"
            :items="age"
            label="Возраст"
            placeholder="Выберите..."
          ></v-autocomplete>
        </v-list-item>
        <v-list-item>
         <v-btn type="submit" color="primary" value="поиск">Поиск</v-btn>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      age: ["1", "2", "3"],
      ageFrom: "",
      ageBefore: "",
      country: "",
      countries: ["Afghanistan", "Albania", "Algeria"],
      firstname: "",
      secondname: "",
    };
  },
};
</script>
