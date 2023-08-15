
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
          x: "Value 5 (+/-)",
          y: "Value 6 (+/-)",
          /* The noop channel splits the markers as all the other channels
                but will have no effect on the markers’ appearance. */
          noop: "Joy factors",
          /* Lightness channel is used to assist the viewer
                in following the animation. */
          lightness: "Year",
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Year",
        },
        
        orientation: "horizontal",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Value 5 (+/-)",
        },
        
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: "Joy factors",
          noop: null,
        },
        
        orientation: "vertical",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: "Value 6 (+/-)",
          noop: "Joy factors",
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

