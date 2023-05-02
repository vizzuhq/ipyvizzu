
const dataLoaded = import("../../../assets/data/infinite_data.js");
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
          x: ["Value 1", "Joy factors"],
          color: "Joy factors",
          label: "Value 1",
        },
        title: "Pie Chart",
        coordSystem: "polar",
      },
    }),(chart) =>
    chart.animate(
      {
        config: {
          channels: {
            x: ["Value 1", "Joy factors", "Region", "Country code"],
            label: null,
          },
        },
      },
      "500ms"
    ),(chart) =>
    chart.animate({
      config: {
        channels: {
          x: ["Value 1", "Joy factors", "Region", "Country code"],
          y: {
            set: "Value 3",
            /* Setting the radius of the empty circle
                    in the centre. */
            range: { min: "-60%" },
          },
        },
        title: "Coxcomb Chart",
      },
    })
      ]
    }
  ]);
});

