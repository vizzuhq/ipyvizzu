
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
          x: "Year",
          y: ["Value 2 (+)", "Country_code"],
          color: "Country_code",
        },
        
        geometry: "area",
        coordSystem: "polar",
      },
    }),(chart) =>
    chart.animate({
      data: {
        filter: (record) =>
          record["Country_code"] == "FR" || record["Country_code"] == "CY",
      },
      config: {
        
      },
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

