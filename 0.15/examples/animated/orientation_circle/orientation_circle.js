
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
                x: 'Value 5 (+/-)',
                y: 'Joy factors',
                /* Lightness channel is used to assist the viewer
                in following the animation. */
                lightness: 'Joy factors',
                /* The noop channel splits the markers as all the other channels
                but will have no effect on the markers’ appearance. */
                noop: 'Year'
            },
            title: 'Dot Plot',
            geometry: 'circle'
        }
    }),chart => chart.animate({
        config: {
            channels: {
                x: 'Year',
                y: 'Value 5 (+/-)',
                noop: 'Joy factors'
            },
            title: 'Dot Plot with Other Orientation'
        }
    })
      ]
    }
  ]);
});

