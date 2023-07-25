const csv2JsLoaded = import("../../assets/javascripts/csv2js.js");
const vizzuLoaded = import("../../assets/javascripts/vizzu.js").then(
  (vizzuUrl) => {
    return import(vizzuUrl.default);
  },
);

Promise.all([csv2JsLoaded, vizzuLoaded]).then((results) => {
  const Csv2Js = results[0].default;
  const Vizzu = results[1].default;

  const dataLoaded = Csv2Js.csv("./titanic.csv");

  dataLoaded.then((data) => {
    new Vizzu("testVizzuCanvas", { data }).initializing.then((chart) => {
      chart.animate({
        config: {
          x: "Count",
          y: "Sex",
          label: "Count",
          title: "Passengers of the Titanic",
        },
      });

      chart.animate({
        config: {
          x: ["Count", "Survived"],
          label: ["Count", "Survived"],
          color: "Survived",
        },
      });

      chart.animate({
        config: { x: "Count", y: ["Sex", "Survived"] },
      });

      chart.animate({
        config: {
          x: ["Count", "Sex", "Survived"],
          y: null,
          coordSystem: "polar",
        },
      });
    });
  });
});
