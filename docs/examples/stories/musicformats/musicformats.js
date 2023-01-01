const csv2JsLoaded = import("../../../javascripts/csv2js.js");
const mdChartLoaded = import("../../../javascripts/mdchart.js");

Promise.all([csv2JsLoaded, mdChartLoaded]).then((results) => {
  const Csv2Js = results[0].default;
  const MdChart = results[1].default;

  const dataLoaded = Csv2Js.csv("./musicformats/musicformats.csv", ["Year"]);

  dataLoaded.then((data) => {
    const mdchart = new MdChart(data, "./vizzu.js", "example");

    const config = {
      channels: {
        y: {
          set: ["Format"],
        },
        x: { set: ["Revenue [m$]"] },
        label: { set: ["Revenue [m$]"] },
        color: { set: ["Format"] },
      },
      sort: "byValue",
    };

    const style = {
      fontSize: 12.5,
      title: { fontWeight: 200 },
      plot: {
        paddingLeft: 100,
        paddingTop: 25,
        yAxis: {
          color: "#ffffff00",
          label: { paddingRight: 10 },
        },
        xAxis: {
          title: { color: "#ffffff00" },
          label: { color: "#ffffff00", numberFormat: "grouped" },
        },
        marker: {
          colorPalette:
            "#b74c20FF #c47f58FF #1c9761FF #ea4549FF #875792FF #3562b6FF #ee7c34FF #efae3aFF",
        },
      },
    };

    const anims = [];

    anims.push((chart) => {
      return chart.animate({
        style,
      });
    });

    for (let i = 1973; i < 2021; i++) {
      const tmp = Object.assign({}, config);
      tmp.title = `Music Revenue by Format - Year by Year ${i}`;
      anims.push((chart) => {
        return chart.animate(
          {
            data: {
              filter: (record) => {
                return parseInt(record.Year) === i;
              },
            },
            config: tmp,
          },
          {
            duration: 0.2,
            x: { easing: "linear", delay: 0 },
            y: { delay: 0 },
            show: { delay: 0 },
            hide: { delay: 0 },
            title: { duration: 0, delay: 0 },
          }
        );
      });
    }

    anims.push((chart) => {
      return chart.animate(
        {
          config: {
            channels: { x: { attach: ["Year"] }, label: { set: null } },
          },
        },
        {
          duration: 0.3,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          data: {
            filter: (record) => {
              return record.Year === "2020" || record.Year === "1972";
            },
          },
          config: { title: "Lets see the total of the last 47 years" },
        },
        {
          duration: 2,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: { sort: "none" },
        },
        {
          delay: 0,
          duration: 2,
        }
      );
    });

    for (let i = 1973; i < 2020; i++) {
      anims.push((chart) => {
        return chart.animate(
          {
            data: {
              filter: (record) => {
                return parseInt(record.Year) >= i || record.Year === "1972";
              },
            },
            config: { split: true },
            style: { "plot.xAxis.interlacing.color": "#ffffff" },
          },
          {
            duration: 0.005,
          }
        );
      });
    }

    anims.push((chart) => {
      return chart.animate(
        {
          data: {
            filter: (record) => {
              return record.Year !== "1972";
            },
          },
          config: { split: false },
        },
        {
          duration: 1.5,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: { channels: { x: { detach: ["Year"] } } },
        },
        {
          duration: 0,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: { channels: { label: { set: ["Revenue [m$]"] } } },
        },
        {
          duration: 0.1,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: {
            channels: {
              x: { attach: ["Year"] },
              label: { detach: ["Revenue [m$]"] },
            },
          },
        },
        {
          duration: 1,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: {
            channels: {
              x: { set: ["Year"] },
              y: {
                set: ["Revenue [m$]", "Format"],
                range: { min: null, max: null },
              },
              color: { set: ["Format"] },
            },
            title: "Music Revenue by Format in the USA 1973 - 2020",
            split: true,
          },
          style: {
            plot: {
              paddingLeft: 7.5,
              paddingTop: 25,
              xAxis: {
                label: { fontSize: 9, angle: 2.0, color: "#8e8e8e" },
              },
              yAxis: {
                interlacing: { color: "#ffffff00" },
                title: { color: "#ffffff00" },
                label: { color: "#ffffff00" },
              },
            },
          },
        },
        {
          duration: 2,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: {
            geometry: "area",
          },
        },
        {
          duration: 1,
        }
      );
    });

    anims.push((chart) => {
      return chart.animate(
        {
          config: {
            channels: {
              x: { set: ["Year"] },
              y: { range: { max: "110%" } },
            },
            align: "center",
            split: false,
          },
          style: {
            "plot.marker.borderWidth": 1,
          },
        },
        {
          duration: 1,
        }
      );
    });

    mdchart.create([
      {
        anims,
      },
    ]);
  });
});
