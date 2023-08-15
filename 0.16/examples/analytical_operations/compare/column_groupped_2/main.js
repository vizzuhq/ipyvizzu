
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
          x: ["Country", "Year"],
          y: "Value 2 (+)",
          color: "Country",
        },
        
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Year",
          y: ["Country", "Value 2 (+)"],
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
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

