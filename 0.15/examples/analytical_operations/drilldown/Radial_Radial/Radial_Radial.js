
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
          x: "Value 2 (+)",
          y: { set: "Country", range: { min: "-30%" } },
          label: "Value 2 (+)",
        },
        
        coordSystem: "polar",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: ["Value 2 (+)", "Joy factors"],
          color: "Joy factors",
          label: null,
        },
        
      },
      style: {
        plot: {
          marker: {
            colorPalette: "#ef675aFF #6d8cccFF #e6cf99FF #9c50abFF",
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

