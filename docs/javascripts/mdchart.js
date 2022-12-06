class MdChart {
  constructor(data, vizzu, id) {
    this.dataLoaded = import(data).then((data) => {
      return data.default;
    });
    this.vizzuLoaded = import(vizzu).then((vizzuUrl) => {
      return import(vizzuUrl.default);
    });
    this.id = id;
  }

  create(snippets) {
    let chart = Promise.resolve();
    for (let i = 0; i < snippets.length; i++) {
      const number = i + 1;
      chart = this.animate(("0" + number).slice(-2), snippets[i], chart);
    }
  }

  animate(number, snippet, prevChart) {
    const div = document.getElementById(this.id + "_" + number);
    div.classList.add("loading");

    let snapshot;

    let chart = Promise.all([this.vizzuLoaded, this.dataLoaded]).then(
      (results) => {
        const Vizzu = results[0];
        const data = results[1];
        const VizzuConstructor = Vizzu.default;
        return new VizzuConstructor(div, { data }).initializing;
      }
    );

    chart = Promise.all([chart, prevChart]).then((results) => {
      const chart = results[0];
      const prevChart = results[1];
      div.classList.remove("loading");
      div.classList.add("replay");
      if (prevChart) {
        return chart.animate(
          { config: prevChart.config, style: prevChart.style },
          0
        );
      } else {
        return chart;
      }
    });

    chart = chart.then((chart) => {
      snapshot = chart.store();
      return chart;
    });

    div.onclick = () => {
      chart = chart.then((chart) => {
        chart = chart.animate(snapshot, 0);
        for (let i = 0; i < snippet.anims.length; i++) {
          chart = chart.then((chart) => {
            return snippet.anims[i](chart);
          });
        }
        return chart;
      });
    };
    div.click();

    return chart;
  }
}

export default MdChart;
