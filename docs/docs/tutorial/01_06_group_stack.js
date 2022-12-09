import("../../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Creating a stacked chart",
              channels: {
                y: { set: "Popularity" },
                x: { set: "Genres" },
              },
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: {
                  attach: "Kinds",
                },
                color: {
                  attach: "Kinds",
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
              title:
                "...then you can add it to another channel = group elements...",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: { detach: "Kinds" },
                x: { attach: "Kinds" },
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
              title: "...doing it the other way is how you stack your chart",
            },
          });
        },
        (chart) => {
          return chart.animate({
            config: {
              channels: {
                y: { attach: "Kinds" },
                x: { detach: "Kinds" },
              },
            },
          });
        },
      ],
    },
  ]);
});
