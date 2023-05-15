
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
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
      data: Object.assign(data, {
        filter: (record) =>
          ["AT", "BE", "DE", "DK", "ES", "FI", "FR", "IT", "NL", "SE"].includes(
            record.Country_code
          ),
      }),
      config: {
        channels: {
          x: ["Year", "Joy factors"],
          y: ["Value 3 (+)", "Country_code"],
          color: "Country_code",
        },
        title: "Stacked Streamgraph",
        geometry: "area",
        align: "center",
      },
    })
      ]
    }
  ]);
});

