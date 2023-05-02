
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
          noop: ["Year", "Country"],
          size: "Value 2 (+)",
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          noop: ["Year", "Country"],
          y: "Value 2 (+)",
          size: null,
        },
        
      },
    })
      ]
    }
  ]);
});

