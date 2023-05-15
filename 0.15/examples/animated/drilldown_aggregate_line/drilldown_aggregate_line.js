
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
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
          x: "Year",
          y: {
            set: "Value 3 (+)",
            /* Making the chart elements fill the whole of
                    the y-axis as the default value is now 110% */
            range: {
              max: "6000000000",
            },
          },
          /* Add the dimension that we’ll use 
                in the next state without splitting
                the lines in this state. */
          size: "Country",
        },
        title: "Single Line Chart",
        geometry: "line",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          color: "Country",
          /* We don’t need this dimension here anymore
                since it’s already on the 'color' channel. */
          size: null,
        },
        title: "Drill down",
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
        title: "Line Chart II",
      },
    })
      ]
    }
  ]);
});

