
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_6 = results[0].data_6;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_6, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_6,

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
          x: ["Country", "Year"],
          y: "Value 2 (+)",
          label: null,
        },
        
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

