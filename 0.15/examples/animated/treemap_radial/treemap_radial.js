
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
                size: 'Value 2 (+)',
                label: 'Joy factors'
            },
            title: 'Treemap'
        }
    }),chart => chart.animate({
        config: {
            channels: {
                x: 'Value 2 (+)',
                y: { set: 'Joy factors',
                    /* Setting the radius of
                    the empty circle in the centre. */
                    range: {
                        min: '-30%',
                    }
                },
                size: null,
                label: 'Value 2 (+)'
            },
            title: 'Radial Chart',
            coordSystem: 'polar'
        }
    })
      ]
    }
  ]);
});

