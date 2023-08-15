
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
          x: "Year",
          y: ["Country", "Value 2 (+)"],
          color: "Country",
          label: "Value 2 (+)",
        },
        
        split: true,
      },
      style: {
        plot: {
          marker: {
            label: {
              position: "top",
              fontSize: "0.6em",
            },
          },
        },
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Value 5 (+/-)",
          y: "Value 2 (+)",
          label: "Year",
        },
        
        geometry: "circle",
        split: false,
      },
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

