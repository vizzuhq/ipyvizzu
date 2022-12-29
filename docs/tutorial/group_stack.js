const dataLoaded = import("../data/music_data.js");
const mdChartLoaded = import("../javascripts/mdchart.js");

Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].default;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "tutorial");

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
