import("../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Click on a column!",
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
          const clickHandler = (event) => {
            alert(JSON.stringify(event.data));
          };
          chart.on("click", clickHandler);
          return chart;
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Override the axis label color for 'Jazz' to red",
            },
          });
        },
        (chart) => {
          const labelDrawHandler = (event) => {
            event.renderingContext.fillStyle =
              event.data.text === "Jazz" ? "red" : "gray";
          };
          chart.on("plot-axis-label-draw", labelDrawHandler);
          return chart;
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: { title: "Block the drawing of the Vizzu Logo" },
          });
        },
        (chart) => {
          const logoDrawHandler = (event) => {
            event.preventDefault();
          };
          chart.on("logo-draw", logoDrawHandler);
          return chart;
        },
      ],
    },
  ]);
});
