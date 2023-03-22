
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
                x: 'Year',
                /* Adding the same dimension (Year) on both axes is
                how you create a Waterfall Chart in Vizzu. */
                y: ['Year', 'Value 5 (+/-)'], 
                label: 'Value 5 (+/-)'
            },
            title: 'Waterfall Chart',
            legend: null
        },
        style: {
            plot: {
                marker: {
                    label: {
                        position: 'top'
                    }
                }
            }
        }
    })
      ]
    }
  ]);
});

