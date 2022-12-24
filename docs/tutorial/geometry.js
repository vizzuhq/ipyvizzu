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
              title: "Geometry",
              channels: {
                y: { set: "Popularity" },
                x: { set: "Genres" },
              },
            },
          });
        },
        (chart) => {
          return chart.animate({
            title: "Geometry: area",
            geometry: "area",
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            title: "Geometry: line",
            geometry: "line",
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            title: "Geometry: circle",
            geometry: "circle",
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            title: "Geometry: rectangle - default",
            geometry: "rectangle",
          });
        },
      ],
    },
  ]);
});
