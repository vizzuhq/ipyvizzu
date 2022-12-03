class Tutorial {

    constructor(tutorial, data, vizzu) {
        this.tutorial = tutorial;
        this.dataLoaded = import(data).then(data => {
            return data.default
        });
        this.vizzuLoaded = import(vizzu).then(vizzuUrl => {
            return import(vizzuUrl.default);
        });        
    }

    animate(number, anims, prevChart) {
        let chart = this.vizzuLoaded.then(Vizzu => {
            return new Vizzu.default(this.tutorial + "_" + number).initializing;
        });

        let btn = document.createElement("button");
        btn.innerHTML = "Replay";
        chart = chart.then(chart => {
            document.getElementById(this.tutorial + "_" + number).appendChild(btn);
            return chart;
        });

        chart = Promise.all([chart, this.dataLoaded]).then(results => {
            let chart = results[0];
            let data = results[1];
            return chart.animate({ data }, 0);
        });
        if (prevChart) {
            chart = Promise.all([chart, prevChart]).then((results) => {
                let chart = results[0];
                let prevChart = results[1];
                // return chart.animate({config: prevChart.config, style: prevChart.style}, 0);
                return chart.animate({style: prevChart.style}, 0);
            });
        }
        let snapshot;
        chart = chart.then(chart => {
            snapshot = chart.store()
            return chart;
        });

        btn.onclick = () => {
            chart = chart.then(chart => {
                chart.animate(snapshot, 0);
                for (var i=0; i < anims.length; i++) {
                    chart = anims[i](chart);
                }
                return chart;
            });
        };
        btn.click();

        return chart;
    }

}

export default Tutorial;