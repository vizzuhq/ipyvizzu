const csv2JsLoaded = import('../../assets/javascripts/csv2js.js')
const vizzuLoaded = import('../../assets/javascripts/vizzu.js').then(
  (vizzuUrl) => {
    return import(vizzuUrl.default)
  }
)

Promise.all([csv2JsLoaded, vizzuLoaded]).then((results) => {
  const Csv2Js = results[0].default
  const Vizzu = results[1].default

  const dataLoaded = Csv2Js.csv('./musicformats.csv', ['Year'])

  dataLoaded.then((data) => {
    new Vizzu('testVizzuCanvas', { data }).initializing.then((chart) => {
      const config = {
        channels: {
          y: {
            set: ['Format']
          },
          x: { set: ['Revenue [m$]'] },
          label: { set: ['Revenue [m$]'] },
          color: { set: ['Format'] }
        },
        sort: 'byValue',
        title: 'Music Revenue by Format - Year by Year 1973'
      }

      const style = {
        plot: {
          paddingLeft: 100,
          paddingTop: 25,
          yAxis: {
            color: '#ffffff00',
            label: { paddingRight: 10 }
          },
          xAxis: {
            title: { color: '#ffffff00' },
            label: { color: '#ffffff00', numberFormat: 'grouped' }
          },
          marker: {
            colorPalette:
              '#b74c20FF #c47f58FF #1c9761FF #ea4549FF #875792FF #3562b6FF #ee7c34FF #efae3aFF'
          }
        }
      }

      chart.animate({
        data: {
          filter: (record) => {
            return parseInt(record.Year) === 1973
          }
        },
        config,
        style
      })

      for (let i = 1974; i < 2021; i++) {
        const title = `Music Revenue by Format - Year by Year ${i}`
        chart.animate(
          {
            data: {
              filter: (record) => {
                return parseInt(record.Year) === i
              }
            },
            config: { title }
          },
          {
            duration: 0.2,
            x: { easing: 'linear', delay: 0 },
            y: { delay: 0 },
            show: { delay: 0 },
            hide: { delay: 0 },
            title: { duration: 0, delay: 0 }
          }
        )
      }

      chart.animate(
        {
          config: {
            channels: { x: { attach: ['Year'] }, label: { set: null } }
          }
        },
        {
          duration: 0.3
        }
      )

      chart.animate(
        {
          data: {
            filter: (record) => {
              return record.Year === '2020' || record.Year === '1972'
            }
          },
          config: { title: 'Lets see the total of the last 47 years' }
        },
        {
          duration: 2
        }
      )

      chart.animate(
        {
          config: { sort: 'none' }
        },
        {
          delay: 0,
          duration: 2
        }
      )

      for (let i = 2019; i > 1972; i--) {
        chart.animate(
          {
            data: {
              filter: (record) => {
                return parseInt(record.Year) >= i || record.Year === '1972'
              }
            },
            config: { split: true },
            style: { 'plot.xAxis.interlacing.color': '#ffffff' }
          },
          {
            duration: 0.005
          }
        )
      }

      chart.animate(
        {
          data: {
            filter: (record) => {
              return record.Year !== '1972'
            }
          },
          config: { split: false }
        },
        {
          duration: 1.5
        }
      )

      chart.animate(
        {
          config: { channels: { x: { detach: ['Year'] } } }
        },
        {
          duration: 0
        }
      )

      chart.animate(
        {
          config: { channels: { label: { set: ['Revenue [m$]'] } } }
        },
        {
          duration: 0.1
        }
      )

      chart.animate(
        {
          config: {
            channels: {
              x: { attach: ['Year'] },
              label: { detach: ['Revenue [m$]'] }
            }
          }
        },
        {
          duration: 1
        }
      )

      chart.animate(
        {
          config: {
            channels: {
              x: { set: ['Year'] },
              y: {
                set: ['Revenue [m$]', 'Format'],
                range: { min: null, max: null }
              },
              color: { set: ['Format'] }
            },
            title: 'Music Revenue by Format in the USA 1973 - 2020',
            split: true
          },
          style: {
            plot: {
              paddingLeft: 7.5,
              paddingTop: 25,
              xAxis: {
                label: { fontSize: 9, angle: 2.0, color: '#8e8e8e' }
              },
              yAxis: {
                interlacing: { color: '#ffffff00' },
                title: { color: '#ffffff00' },
                label: { color: '#ffffff00' }
              }
            }
          }
        },
        {
          duration: 2
        }
      )

      chart.animate(
        {
          config: {
            geometry: 'area'
          }
        },
        {
          duration: 1
        }
      )

      chart.animate(
        {
          config: {
            channels: {
              x: { set: ['Year'] },
              y: { range: { max: '110%' } }
            },
            align: 'center',
            split: false
          },
          style: {
            'plot.marker.borderWidth': 1
          }
        },
        {
          duration: 1
        }
      )
    })
  })
})
