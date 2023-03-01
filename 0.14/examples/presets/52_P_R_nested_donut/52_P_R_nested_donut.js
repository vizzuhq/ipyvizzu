
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_3 = results[0].data_3;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_3, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        chart => chart.animate(
        {
            data: data_3,
            config: chart.constructor.presets.nestedDonut({
                angle: 'Value 2 (+)',
                stackedBy: 'Joy factors',
                radius: 'Country',
                title: 'Nested Donut Chart'
            }),
            style: {
                plot: {
                    marker: {
                        rectangleSpacing: '0',
                        borderWidth: 1,
                        borderOpacity: 0
                    }
                }
            }
        }
    )
      ]
    }
  ]);
});

