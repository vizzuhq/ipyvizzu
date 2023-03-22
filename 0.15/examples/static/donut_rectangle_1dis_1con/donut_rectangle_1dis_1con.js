
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
                x: ['Joy factors', 'Value 2 (+)'],
                /* Setting the radius of the empty circle
                in the centre. */
                y: { range: { min: '-200%' } }, 
                color: 'Joy factors',
                label: 'Value 2 (+)'
            },
            title: 'Donut Chart',
            coordSystem: 'polar'
        }
    })
      ]
    }
  ]);
});

