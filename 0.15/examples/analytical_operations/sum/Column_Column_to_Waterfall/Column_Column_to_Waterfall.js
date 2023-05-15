
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
      data: Object.assign(data, {
        filter: (record) => record.Country == "Belgium",
      }),
      config: {
        channels: {
          x: "Year",
          y: "Value 5 (+/-)",
          color: {
            set: "Value 5 (+/-)",
            range: { min: "-45", max: "45" },
          },
          noop: "Country",
          label: "Value 5 (+/-)",
        },
        
        legend: "color",
      },
      style: {
        plot: {
          marker: {
            colorGradient: [
              "#ac1727 0",
              "#e36c56 0.15",
              "#f4b096 0.35",
              "#d5d7d9 0.5",
              "#9fbffa 0.65",
              "#6389ec 0.85",
              "#3d51b8 1",
            ].join(),
            label: { position: "top" },
          },
        },
      },
    }),(chart) =>
    chart.animate({
      config: {
        channels: {
          y: ["Year", "Value 5 (+/-)"],
        },
        
      },
    })
      ]
    }
  ]);
});

