
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_6 = results[0].data_6;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_6, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) => {
    let f = data_6.filter;
    return chart.animate({
      data: Object.assign(data_6, {
        filter: (record) => f(record) && record.Year >= 10,
      }),

      config: {
        channels: {
          x: "Year",
          y: ["Country", "Value 2 (+)"],
          color: "Country",
        },
        
      },
    });
  },(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Joy factors",
          //                label: 'Value 2 (+)'
        },
        
      },
    })
      ]
    }
  ]);
});

