
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data,
      config: {
        channels: {
          x: "Joy factors",
          y: "Value 5 (+/-)",
          color: "Joy factors",
          /* The noop channel (no operation) splits the markers as all the other channels
                but will have no effect on the markers’ appearance. */
          noop: "Country_code",
        },
        title: "Distribution Plot",
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: ["Joy factors", "Value 6 (+/-)"],
          label: "Country_code",
        },
        title: "Scatter Plot",
      },
    })
      ]
    }
  ]);
});

