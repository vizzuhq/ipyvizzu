
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
            data: Object.assign(data, {
                filter: record => record.Country == 'Belgium'
            }),
            config: chart.constructor.presets.waterfall({
                x: 'Year',
                y: 'Value 5 (+/-)',
                title: 'Waterfall Chart'
            }),
            style:
            {
                plot: {
                    marker: {
                        colorGradient:
                            [
                                '#ff001b 0',
                                '#ff001b 0.5',
                                '#7e79e8 0.5',
                                '#7e79e8 1'
                            ].join(),
                        label: {
                            position: 'top'
                        }
                    }
                }
            }
        }
    )
      ]
    }
  ]);
});

