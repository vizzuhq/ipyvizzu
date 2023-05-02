
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_8 = results[0].data_8;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_8, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_8,

      config: {
        channels: {
          color: "Country",
          size: "Value 2 (+)",
          label: "Value 2 (+)",
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          size: ["Year", "Value 2 (+)"],
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Value 1 (+)",
          y: "Value 3 (+)",
          noop: "Year",
          size: "Value 2 (+)",
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

