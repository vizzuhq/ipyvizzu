const csv2JsLoaded = import("../../../javascripts/csv2js.js");
const mdChartLoaded = import("../../../javascripts/mdchart.js");

Promise.all([csv2JsLoaded, mdChartLoaded]).then((results) => {
  const Csv2Js = results[0].default;
  const MdChart = results[1].default;

  const csv2js = new Csv2Js();
  const dataLoaded = csv2js.getData("./music.csv");

  dataLoaded.then((data) => {
    const mdchart = new MdChart(data, "./vizzu.js", "example");

    mdchart.create([
      {
        anims: [
          (chart) => {
            return chart.animate({
              config: {
                title: "Revenue by Music Format 1973-2020",
                x: "Year",
                y: ["Format", "Revenue [m$]"],
                color: "Format",
                geometry: "area",
                align: "center",
              },
              style: {
                plot: {
                  xAxis: { label: { fontSize: 9, angle: 2.0 } },
                  marker: {
                    colorPalette:
                      "#b74c20FF #c47f58FF #1c9761FF" +
                      " #ea4549FF #875792FF #3562b6FF" +
                      " #ee7c34FF #efae3aFF",
                  },
                },
              },
            });
          },
          (chart) => {
            return chart.animate({
              config: {
                title: "Revenue by Music Format 1973-2020(%)",
                align: "stretch",
              },
              delay: 1,
            });
          },
          (chart) => {
            return chart.animate({
              config: {
                title: "Revenue by Music Format 1973-2020",
                align: "center",
              },
              delay: 1,
            });
          },
          (chart) => {
            return chart.animate({
              config: {
                split: true,
              },
              delay: 1,
            });
          },
          (chart) => {
            return chart.animate({
              data: {
                filter: (record) => {
                  return (
                    record.Format === "Vinyl" || record.Format === "Streaming"
                  );
                },
              },
              config: {
                title: "Revenue of Vinyl & Streaming 1973-2020",
              },
              delay: 1,
            });
          },
          (chart) => {
            return chart.animate({
              data: { filter: null },
              config: {
                title: "Revenue by Music Format 1973-2020",
                split: false,
              },
              delay: 1,
            });
          },
          (chart) => {
            return chart.animate({
              config: {
                x: "Year",
                y: "Revenue [m$]",
                noop: "Format",
                align: "none",
                geometry: "line",
              },
              delay: 1,
            });
          },
        ],
      },
    ]);
  });
});
