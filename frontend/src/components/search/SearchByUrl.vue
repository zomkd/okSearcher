<template>
  <div class="search-by-url">
    <input
      placeholder="username1, username2"
      id="username"
      type="text"
    />
    <button type="submit" name="action" v-on:click="setUrls()">
      Submit
    </button>
    <vue-ellipse-progress :progress="progress"/>

  </div>
</template>

<script>
export default {
  name: "SearchByUrl",
  data() {
    return {
      urls: "",
      myProgress: 0,
      count: 0,
    };
  },
  methods: {
    async setUrls() {
      let r = await fetch("http://localhost:8000/tasks/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ type: 0 }),
      }).then((response) => {
        return response.json();
      });
      this.getStatus(r.task_id);
    },
    getStatus(task_id) {
      let resp = fetch("http://localhost:8000/tasks/" + task_id + "/").then((response) => {
        return response.json();
      });
      this.urls = resp;
      console.log(this.urls);
      
      this.count = this.count + 1;
      this.myProgress = this.count;
      // setTimeout(
      //   this.getStatus(task_id), 1000);
      },
  },

  //   async created() {
  //     let response = await fetch("http://localhost:8000/ping");
  //     this.test = await response.json();
  //   },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
