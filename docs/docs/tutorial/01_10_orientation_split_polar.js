import("../../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Switch the orientation = arrange by other axis",
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
                  detach: "Popularity",
                },
                x: {
                  attach: "Popularity",
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
              title: "Split stacked values = show side-by-side",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              split: true,
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
              title: "Merge",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              split: false,
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
              title: "Aggregate",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                x: {
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
              title: "Polar coordinates",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  range: {
                    min: "-30%",
                  },
                },
              },
              coordSystem: "polar",
            },
          });
        },
      ],
    },
  ]);
});
