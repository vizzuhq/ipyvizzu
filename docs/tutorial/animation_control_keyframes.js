const dataLoaded = import("../assets/data/music_data.js");
const mdChartLoaded = import("../assets/javascripts/mdchart.js");

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
              title: "Using keyframes",
              channels: {
                y: { set: ["Popularity", "Kinds"] },
                x: { set: "Genres" },
                label: { attach: "Popularity" },
              },
              color: { set: "Kinds" },
            },
          });
        },
        (chart) => {
          return chart.animate([
            {
              target: {
                config: {
                  channels: {
                    x: {
                      attach: ["Kinds"],
                    },
                    y: {
                      detach: ["Kinds"],
                    },
                  },
                  title: "Using keyframes",
                },
              },
              options: {
                duration: 0.5,
              },
            },
            {
              target: {
                config: {
                  channels: {
                    x: {
                      detach: ["Kinds"],
                    },
                    y: {
                      attach: ["Kinds"],
                    },
                  },
                },
              },
              options: {
                duration: 1,
              },
            },
          ]);
        },
      ],
    },
  ]);
});
