const csv2JsLoaded = import("../../../javascripts/csv2js.js");
const mdChartLoaded = import("../../../javascripts/mdchart.js");

Promise.all([csv2JsLoaded, mdChartLoaded]).then((results) => {
  const Csv2Js = results[0].default;
  const MdChart = results[1].default;

  const dataLoaded = Csv2Js.csv("./titanic/titanic.csv");

  dataLoaded.then((data) => {
    const mdchart = new MdChart(data, "./vizzu.js", "example");

    mdchart.create([
      {
        anims: [
          (chart) => {
            return chart.animate({
              config: {
                x: "Count",
                y: "Sex",
                label: "Count",
                title: "Passengers of the Titanic",
              },
            });
          },
          (chart) => {
            return chart.animate({
              config: {
                x: ["Count", "Survived"],
                label: ["Count", "Survived"],
                color: "Survived",
              },
            });
          },
          (chart) => {
            return chart.animate({
              config: { x: "Count", y: ["Sex", "Survived"] },
            });
          },
          (chart) => {
            return chart.animate({
              config: {
                x: ["Count", "Sex", "Survived"],
                y: null,
                coordSystem: "polar",
              },
            });
          },
        ],
      },
    ]);
  });
});
