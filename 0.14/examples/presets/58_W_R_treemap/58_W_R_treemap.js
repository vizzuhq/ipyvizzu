
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        chart => chart.animate(
        {
            data: data,
            config: chart.constructor.presets.treemap({
                size: 'Value 2 (+)',
                color: 'Country_code',
                title: 'Treemap'
            })
        }
    )
      ]
    }
  ]);
});

