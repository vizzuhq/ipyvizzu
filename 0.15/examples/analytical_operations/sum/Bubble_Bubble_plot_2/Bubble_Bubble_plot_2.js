
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data,
      config: {
        channels: {
          x: ["Joy factors", "Value 6 (+/-)"],
          y: "Value 5 (+/-)",
          color: "Joy factors",
          size: "Value 2 (+)",
          label: "Country_code",
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: ["Country_code", "Value 2 (+)"],
          y: "Joy factors",
          label: null,
        },
        
        geometry: "rectangle",
        orientation: "vertical",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Value 2 (+)",
          label: "Value 2 (+)",
        },
      },
    })
      ]
    }
  ]);
});

