import("../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Click event added to markers",
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
              title: "Changing the canvas context before label draw",
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
            config: { title: "Prevent default behavior" },
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
