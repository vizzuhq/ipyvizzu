
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
          color: "Joy factors",
          label: "Country_code",
          /* With a dimension on the size channel Vizzu will stack
                the elements by the categories on the other channels
                on charts without coordinates. Here the Country code dimension is
                used to stack the bubbles by the dimension on the color channel. */
          size: ["Country_code", "Value 2 (+)"],
        },
        title: "Stacked Bubble Chart",
        geometry: "circle",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: "Joy factors",
          y: ["Country_code", "Value 2 (+)"],
          label: null,
          /* The stacking is eliminated when we remove
                the extra dimension from the size channel. */
          size: null,
        },
        title: "Column Chart",
        geometry: "rectangle",
        orientation: "vertical",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: "Value 2 (+)",
          label: "Value 2 (+)",
        },
      },
    })
      ]
    }
  ]);
});

