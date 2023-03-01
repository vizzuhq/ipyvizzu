
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        chart => chart.animate({
    data: data,
    config: {
      channels: {
        color: 'Joy factors',
        size: ['Country_code', 'Value 2 (+)'],
        label: 'Country_code'
      },
      title: 'Stacked Bubble Chart',
      geometry: 'circle'
    }
  })
      ]
    }
  ]);
});

