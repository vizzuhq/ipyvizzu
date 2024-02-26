class Js2csv {
	constructor(data) {
		this.data = data
	}

	getHeaderLine() {
		const header = []
		for (const series in this.data.series) {
			header.push(this.data.series[series].name)
		}
		return header.join(',') + '\n'
	}

	getDataLine(i) {
		const line = []
		const record = {}
		for (const j in this.data.series) {
			let value = this.data.series[j].values[i]
			if (typeof value === 'string' && value.includes(',')) {
				value = `"${value}"`
			}
			record[this.data.series[j].name] = value
			line.push(value)
		}
		if (this.data.filter) {
			if (!this.data.filter(record)) {
				return ''
			}
		}
		return line.join(',') + '\n'
	}

	getRecordLine(i) {
		const line = []
		const record = {}
		for (const j in this.data.series) {
			let value = this.data.records[i][j]
			if (typeof value === 'string' && value.includes(',')) {
				value = `"${value}"`
			}
			record[this.data.series[j].name] = value
			line.push(value)
		}
		if (this.data.filter) {
			if (!this.data.filter(record)) {
				return ''
			}
		}
		return line.join(',') + '\n'
	}

	convert() {
		let csv = ''
		csv += this.getHeaderLine()
		if (this.data.series[0].values) {
			for (let i = 0; i < this.data.series[0].values.length; i++) {
				csv += this.getDataLine(i)
			}
		} else {
			for (let i = 0; i < this.data.records.length; i++) {
				csv += this.getRecordLine(i)
			}
		}
		return csv
	}
}

const inputFilename = process.argv[2]
const dataName = process.argv[3]

import(inputFilename).then((module) => {
	const js2csv = new Js2csv(module[dataName])
	console.log(js2csv.convert())
})
