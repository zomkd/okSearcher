<template>
  <div id="vis-network">
    <network
      class="network"
      ref="network"
      :nodes="getNodes"
      :edges="getEdges"
      :options="options"
    ></network>
  </div>
</template>

<script>
export default {
  name: "UserGraph",
  props: ["graphData"],
  data() {
    return {
      nodes: [],
      edges: [],
      options: {
        nodes: {
          shape: "dot",
        },
        edges: {
          width: 2,
          smooth: { type: "curvedCW", forceDirection: "none", roundness: 0.2 },
        },
        physics: {
          enabled: false,
          barnesHut: {
            theta: 0.5,
            // gravitationalConstant: gravitationalConstant,
            centralGravity: 0,
            springLength: 10,
            springConstant: 0.04,
            damping: 0.09,
            avoidOverlap: 1,
          },
        },
        layout: {
          randomSeed: 3,
        },
      },
    };
  },
  computed: {
    getNodes () {
      return this.nodes = this.graphData[0];
    },
    getEdges () {
      return this.edges = this.graphData[1];
    }
  }
};
</script>

<style>
</style>