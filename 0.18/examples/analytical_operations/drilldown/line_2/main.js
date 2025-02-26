
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data_6 = results[0].data_6;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data_6, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
		chart.animate({
			data: data_6,
			config: {
				channels: {
					x: 'Year',
					y: 'Value 3 (+)'
				},

				geometry: 'line'
			}
		}),(chart) =>
		chart.animate({
			config: {
				channels: {
					y: ['Country', 'Value 3 (+)'],
					color: 'Country'
				},

				geometry: 'area'
			}
		})
      ]
    }
  ]);
});

