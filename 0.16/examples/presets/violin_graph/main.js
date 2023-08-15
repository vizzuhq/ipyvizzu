
const dataLoaded = import("../../../assets/data/music_industry_history_1.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
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
      config: chart.constructor.presets.violin({
        x: "Year",
        y: "Revenue [$]",
        splittedBy: "Format",
        title: "Violin Graph",
      }),
      style: {
        plot: {
          yAxis: { interlacing: { color: "#ffffff00" } },
          yAxis: { label: { numberScale: "K, M, B, T" } },
          xAxis: { label: { angle: "-45deg" } },
        },
      },
    })
      ]
    }
  ]);
});

