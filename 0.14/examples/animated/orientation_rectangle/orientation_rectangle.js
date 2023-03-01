
const dataLoaded = import("../../../assets/data/tutorial.js");
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
        x: 'Timeseries',
        y: ['Values 1', 'Categ. Parent'],
        color: 'Categ. Parent',
        label: 'Values 1'
      },
      title: 'Stacked Column Chart'
    }
  }),chart => chart.animate({
    config: {
      channels: {
        /* Taking the dimension off to show the sum of
        the newly stacked elements. */
        x: 'Values 1',
        y: 'Categ. Parent', 
      },
      title: 'Bar Chart'
    }
  })
      ]
    }
  ]);
});

