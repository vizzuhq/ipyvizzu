import("../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Treemap",
              channels: {
                y: { set: ["Popularity", "Kinds"] },
                x: { set: "Genres" },
                label: { attach: "Popularity" },
              },
              color: { set: "Kinds" },
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  set: null,
                },
                x: {
                  set: null,
                },
                size: {
                  attach: ["Genres", "Popularity"],
                },
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
              title: "Bubble chart - stacked",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              geometry: "circle",
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
              title: "Bubble chart - grouped - using the noop channel",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                size: {
                  detach: "Genres",
                },
                noop: {
                  set: "Genres",
                },
              },
            },
          });
        },
      ],
    },
  ]);
});
