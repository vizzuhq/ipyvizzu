
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
                y: {
                    set: ['Value 2 (+)'],
                    /* Set enough space for 
                    tangential labels. */
                    range: { max: '130%' }
                },
                label: 'Value 2 (+)',
            },
            title: 'Polar Area Chart',
            geometry: 'area',
            coordSystem: 'polar',
        },
        style: {
            plot: {
                marker: {
                    label: {
                        orientation: 'tangential',
                        angle: 3.14 * -0.5
                    }
                }
            }
        }
    })
      ]
    }
  ]);
});

