
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
          y: ["Country", "Value 2 (+)"],
          color: "Country",
        },
        
        align: "stretch",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          label: "Value 2 (+)",
        },
        
        align: "min",
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

