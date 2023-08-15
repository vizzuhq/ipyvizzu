
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_8 = results[0].data_8;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_8, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) => {
    let f = data_8.filter;
    return chart.animate({
      data: Object.assign(data_8, {
        filter: (record) => f(record) && record.Year >= 15,
      }),
      config: {
        channels: {
          x: ["Country", "Value 2 (+)"],
          y: {
            set: "Year",
            range: { min: "-3" },
          },
          color: "Country",
        },
        
        coordSystem: "polar",
      },
    });
  },(chart) =>
    chart.animate({
      config: {
        
        split: true,
      },
    })
      ]
    }
  ]);
});

