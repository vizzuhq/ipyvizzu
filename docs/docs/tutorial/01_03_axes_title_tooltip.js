import("../../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: { set: "Popularity" },
                x: { set: "Genres" },
              },
            },
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                x: { set: null },
                y: { set: ["Genres", "Popularity"] },
              },
            },
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: { detach: "Popularity" },
                x: { attach: "Popularity" },
              },
            },
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          console.log(chart.config);
          return chart;
        },
        (chart) => {
          return chart.animate({ title: "My first chart" });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          chart.feature("tooltip", true);
          return chart;
        },
      ],
    },
  ]);
});
