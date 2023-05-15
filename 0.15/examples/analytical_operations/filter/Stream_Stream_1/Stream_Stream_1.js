
const dataLoaded = import("../../../../assets/data/music_industry_history_1.js");
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
      data: Object.assign(data, {
        filter: (record) => record.Format == "Tapes" && record["Year"] <= 1981,
      }),
      config: {
        channels: {
          x: ["Year"],
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
      data: {
        filter: (record) =>
          (record.Format == "Tapes" || record.Format == "Vinyl") &&
          record["Year"] <= 1989,
      },
      config: {
        
      },
    }),(chart) => {
    chart.on("plot-axis-label-draw", (event) => {
      let year = parseFloat(event.data.text);
      if (!event.data.text.includes("$") && !isNaN(year) && year % 5 != 0)
        event.preventDefault();
    });
    return chart;
  },(chart) =>
    chart.animate({
      data: {
        filter: (record) =>
          (record.Format == "Tapes" ||
            record.Format == "Cassette" ||
            record.Format == "Vinyl") &&
          record["Year"] <= 1999,
      },
      config: {
        
      },
    }),(chart) =>
    chart.animate({
      data: {
        filter: (record) =>
          record.Format == "DVD" ||
          record.Format == "Other" ||
          record.Format == "Tapes" ||
          record.Format == "Cassette" ||
          record.Format == "Vinyl" ||
          record.Format == "CD",
      },
      config: {
        
      },
    }),(chart) =>
    chart.animate({
      data: {
        filter: (record) =>
          record.Format == "DVD" ||
          record.Format == "Other" ||
          record.Format == "Tapes" ||
          record.Format == "Download" ||
          record.Format == "Cassette" ||
          record.Format == "Vinyl" ||
          record.Format == "CD",
      },
      config: {
        
      },
    }),(chart) =>
    chart.animate({
      data: {
        filter: (record) =>
          record.Format == "DVD" ||
          record.Format == "Other" ||
          record.Format == "Tapes" ||
          record.Format == "Download" ||
          record.Format == "Streaming" ||
          record.Format == "Cassette" ||
          record.Format == "Vinyl" ||
          record.Format == "CD",
      },
      config: {
        
      },
    }),(chart) => {
    chart.feature("tooltip", true);
    return chart;
  }
      ]
    }
  ]);
});

