
const dataLoaded = import("../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_6 = results[0].data_6;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_6, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
    chart.animate({
      data: data_6,
      config: {
        channels: {
          x: ["Year", "Joy factors"],
          y: ["Value 3 (+)", "Country"],
          color: "Country",
        },
        title: "Stacked Streamgraph",
        geometry: "area",
        align: "center",
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: {
            /* Making the chart elements fill the whole of
                        the y-axis as the default value is now 110% */
            range: {
              max: "100%",
            },
          },
        },
        title: "Split Area Chart",
        split: true,
        align: "min",
      },
    })
      ]
    }
  ]);
});

