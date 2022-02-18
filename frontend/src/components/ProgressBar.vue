<template>
<div class="progress-bar">
  <div class="text-center">
    <v-progress-circular
      :rotate="360"
      :size="100"
      :width="15"
      :value="value"
      color="teal"
    >
      {{ value }}
    </v-progress-circular>
    <p> Идет подключение...</p>
  </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProgressBar",
  props: ["task_id"],
  data() {
    return {
      status: "",
      value: 0,
      data: [],
    };
  },
  mounted() {
    this.getStatus();
  },
  methods: {
    getStatus() {
      console.log(this.task_id);
      //   await axios.get('http://localhost:8000/tasks/').then(response => (this.task_id = response.task_id))
      let timerID = setInterval(() => {
        axios
          .get("http://localhost:8000/tasks/" + this.task_id + "/")
          .then((response) => {
            console.log(response);
            this.status = response.data.task_status;
            this.value += 20;
            if (this.status === 'SUCCESS') {
            clearInterval(timerID)
            this.data = response.data.task_data
            this.$store.commit('SET_USERS',response.data.task_data)
            this.value = 100;
            this.stopLoading()
          }
            console.log(this.status);
          });
          
      }, 5000);
    },
    stopLoading() {
      this.$emit("stopLoading", "")
    },
  },
};
</script>

<style>
.progress-bar {
  text-align: center;
  margin-top: 20%;
}

</style>