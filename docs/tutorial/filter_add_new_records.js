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
      initDataFilter: (record) =>
        record.Genres === "Pop" || record.Genres === "Metal",
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
      initDataFilter: (record) =>
        (record.Genres === "Pop" || record.Genres === "Metal") &&
        record.Kinds === "Smooth",
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
      initDataFilter: (record) => record.Genres !== "Soul",
      anims: [
        (chart) => {
          return chart.animate({
            config: {
              title: "Adding new records",
            },
          });
        },
        (chart, metadata) => {
          return metadata.dataLoaded.then((data) => {
            const expandedData = JSON.parse(JSON.stringify(data));

            expandedData.series[0].values.splice(5, 0, "Soul");
            expandedData.series[0].values.splice(9, 0, "Soul");
            expandedData.series[0].values.splice(14, 0, "Soul");

            expandedData.series[1].values.splice(5, 0, "Hard");
            expandedData.series[1].values.splice(9, 0, "Smooth");
            expandedData.series[1].values.splice(14, 0, "Experimental");

            expandedData.series[2].values.splice(5, 0, 91);
            expandedData.series[2].values.splice(9, 0, 57);
            expandedData.series[2].values.splice(14, 0, 115);

            expandedData.filter = null;

            return chart.animate(
              {
                data: expandedData,
              },
              2
            );
          });
        },
      ],
    },
  ]);
});
