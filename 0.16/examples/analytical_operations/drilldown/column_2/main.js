
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
          y: "Value 2 (+)",
          label: "Value 2 (+)",
        },
        
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Year",
          y: ["Country", "Value 2 (+)"],
          color: "Country",
          label: null,
        },
        
      },
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

