if (window.IpyVizzu?.version !== '__version__') {
  class IpyVizzu {
    static version = '__version__'
    static analytics = undefined
    static inhibitScroll = false

    constructor() {
      document.addEventListener(
        'wheel',
        (evt) => {
          IpyVizzu.inhibitScroll = true
        },
        true
      )
      document.addEventListener(
        'keydown',
        (evt) => {
          IpyVizzu.inhibitScroll = true
        },
        true
      )
      document.addEventListener(
        'touchstart',
        (evt) => {
          IpyVizzu.inhibitScroll = true
        },
        true
      )

      this.elements = {}
      this.charts = {}
      this.controls = {}

      this.storage = {}
      this.displays = {}

      this.events = {}
      this.loaded = {}
      this.libs = {}
    }

    static clearInhibitScroll(element) {
      IpyVizzu.inhibitScroll = false
    }

    createChart(element, chartId, vizzulib, divWidth, divHeight) {
      this.elements[chartId] = document.createElement('div')
      this.elements[chartId].style.cssText = `width: ${divWidth}; height: ${divHeight};`
      this.loaded[chartId] = import(vizzulib)
      this.charts[chartId] = this.loaded[chartId].then((Vizzu) => {
        this.libs[chartId] = Vizzu.default
        const VizzuConstructor = Vizzu.default
        return new VizzuConstructor(this.elements[chartId]).initializing
      })
      this._moveHere(chartId, element)
    }

    animate(element, chartId, animId, displayTarget, scrollEnabled, getChartTarget, chartAnimOpts) {
      if (displayTarget === 'end') this._moveHere(chartId, element)
      this.controls[chartId] = this.charts[chartId]
      this.charts[chartId] = this.charts[chartId].then((chart) => {
        if (displayTarget === 'actual') this._moveHere(chartId, element)
        this._scroll(chartId, scrollEnabled)
        let chartTarget = getChartTarget(this.libs[chartId])
        if (typeof chartTarget === 'string') {
          chartTarget = this.storage[chartTarget]
        } else if (Array.isArray(chartTarget)) {
          for (let i = 0; i < chartTarget.length; i++) {
            const target = chartTarget[i].target
            if (typeof target === 'string') {
              chartTarget[i].target = this.storage[target]
            }
          }
        }
        chart = chart.animate(chartTarget, chartAnimOpts)
        this.controls[animId] = chart
        return chart
      })
    }

    store(element, chartId, id) {
      this.charts[chartId] = this.charts[chartId].then((chart) => {
        this.storage[id] = chart.store()
        return chart
      })
    }

    feature(element, chartId, name, enabled) {
      this.charts[chartId] = this.charts[chartId].then((chart) => {
        chart.feature(name, enabled)
        return chart
      })
    }

    setEvent(element, chartId, id, event, handler) {
      this.charts[chartId] = this.charts[chartId].then((chart) => {
        this.events[id] = handler
        chart.on(event, this.events[id])
        return chart
      })
    }

    clearEvent(element, chartId, id, event) {
      this.charts[chartId] = this.charts[chartId].then((chart) => {
        chart.off(event, this.events[id])
        return chart
      })
    }

    log(element, chartId, chartProperty) {
      this.charts[chartId] = this.charts[chartId].then((chart) => {
        console.log(chart[chartProperty])
        return chart
      })
    }

    control(element, method, prevId, lastId, ...params) {
      this.controls[prevId].then(() => {
        this.controls[lastId].activated.then((control) => {
          if (method === 'seek') {
            const value = params[0]
            control[method](value)
            return
          }
          if (method === 'store') {
            const id = params[0]
            this.storage[id] = control[method]()
            return
          }
          control[method]()
        })
      })
    }

    _moveHere(chartId, element) {
      element.append(this.elements[chartId])
    }

    _scroll(chartId, enabled) {
      if (!IpyVizzu.inhibitScroll && enabled) {
        this.elements[chartId].scrollIntoView({
          behavior: 'auto',
          block: 'center'
        })
      }
    }

    static _hide(element) {
      document.getElementById(element.selector.substring(1)).parentNode.style.display = 'none'
    }

    static _display(prevElement, element) {
      if (prevElement.parentNode) {
        prevElement.parentNode.style.display = 'none'
      }
      document.getElementById(element.selector.substring(1)).parentNode.style.display = 'flex'
      document.getElementById(element.selector.substring(1)).parentNode.style.margin = 'auto'
    }

    static changeAnalyticsTo(analytics) {
      if (IpyVizzu.analytics !== analytics) {
        console.log('ipyvizzu gather usage stats:', analytics)
        IpyVizzu.analytics = analytics
      }
      if (analytics) {
        IpyVizzu._addHeadScript()
      } else {
        IpyVizzu._removeScript('ipyvizzu-analytics-head')
      }
    }

    static _addHeadScript() {
      const scriptId = 'ipyvizzu-analytics-head'
      if (!IpyVizzu._isScriptAppended(scriptId)) {
        const script = document.createElement('script')
        script.defer = true
        script.src = 'https://plausible.io/js/script.local.js'
        script.dataset.domain = 'usage.ipyvizzu.com'
        script.id = scriptId
        document.getElementsByTagName('head')[0].appendChild(script)
      }
    }

    static _isScriptAppended(id) {
      return document.querySelector(`script[id="${id}"]`) !== null
    }

    static _removeScript(id) {
      const script = document.getElementById(id)
      if (script) script.remove()
    }
  }

  window.IpyVizzu = IpyVizzu
  console.log(`ipyvizzu ${IpyVizzu.version}`)
  window.ipyvizzu = new window.IpyVizzu()
}
