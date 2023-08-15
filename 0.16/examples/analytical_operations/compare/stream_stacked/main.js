
const dataLoaded = import("../../../../assets/data/music_industry_history_1.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) => {
    chart.on("plot-axis-label-draw", (event) => {
      let year = parseFloat(event.data.text);
      if (!event.data.text.includes("$") && !isNaN(year) && year % 5 != 0)
        event.preventDefault();
    });
    return chart;
  },(chart) =>
    chart.animate({
      data: Object.assign(data, {
        filter: (record) => record["Year"] > 1972,
      }),
      config: {
        channels: {
          x: "Year",
          y: ["Revenue [$]", "Format"],
          color: "Format",
        },
        
        geometry: "area",
        align: "center",
      },
      style: {
        plot: {
          yAxis: {
            label: {
              numberScale: "K, M, B, T",
            },
          },
        },
      },
    }),(chart) =>
    chart.animate({
      config: {
        
        align: "min",
        split: true,
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: ["Format", "Year"],
          y: "Revenue [$]",
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

