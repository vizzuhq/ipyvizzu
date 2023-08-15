
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
          x: ["Country", "Value 2 (+)"],
          y: { range: { min: "-200%" } },
          color: "Country",
          label: "Value 2 (+)",
        },
        
        coordSystem: "polar",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: ["Year", "Value 2 (+)"],
          y: { set: "Country", range: { min: "-30%" } },
          label: null,
        },
        
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Year",
          y: { set: ["Country", "Value 2 (+)"], range: { min: "-30%" } },
        },
        
      },
      style: {
        plot: {
          marker: {
            rectangleSpacing: "0.1em",
          },
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

