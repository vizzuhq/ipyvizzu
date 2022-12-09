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

    return this.dataLoaded.then((data) => {
      let chart = this.vizzuLoaded.then((Vizzu) => {
        const VizzuConstructor = Vizzu.default;
        return new VizzuConstructor(div).initializing;
      });

      chart = Promise.all([chart, prevChart]).then((results) => {
        const chart = results[0];
        const prevChart = results[1];
        div.classList.remove("loading");
        div.classList.add("playing");
        const animTarget = {};
        animTarget.data = Object.assign({}, data);
        if (prevChart) {
          animTarget.config = Object.assign({}, prevChart.config);
          animTarget.style = Object.assign({}, prevChart.style);
        }
        // remove if it can be found in the prevChart
        if (snippet.initDataFilter) {
          animTarget.data.filter = snippet.initDataFilter;
        }
        return chart.animate(animTarget, 0);
      });

      let clicked = false;
      div.onclick = () => {
        if (!clicked) {
          clicked = true;
          chart = Promise.all([chart, prevChart]).then((results) => {
            const chart = results[0];
            const prevChart = results[1];
            const animTarget = {};
            animTarget.data = Object.assign({}, data);
            if (prevChart) {
              animTarget.config = Object.assign({}, prevChart.config);
              animTarget.style = Object.assign({}, prevChart.style);
            }
            // remove if it can be found in the prevChart
            if (snippet.initDataFilter) {
              animTarget.data.filter = snippet.initDataFilter;
            }
            return chart.animate(animTarget, 0);
          });

          div.classList.remove("replay");
          div.classList.add("playing");
          for (let i = 0; i < snippet.anims.length; i++) {
            chart = chart.then((chart) => {
              return snippet.anims[i](chart);
            });
          }

          chart.then(() => {
            div.classList.remove("playing");
            div.classList.add("replay");
            clicked = false;
          });

          return chart;
        }
      };
      div.click();

      return chart;
    });
  }
}

export default MdChart;
