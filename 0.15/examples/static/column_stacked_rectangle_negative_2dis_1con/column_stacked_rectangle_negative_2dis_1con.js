
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
                x: 'Country',
                y: ['Joy factors', 'Value 2 (+)'],
                color: 'Joy factors',
                label: 'Value 2 (+)'
            },
            title: 'Stacked Column Chart'
        },
        // Labels have to be rotated on this chart.
        style: { 
            plot: {
                xAxis: {
                    label: {
                        angle: 2.3
                    }
                },
                marker: {
                    label: {
                        fontSize: 7,
                        orientation: 'vertical',
                        angle: 3.14 * -1
                    }
                }
            }
        }
    })
      ]
    }
  ]);
});

