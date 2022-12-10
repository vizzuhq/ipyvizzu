import("../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Using a preset",
            },
          });
        },
        (chart, metadata) => {
          return metadata.vizzuLoaded.then((Vizzu) => {
            const VizzuConstructor = Vizzu.default;
            return chart.animate(
              VizzuConstructor.presets.stackedBubble({
                size: "Popularity",
                color: "Kinds",
                stackedBy: "Genres",
              })
            );
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Set sorting for a chart preset",
            },
          });
        },
        (chart, metadata) => {
          return metadata.vizzuLoaded.then((Vizzu) => {
            const VizzuConstructor = Vizzu.default;
            return chart.animate(
              VizzuConstructor.presets.radialStackedBar({
                angle: "Popularity",
                radius: "Genres",
                stackedBy: "Kinds",
                sort: "byValue",
              })
            );
          });
        },
      ],
    },
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Setting style for a preset",
            },
          });
        },
        (chart, metadata) => {
          return metadata.vizzuLoaded.then((Vizzu) => {
            const VizzuConstructor = Vizzu.default;
            return chart.animate({
              config: VizzuConstructor.presets.radialBar({
                angle: "Popularity",
                radius: "Genres",
              }),
              style: {
                "plot.xAxis.interlacing.color": "#ffffff00",
              },
            });
          });
        },
      ],
    },
  ]);
});
