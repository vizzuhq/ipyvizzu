import("../../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Geometry",
              channels: {
                y: { set: ["Popularity"] },
                x: { set: ["Genres"] },
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
