<template>
  <v-container fluid>
    <v-row>
      <v-col v-for="action in actions" :key="action.key">
        <v-card>
          <v-card-text>
            <div class="text--primary">
              {{ action }}
            </div>
          </v-card-text>
          <v-card-actions>
          <v-btn color="blue lighten-3">Старт</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "GraphActions",
  data() {
    return {
      actions: [
        "Друзья пользователя",
        "Активные пользователи",
        "Общие друзья",
        "Общие активные пользователи",
      ],
    };
  },
};
</script>

<style>
</style>
