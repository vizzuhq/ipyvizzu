class Csv2Js {
  constructor() {
    this.data = { series: [], records: [] };
  }

  receiveLine(results) {
    const keys = Object.keys(results.data);

    if (this.data.series.length === 0) {
      for (const key of keys) {
        this.data.series.push({
          name: key,
          type: key === "Year" ? "dimension" : "measure",
        });
      }
    } else {
      this.data.records.push(Object.values(results.data));

      for (let i = 0; i < this.data.series.length; i++) {
        const key = this.data.series[i].name;
        if (typeof results.data[key] !== "number")
          this.data.series[i].type = "dimension";
      }
    }
  }

  getData(csv) {
    const data = this.data;
    const stepCallback = this.receiveLine;
    const bindedStepCallback = stepCallback.bind(this);
    return new Promise(function (resolve, reject) {
      // eslint-disable-next-line no-undef
      Papa.parse(csv, {
        download: true,
        header: true,
        dynamicTyping: true,
        quoteChar: '"',
        skipEmptyLines: true,
        step: bindedStepCallback,
        complete: () => {
          resolve(data);
        },
        error: reject,
      });
    });
  }
}

export default Csv2Js;
