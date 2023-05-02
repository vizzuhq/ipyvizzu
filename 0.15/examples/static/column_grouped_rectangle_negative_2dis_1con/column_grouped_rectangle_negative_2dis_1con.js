
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
          x: ["Joy factors", "Country"],
          y: "Value 5 (+/-)",
          color: "Joy factors",
          label: "Value 5 (+/-)",
        },
        title: "Grouped Column Chart",
      },
      // Labels have to be rotated on this chart.
      style: {
        plot: {
          marker: {
            label: {
              fontSize: 6,
              orientation: "vertical",
              angle: 3.14 * -1,
            },
          },
        },
      },
    })
      ]
    }
  ]);
});

