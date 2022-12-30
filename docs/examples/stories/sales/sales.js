const csv2JsLoaded = import("../../../javascripts/csv2js.js");
const mdChartLoaded = import("../../../javascripts/mdchart.js");

Promise.all([csv2JsLoaded, mdChartLoaded]).then((results) => {
  const Csv2Js = results[0].default;
  const MdChart = results[1].default;

  const csv2js = new Csv2Js(["tenure"]);
  const dataLoaded = csv2js.getData("./sales.csv");

  dataLoaded.then((data) => {
    const mdchart = new MdChart(data, "./vizzu.js", "example");

    mdchart.create([
      {
        anims: [
          (chart) => {
            return chart.animate({
              data: {
                filter: (record) => {
                  return record.Product === "Shoes";
                },
              },
              config: {
                x: "Region",
                y: ["Sales", "Product"],
                label: "Sales",
                color: "Product",
                title: "Sales of Shoes",
              },
            });
          },
          (chart) => {
            return chart.animate(
              {
                data: {
                  filter: (record) => {
                    return (
                      record.Product === "Shoes" ||
                      record.Product === "Handbags"
                    );
                  },
                },
                config: { title: "Sales of Shoes & Handbags" },
              },
              { delay: 1 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                data: {
                  filter: (record) => {
                    return record.Product !== "Accessories";
                  },
                },
                config: { title: "Sales of Shoes, Handbags & Gloves" },
              },
              { delay: 1 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                data: { filter: null },
                config: { title: "Sales of All Products" },
              },
              { delay: 1 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: {
                  y: ["Revenue [$]", "Product"],
                  label: "Revenue [$]",
                  title: "Revenue of All Products",
                },
              },
              { delay: 1 }
            );
          },
          (chart) => {
            return chart.animate(
              {
                config: { x: ["Region", "Revenue [$]"], y: "Product" },
              },
              { delay: 2 }
            );
          },
          (chart) => {
            return chart.animate({
              config: { x: "Revenue [$]", y: "Product" },
            });
          },
          (chart) => {
            return chart.animate(
              {
                config: { coordSystem: "polar", sort: "byValue" },
              },
              { delay: 1 }
            );
          },
        ],
      },
    ]);
  });
});
