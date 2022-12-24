const dataLoaded = import("../javascripts/data.js");
const mdChartLoaded = import("../javascripts/mdchart.js");

Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].default;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "tutorial");

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
              title: "Drill-down",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                x: {
                  attach: "Genres",
                },
              },
            },
          });
        },
      ],
    },
  ]);
});
