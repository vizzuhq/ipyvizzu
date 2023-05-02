
const dataLoaded = import("../../../assets/data/tutorial.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data,
      config: {
        channels: {
          x: "Timeseries",
          y: {
            set: ["Values 1", "Categ. Parent"],
            /* Making the chart elements fill the whole of
             the y-axis as the default value is now 110% */
            range: {
              max: "400",
            },
          },
          label: "Values 1",
          color: "Categ. Parent",
        },
        title: "Stacked Area Chart",
        geometry: "area",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: "Values 1",
        },
        title: "Line Chart",
        geometry: "line",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: {
            /* Setting back the y-axis range
          to the default value. */
            range: {
              max: "auto",
            },
          },
        },
      },
    })
      ]
    }
  ]);
});

