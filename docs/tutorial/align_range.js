import("../../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Align: center",
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
              align: "center",
              channels: {
                y: {
                  labels: false,
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
              title: "Align: stretch = % view",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              align: "stretch",
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
              title: "Align: none - default",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              align: "none",
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
              title: "Axis range set proportionally to shown values",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  range: {
                    max: "150%",
                  },
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
              title:
                "Axis range set explicitly on an axis with discrete series",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                x: {
                  range: {
                    min: -2,
                    max: 3,
                  },
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
              title: "Back to the default ranges",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  range: {
                    max: "auto",
                  },
                  labels: true,
                },
                x: {
                  range: {
                    min: "auto",
                    max: "auto",
                  },
                },
              },
            },
          });
        },
      ],
    },
  ]);
});
