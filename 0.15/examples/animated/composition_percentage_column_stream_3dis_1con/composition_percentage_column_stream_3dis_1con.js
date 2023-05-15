
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_14 = results[0].data_14;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_14, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_14,
      config: {
        channels: {
          x: "Year",
          y: ["Value 2 (+)", "Country"],
          /* The noop channel splits the markers as all the other channels
                but will have no effect on the markers’ appearance. */
          noop: "Country",
        },
        title: "Column Chart",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: {
            /* Making the chart elements fill the whole of the y-axis
                    as the default value is now 110% */
            range: {
              max: "100%",
            },
          },
          color: "Country",
          noop: null,
        },
        title: "Split Column Chart",
        split: true,
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: {
            /* Setting back the y-axis range to the default value. */
            range: {
              max: "auto",
            },
          },
        },
        title: "Stacked Column Chart",
        split: false,
      },
    }),(chart) =>
    chart.animate({
      config: {
        title: "100% Column Chart",
        align: "stretch",
      },
    })
      ]
    }
  ]);
});

