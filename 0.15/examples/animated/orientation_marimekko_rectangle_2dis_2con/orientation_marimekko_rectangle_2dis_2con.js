
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_4 = results[0].data_4;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_4, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_4,
      config: {
        channels: {
          x: ["Country", "Value 2 (+)"],
          y: ["Joy factors", "Value 3 (+)"],
          color: "Joy factors",
          label: "Country",
          lightness: "Country",
        },
        title: "Marimekko Chart",
        align: "stretch",
        orientation: "horizontal",
      },
    }),(chart) =>
    chart.animate({
      config: {
        title: "Marimekko with Other Orientation",
        orientation: "vertical",
      },
    })
      ]
    }
  ]);
});

