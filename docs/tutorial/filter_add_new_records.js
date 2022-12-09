import("../javascripts/mdchart.js").then((MdChart) => {
  const MdChartConstructor = MdChart.default;
  const mdchart = new MdChartConstructor("./data.js", "./vizzu.js", "tutorial");

  mdchart.create([
    {
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Filter by one dimension",
              channels: {
                y: { set: ["Popularity", "Kinds"] },
                x: { set: "Genres" },
                label: { attach: "Popularity" },
              },
              color: { attach: "Kinds" },
            },
          });
        },
        (chart) => {
          return chart.animate({
            data: {
              filter: (record) =>
                record.Genres === "Pop" || record.Genres === "Metal",
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
              title: "Filter by two dimensions",
            },
          });
        },
        (chart) => {
          return chart.animate({
            data: {
              filter: (record) =>
                (record.Genres === "Pop" || record.Genres === "Metal") &&
                record.Kinds === "Smooth",
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
              title: "Filter off",
            },
          });
        },
        (chart) => {
          return chart.animate({
            data: {
              filter: null,
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
              title: "Adding new records",
            },
          });
        },
        (chart) => {
          return chart.animate({
            data: {
              records: [
                ["Soul", "Hard", 91],
                ["Soul", "Smooth", 57],
                ["Soul", "Experimental", 115],
              ],
            },
          });
        },
      ],
    },
  ]);
});
