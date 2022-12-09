import("../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Stack",
              channels: {
                y: { set: ["Popularity", "Kinds"] },
                x: { set: "Genres" },
                label: { attach: "Popularity" },
              },
              color: { attach: "Kinds" },
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  attach: "Genres",
                },
                x: {
                  set: null,
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
              title: "Aggregate element",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  detach: "Genres",
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
              title: "Drill-down",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  attach: "Genres",
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
              title: "Group",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  detach: "Genres",
                },
                x: {
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
