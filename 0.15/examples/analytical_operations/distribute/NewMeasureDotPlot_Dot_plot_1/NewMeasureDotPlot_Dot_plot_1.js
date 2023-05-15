
const dataLoaded = import("../../../../assets/data/IMDB_data.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_1974_1990 = results[0].data_1974_1990;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_1974_1990, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_1974_1990,
      config: {
        channels: {
          x: "Year",
          y: { set: "Index", range: { max: "105%" } },
        },
        
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: { set: "IMDb Rating", range: { max: "105%" } },
          noop: "Index",
        },
        
        orientation: "vertical",
        split: true,
      },
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

