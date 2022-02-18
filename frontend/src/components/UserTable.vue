<template>
  <v-card>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      v-model="selected"
      item-key="name"
      show-select
      :headers="this.headers"
      :items="info"
      :search="search"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >Are you sure you want to delete this item?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
      <!-- <template v-slot:no-data>
        <v-btn color="primary" @click="initialize"> Reset </v-btn>
      </template> -->
    </v-data-table>
  </v-card>
</template>

<script>

export default {
  name: "UserTable",
  props: ["users", "headers"],
  data() {
    return {
      dialog: false,
      dialogDelete: false,
      selected: [],
      info: [],
      search: "",
    };
  },
  watch: {
    dialog(val) { 
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
    selected(selection) {
      this.$store.commit('SET_SELECTED', selection)
    }
  },
  created() {
    this.initialize();
  },
  methods: {
    setSelected() {
      this.SET_SELECTED(this.selected)
    },

    initialize() {
      this.info = this.users;
    },

    deleteItem(item) {
      this.editedIndex = this.info.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.info.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.info[this.editedIndex], this.editedItem);
      } else {
        this.info.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>

<style>
</style>
