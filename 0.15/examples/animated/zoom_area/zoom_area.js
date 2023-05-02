
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
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
          x: ["Year", "Joy factors"],
          y: ["Value 3 (+)", "Country_code"],
          color: "Country_code",
        },
        title: "Stacked Area",
        geometry: "area",
      },
    }),(chart) =>
    chart.animate({
      data: {
        filter: (record) =>
          data_6.filter(record) && record.Year < 12 && record.Year > 6,
      },
      config: {
        title: "Zoomed Stacked Area",
      },
    })
      ]
    }
  ]);
});

