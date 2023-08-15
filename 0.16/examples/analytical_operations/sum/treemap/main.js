
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
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
          size: "Value 2 (+)",
          /* The noop channel (no operation) splits the markers as all the other channels
        but will have no effect on the markers’ appearance. */
          noop: "Country_code",
          color: "Joy factors",
          label: "Country_code",
        },
        
      },
    }),(chart) =>
    chart.animate({
      config: {
        /* With a dimension on the size channel Vizzu will stack the elements
      by the categories on the other channels on charts without coordinates.
      Here the Country code dimension is used to stack the bubbles
      by the dimension on the color channel. */
        channels: {
          size: ["Country_code", "Value 2 (+)"],
        },
        
      },
    })
      ]
    }
  ]);
});

