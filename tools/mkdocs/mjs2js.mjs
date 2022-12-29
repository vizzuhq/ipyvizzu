const inputFileName = process.argv[2];
const dataFileName = process.argv[3];

import(inputFileName).then((module) => {
  const test = `
const dataLoaded = import("../../data/${dataFileName}.js");
const mdChartLoaded = import("../../javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        ${module.default}
      ]
    }
  ]);
});
`;
  console.log(test);
});
