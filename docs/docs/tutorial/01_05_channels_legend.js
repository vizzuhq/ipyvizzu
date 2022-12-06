import("../../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Label",
              channels: {
                y: { set: ["Popularity"] },
                x: { set: ["Genres"] },
              },
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                label: {
                  attach: "Popularity",
                },
              },
            },
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Lightness - legend on",
              channels: {
                lightness: {
                  attach: "Popularity",
                },
              },
              legend: "lightness",
            },
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Color",
              channels: {
                lightness: {
                  set: null,
                },
                color: {
                  attach: "Genres",
                },
              },
              legend: "color",
            },
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Color",
              channels: {
                size: {
                  set: "Popularity",
                },
              },
              geometry: "circle",
            },
          });
        },
      ],
    },
  ]);
});
