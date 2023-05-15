
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_14 = results[0].data_14;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_14, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_14,

      config: {
        channels: {
          y: "Value 4 (+/-)",
          x: "Value 2 (+)",
          color: "Country",
          label: "Country",
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          noop: "Year",
          label: null,
        },
        
      },
    })
      ]
    }
  ]);
});

