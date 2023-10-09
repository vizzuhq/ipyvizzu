class PresetsMock {
  constructor() {
    return new Proxy(this, {
      get: (target, prop) => {
        return function (obj) {
          return `Config.${prop}(${JSON.stringify(obj, null, 2)})`
        }
      }
    })
  }
}

class VizzuMock {
  constructor(title, description, data, assetsPath, dataFileName, dataName) {
    this.description = ''
    if (description) {
      this.description = description
    }
    this.data = data
    if (dataName !== 'data') {
      dataFileName = dataFileName + '_' + dataName
    }

    this.code = `---
csv_url: ${assetsPath}/assets/data/${dataFileName}.csv
---

# ${title}

<div id="example_01"></div>

??? info "Info - How to setup Chart"
    \`\`\`python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style

    df = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/latest/assets/data/${dataFileName}.csv",
        dtype={"Year": str, "Timeseries": str},
    )
    data = Data()
    data.add_df(df)

    chart = Chart()
    chart.animate(data)
    \`\`\`

${this.description}

\`\`\`python
`

    this.end = `
\`\`\`

<script src="./main.js"></script>
`
  }

  animate(chart, animOptions) {
    const params = []

    if (chart.data && chart.data.filter) {
      if (JSON.stringify(chart.data) !== JSON.stringify(this.data)) {
        const fnCode = chart.data.filter.toString().replace(/\s*record\s*=>\s*/, '')
        params.push(`data.filter("""\n${fnCode.replace(/^\s*/gm, '')}\n""")`)
      }
    }
    if (chart.config) {
      if (typeof chart.config === 'string' && chart.config.startsWith('Config.')) {
        params.push(chart.config)
      } else {
        params.push('Config(' + JSON.stringify(chart.config, null, 2) + ')')
      }
    }
    if (chart.style) {
      params.push('Style(' + JSON.stringify(chart.style, null, 2) + ')')
    }
    if (animOptions) {
      if (typeof animOptions === 'object') {
        for (const key in animOptions) {
          params.push(`${key} = ${JSON.stringify(animOptions[key])}`)
        }
      } else {
        params.push(`duration = "${animOptions}"`)
      }
    }

    const args = params.join(',\n')
    const callCode = `chart.animate(\n${args}`
    const fullCode = callCode.replace(/\n/g, '\n  ') + '\n)\n\n'
    this.code += fullCode
  }

  feature(name, enabled) {
    this.code += `chart.feature("${name}", ${enabled})\n\n`
  }

  on(eventName, handler) {
    const entire = handler.toString()
    const body = entire.slice(entire.indexOf('{') + 1, entire.lastIndexOf('}'))
    this.code += `method = """${body}"""\n`
    this.code += `handler = chart.on("${eventName}", method)\n\n`
  }

  static get presets() {
    return new PresetsMock()
  }

  getCode() {
    return (
      this.code
        .replace(/\bnull\b/g, 'None')
        .replace(/\btrue\b/g, 'True')
        .replace(/\bfalse\b/g, 'False') + this.end
    )
  }
}

const inputFileName = process.argv[2]
const dataFilePath = process.argv[3]
const assetsPath = process.argv[4]
const dataFileName = process.argv[5]
const dataName = process.argv[6]
let title = process.argv[7]
const inputFileLoaded = import(inputFileName)
const dataFileLoaded = import(dataFilePath + '/' + dataFileName + '.mjs')
Promise.all([inputFileLoaded, dataFileLoaded]).then((results) => {
  const module = results[0]
  const description = module.description
  if (module.title) {
    title = module.title
  }
  const data = results[1][dataName]
  const chart = new VizzuMock(title, description, data, assetsPath, dataFileName, dataName)
  for (const testStep of module.default) {
    testStep(chart)
  }
  console.log(chart.getCode())
})
