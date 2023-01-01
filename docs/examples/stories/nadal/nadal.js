const csv2JsLoaded = import("../../../javascripts/csv2js.js");
const mdChartLoaded = import("../../../javascripts/mdchart.js");

Promise.all([csv2JsLoaded, mdChartLoaded]).then((results) => {
  const Csv2Js = results[0].default;
  const MdChart = results[1].default;

  const dataLoaded = Csv2Js.csv("./nadal/nadal.csv", [
    "Year",
    "Round2",
    "Order_GS",
    "Order_all",
  ]);

  dataLoaded.then((data) => {
    const mdchart = new MdChart(data, "./vizzu.js", "example");

    mdchart.create([
      {
        anims: [
          (chart) => {
            return chart.animate({
              data: {
                filter: (record) => {
                  return record.Year !== "Total";
                },
              },
              config: {
                x: "Year",
                y: "Round2",
                color: { set: "Result_Num", range: { min: -1, max: 1 } },
                size: null,
                orientation: "horizontal",
                geometry: "rectangle",
                title: "Rafael Nadal's matches at the Roland Garros",
                legend: "size",
              },
              style: {
                fontSize: 10,
                title: {
                  fontWeight: 300,
                  paddingTop: 50,
                  paddingBottom: 0,
                },
                plot: {
                  marker: {
                    borderWidth: 3,
                    borderOpacity: 0,
                    colorPalette: "#1EB55FFF #AD0000FF #AEAEAEFF",
                    colorGradient:
                      "#AEAEAEFF 0.000000, #AD0000FF 0.500000, #1EB55FFF 1.000000",
                  },
                  paddingLeft: 20,
                  paddingBottom: "3.5em",
                  paddingTop: "2.5em",
                  xAxis: { interlacing: { color: "#ffffff00" } },
                  yAxis: { label: { fontSize: "120%" } },
                },
                logo: { width: 100 },
              },
            });
          },
          (chart) => {
            return chart.animate(
              {
                config: {
                  lightness: "Won",
                  title: "Won 112 out of 116 (96.5%)",
                },
                style: {
                  plot: { marker: { maxLightness: 0, minLightness: 0.8 } },
                },
              },
              { delay: 4 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: {
                  lightness: "Lost",
                  title: "Lost 3 times, retired once",
                },
              },
              { delay: 4 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: { lightness: null, title: "" },
                style: {
                  plot: { marker: { maxLightness: null, minLightness: null } },
                },
              },
              { delay: 4 }
            );
          },
          (chart) => {
            return chart.animate({
              config: {
                lightness: "3SetWin",
                title: "90 wins (80%) in straight sets",
              },
              style: {
                plot: { marker: { maxLightness: 0, minLightness: 0.8 } },
              },
            });
          },
          (chart) => {
            return chart.animate(
              {
                config: {
                  lightness: "Straightwin",
                  title: "Won 4 titles without dropping a set",
                },
              },
              { delay: 3 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: { lightness: null, title: "" },
                style: {
                  plot: { marker: { maxLightness: null, minLightness: null } },
                },
              },
              { delay: 4 }
            );
          },
          (chart) => {
            return chart.animate({
              config: {
                lightness: "Novak",
                title: "Played the most times against Djokovic - 10 matches",
              },
              style: {
                plot: { marker: { maxLightness: 0, minLightness: 0.8 } },
              },
            });
          },
          (chart) => {
            return chart.animate(
              {
                config: {
                  lightness: "Roger",
                  title: "Second on this list is Federer - with 6 encounters",
                },
              },
              { delay: 4 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: {
                  lightness: "Final",
                  title: "Rafa won all of his 14 finals",
                },
              },
              { delay: 4 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                data: {
                  filter: (record) => {
                    return record.Year !== "Total" && record.Round === "F";
                  },
                },
                condig: {
                  y: { set: "Round2", range: { max: 1, min: -5 } },
                  x: "Count",
                  lightness: null,
                  noop: "Year",
                  label: null,
                  title: "",
                },
                style: {
                  plot: {
                    marker: {
                      borderWidth: 0,
                      colorPalette:
                        "#C6652A #CDA02E #47B0FF #329564 #5C88F2 #91A9B5 #DBC4B1",
                      maxLightness: null,
                      minLightness: null,
                      label: {
                        position: "center",
                        format: "dimensionsFirst",
                      },
                    },
                    xAxis: {
                      title: { color: "#ffffff00" },
                      label: { color: "#ffffff00" },
                      interlacing: { color: "#ffffff00" },
                    },
                    yAxis: {
                      title: { color: "#ffffff00" },
                      label: { color: "#ffffff00", fontSize: null },
                    },
                  },
                },
              },
              { delay: 3 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                data: {
                  filter: (record) => {
                    return (
                      record.Year === "Total" &&
                      record.Tournament === "Roland Garros" &&
                      record.Player === "Nadal"
                    );
                  },
                },
                config: {
                  noop: ["Level", "Round2"],
                  label: ["Player", "Tournament", "Count"],
                  y: { set: ["Player", "Tournament"] },
                },
              },
              { duration: 0 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: { noop: "Level" },
              },
              { duration: 0 }
            );
          },
          (chart) => {
            return chart.animate({
              data: {
                filter: (record) => {
                  return (
                    record.Year === "Total" &&
                    record.Round === "GS" &&
                    record.Top === "1"
                  );
                },
              },
              config: {
                y: {
                  set: ["Player", "Tournament", "Level"],
                  range: { max: null, min: null },
                },
                title: "Rafa won the same Grand Slam title the most times",
                color: "Level",
                legend: "color",
                noop: null,
                sort: "byValue",
              },
            });
          },
          (chart) => {
            return chart.animate(
              {
                data: {
                  filter: (record) => {
                    return record.Year === "Total" && record.Top === "1";
                  },
                },
                config: {
                  y: {
                    set: ["Player", "Tournament", "Level"],
                    range: { max: 19, min: 7 },
                  },
                  x: ["Count"],
                  title:
                    "Winning the same ATP title - Rafa is 1st, 2nd, 3rd & 4th!",
                },
              },
              { delay: 5 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                data: {
                  filter: (record) => {
                    return (
                      record.Year === "Total" &&
                      record.Round === "GS" &&
                      record.Top === "1"
                    );
                  },
                },
                config: {
                  y: {
                    set: ["Player", "Tournament", "Level"],
                    range: { max: null, min: null },
                  },
                  x: ["Count"],
                  title: "",
                  color: "Level",
                },
              },
              { delay: 5 }
            );
          },
          (chart) => {
            return chart.animate({
              config: { x: ["Count", "Total_GS"], label: "Player" },
            });
          },
          (chart) => {
            return chart.animate({
              data: {
                filter: (record) => {
                  return record.Year === "Total" && record.Round === "GS";
                },
              },
              config: {
                y: { set: ["Player"], range: { max: null, min: null } },
                x: ["Count", "Tournament", "Level", "Total_GS"],
                title: "Rafa also leads in the number of total Grand Slams won",
              },
            });
          },
          (chart) => {
            return chart.animate({
              config: { label: ["Total_GS"] },
              style: {
                plot: {
                  marker: {
                    label: {
                      position: "right",
                      filter: "color(#666666FF)",
                    },
                  },
                },
              },
            });
          },
        ],
      },
    ]);
  });
});
