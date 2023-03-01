
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_6 = results[0].data_6;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_6, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        chart => chart.animate(
        {
            data: data_6,
            config: chart.constructor.presets.radialStackedBar({
                angle: 'Value 2 (+)',
                radius: 'Country',
                stackedBy: 'Joy factors',
                title: 'Radial Stacked Bar Chart'
            })
        }
    )
      ]
    }
  ]);
});

