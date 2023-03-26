
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
                x: 'Value 2 (+)',
                y: {
                    set: ['Joy factors'],
                    /* Setting the radius of the empty circle
                    in the centre. */
                    range: { min: '-30%' }
                },
                color: 'Joy factors',
                label: 'Value 2 (+)'
            },
            title: 'Radial Bar Chart',
            coordSystem: 'polar'
        }
    })
      ]
    }
  ]);
});

