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
<!--eslint-disable -->
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
          scaling: {
            min: 10,
            max: 30,
          },
        },
        edges: {
          width: 2,
          color: { inherit: "from" },
          arrows: {
            to: {
              enabled: true,
              type: 'arrow',
            },
          },
          // smooth: {
          //     type: "continuous",
          //   },
          smooth: { type: "curvedCW", forceDirection: "none", roundness: 0.2 },
        },
        physics: {
          enabled: false,
          // barnesHut: {
          //   theta: 0.5,
          //   // gravitationalConstant: gravitationalConstant,
          //   centralGravity: 0,
          //   springLength: 10,
          //   springConstant: 0.04,
          //   damping: 0.09,
          //   avoidOverlap: 1,
          // },
          
        },
        // layout: {
        //   randomSeed: 3,
        // },
      },
    };
  },
  computed: {
    getNodes() {
      this.nodes = this.graphData[0];
      return this.nodes;
    },
    getEdges() {
      this.edges = this.graphData[1];
      return this.edges;
    },
  },
};
</script>

<style>
.network {
  width: 100%;
  height: 600px;
  max-height: 900px;
}
</style>