vizzuLoaded = import("https://cdn.jsdelivr.net/npm/vizzu@0.6/dist/vizzu.min.js");

vizzuLoaded.then(Vizzu =>{

    data = {
        series: [
            { name: "Genres", type: "dimension" },
            { name: "Kinds", type: "dimension" },
            { name: "Popularity", type: "measure" }
        ],
        records: [
            ["Pop", "Hard", 114],
            ["Rock", "Hard", 96],
            ["Jazz", "Hard", 78],
            ["Metal", "Hard", 52],
            ["Pop", "Smooth", 56],
            ["Rock", "Smooth", 36],
            ["Jazz", "Smooth", 174],
            ["Metal", "Smooth", 121],
            ["Pop", "Experimental", 127],
            ["Rock", "Experimental", 83],
            ["Jazz", "Experimental", 94],
            ["Metal", "Experimental", 58],
        ]
    };

    chart1 = new Vizzu.default("tutorial_01_03_01").initializing;
    chart1 = chart1.then(chart => {
        return chart.animate({ data }, 0);
    });
    chart1 = chart1.then(chart => {
        snapshot1 = chart.store()
        return chart;
    });
    button1 = document.getElementById("tutorial_01_03_01_replay");
    button1.onclick = () => {
        chart1 = chart1.then(chart => {
            chart.animate(snapshot1, 0);
            return chart.animate({
                config: {
                    channels: {
                        y: { set: ["Popularity"] },
                        x: { set: ["Genres"] }
                    }
                }
            });
        });
    };
    button1.click();

    chart2 = new Vizzu.default("tutorial_01_03_02").initializing;
    chart2 = chart2.then(chart => {
        return chart.animate({ data }, 0);
    });
    chart2 = Promise.all([chart1, chart2]).then((charts) => {
        config = charts[0].config;
        style = charts[0].style;
        // return charts[1].animate({config: charts[0].config, style: charts[0].style}, 0);
        return charts[1].animate({style: charts[0].style}, 0);
    });
    chart2 = chart2.then(chart => {
        snapshot2 = chart.store()
        return chart;
    });
    button2 = document.getElementById("tutorial_01_03_02_replay");
    button2.onclick = () => {
        chart2 = chart2.then(chart => {
            chart.animate(snapshot2, 0);
            return chart.animate({
                config: {
                    channels: {
                            x: { set: null },
                            y: { set: ["Genres", "Popularity"] }
                    }
                }
            });
        });
    };
    button2.click();

    chart3 = new Vizzu.default("tutorial_01_03_03").initializing;
    chart3 = chart3.then(chart => {
        return chart.animate({ data }, 0);
    });
    chart3 = Promise.all([chart2, chart3]).then((charts) => {
        config = charts[0].config;
        style = charts[0].style;
        // return charts[1].animate({config: charts[0].config, style: charts[0].style}, 0);
        return charts[1].animate({style: charts[0].style}, 0);
    });
    chart3 = chart3.then(chart => {
        snapshot3 = chart.store()
        return chart;
    });
    button3 = document.getElementById("tutorial_01_03_03_replay");
    button3.onclick = () => {
        chart3 = chart3.then(chart => {
            chart.animate(snapshot3, 0);
            return chart.animate({
                config: {
                    channels: {
                        y: { detach: ["Popularity"] },
                        x: { attach: ["Popularity"] }
                    }
                }
            });
        });
        chart3 = chart3.then(chart => {
            console.log(chart.config)
            return chart;
        });
    };
    button3.click();

    chart4 = new Vizzu.default("tutorial_01_03_04").initializing;
    chart4 = chart4.then(chart => {
        return chart.animate({ data }, 0);
    });
    chart4 = Promise.all([chart3, chart4]).then((charts) => {
        config = charts[0].config;
        style = charts[0].style;
        // return charts[1].animate({config: charts[0].config, style: charts[0].style}, 0);
        return charts[1].animate({style: charts[0].style}, 0);
    });
    chart4 = chart4.then(chart => {
        snapshot4 = chart.store()
        return chart;
    });
    button4 = document.getElementById("tutorial_01_03_04_replay");
    button4.onclick = () => {
        chart4 = chart4.then(chart => {
            chart.animate(snapshot4, 0);
            return chart.animate({ title: "My first chart" });
        });
    };
    button4.click();

    chart5 = new Vizzu.default("tutorial_01_03_05").initializing;
    chart5 = chart4.then(chart => {
        return chart.animate({ data }, 0);
    });
    chart5 = Promise.all([chart4, chart5]).then((charts) => {
        config = charts[0].config;
        style = charts[0].style;
        // return charts[1].animate({config: charts[0].config, style: charts[0].style}, 0);
        return charts[1].animate({style: charts[0].style}, 0);
    });
    chart5 = chart5.then(chart => {
        snapshot5 = chart.store()
        return chart;
    });
    button5 = document.getElementById("tutorial_01_03_05_replay");
    button5.onclick = () => {
        chart5 = chart5.then(chart => {
            chart.animate(snapshot5, 0);
            chart.feature("tooltip", true);
            return chart;
        });
    };
    button5.click();
});