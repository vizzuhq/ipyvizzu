import fs from 'fs';

class VizzuMock 
{
	constructor(datafilename) 
	{
		this.cellcnt = 0;

		this.firstcell = `
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

data_frame = pd.read_csv('../../data/${datafilename}.csv', dtype={"Year": str})
data = Data()
data.add_data_frame(data_frame)

chart = Chart()
chart.animate(data)

`
		;

		this.code = `---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: .venv
  language: python
  name: .venv
---
`
		;
	}

	animate(chart, animOptions) 
	{
		let params = [];

		if (chart.data && chart.data.filter)
		{
			let fnCode = chart.data.filter.toString().replace(/\s*record\s*=>\s*/, '');
			params.push(`data.filter("""\n${fnCode.replace(/^\s*/gm,"")}\n""")`);
		}
		if (chart.config)
		{
			params.push("Config(" + JSON.stringify(chart.config, null, 2) + ")");
		}
		if (chart.style)
		{
			params.push("Style(" + JSON.stringify(chart.style, null, 2) + ")");
		}
		if (animOptions)
		{
			if (typeof animOptions === 'object')
			{
				for (let key in animOptions)
				{
					params.push(`${key} = ${JSON.stringify(animOptions[key])}`);
				}
			}
			else
			{
				params.push(`duration = "${animOptions}"`);
			}
		}

		let args = params.join(',\n');
		let callCode = `chart.animate(\n${args}`;
		let fullCode = callCode.replace(/\n/g, '\n  ') + "\n)\n\n";

		if (this.cellcnt === 0)
		{
			fullCode = this.firstcell + fullCode;
		}
		this.cellcnt++;

		this.code +=  `

\`\`\`{code-cell}
${fullCode}
\`\`\`

`
		;
	}

	getCode()
	{
		return this.code
			.replace(/\bnull\b/g, 'None')
			.replace(/\btrue\b/g, 'True')
			.replace(/\bfalse\b/g, 'False');
	}
}

function getDataFilename(sourcefilename)
{
	let source = fs.readFileSync(sourcefilename, 'utf8');
	let datafilename = source.match(/test_data\/(\w*).mjs/)[1];
	return datafilename;
}

let inputFileName = process.argv[2];
let outputFileName = process.argv[3];

console.log(`[mjs2md] processing ${inputFileName}`);

let datafilename = getDataFilename(inputFileName);
console.log(`[mjs2md] data file detected: ${datafilename}`);

import("./"+inputFileName).then((module) => 
{
	const chart = new VizzuMock(datafilename);
	for (let testStep of module.default) {
		testStep(chart);
	}
	console.log(`[mjs2md] writing ${outputFileName}`);
	fs.writeFileSync(outputFileName, chart.getCode());
}); 
