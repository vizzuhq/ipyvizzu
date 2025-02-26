
const dataLoaded = import("../../../../assets/data/chart_types_eu.js");
const mdChartLoaded = import("../../../../assets/javascripts/mdchart.js");
  
Promise.all([dataLoaded, mdChartLoaded]).then((results) => {
  const data = results[0].data;
  const MdChart = results[1].default;
  const mdchart = new MdChart(data, "./vizzu.js", "example");

  mdchart.create([
    {
      anims: [
        (chart) =>
		chart.animate({
			data,

			config: {
				channels: {
					x: 'Year',
					y: ['Joy factors', 'Value 2 (+)'],
					color: 'Joy factors'
				}
			},
			style: {
				plot: {
					marker: {
						colorPalette: '#ef675aFF #6d8cccFF #e6cf99FF #9c50abFF'
					}
				}
			}
		}),(chart) =>
		chart.animate({
			config: {
				channels: {
					x: 'Value 2 (+)',
					y: ['Joy factors'],
					label: 'Value 2 (+)'
				}
			}
		})
      ]
    }
  ]);
});

