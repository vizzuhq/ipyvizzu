
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
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
          color: "Country",
          size: ["Year", "Value 2 (+)"],
          label: "Value 2 (+)",
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Year",
          y: ["Country", "Value 2 (+)"],
          size: null,
          label: null,
        },
        
        geometry: "rectangle",
      },
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

