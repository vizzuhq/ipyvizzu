
class MdChart {

    constructor(data, vizzu, id) {
        this.dataLoaded = import(data).then(data => {
            return data.default
        });
        this.vizzuLoaded = import(vizzu).then(vizzuUrl => {
            return import(vizzuUrl.default);
        });
        this.id = id;
    }

    create(snippets) {
        let chart = Promise.resolve();
        for (var i=0; i < snippets.length; i++) {
            let number = i + 1;
            chart = this.animate(("0" + number).slice(-2), snippets[i], chart);
        }
    }

    animate(number, snippet, prevChart) {

        let div = document.getElementById(this.id + "_" + number);
        div.classList.add("loading");

        let snapshot;

        let chart = Promise.all([this.vizzuLoaded, this.dataLoaded]).then(results => {
            let Vizzu = results[0];
            let data = results[1];
            return new Vizzu.default(div, { data }).initializing;
        });
        
        chart = Promise.all([chart, prevChart]).then((results) => {
            let chart = results[0];
            let prevChart = results[1];
            div.classList.remove("loading");
            div.classList.add("replay");
            if (prevChart) {
                return chart.animate({config: prevChart.config, style: prevChart.style}, 0);
            } else {
                return chart;
            }
        });
        
        chart = chart.then(chart => {
            snapshot = chart.store()
            return chart;
        });

        div.onclick = () => {
            chart = chart.then(chart => {
                chart.animate(snapshot, 0);
                for (var i=0; i < snippet.anims.length; i++) {
                    chart = snippet.anims[i](chart);
                }
                return chart;
            });
        };
        div.click();

        return chart;
    }

}

export default MdChart;