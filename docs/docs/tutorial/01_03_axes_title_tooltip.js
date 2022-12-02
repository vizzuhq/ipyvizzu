vizzuLoaded = import("https://cdn.jsdelivr.net/npm/vizzu@0.6/dist/vizzu.min.js");


class Snippet {

    static display(vizzu, data, tutorial, number, anims, prev) {
        let chart = new vizzu.default(tutorial + "_" + number).initializing;
        chart = chart.then(chart => {
            return chart.animate({ data }, 0);
        });

        if (prev) {
            chart = Promise.all([chart, prev]).then((charts) => {
                // return charts[0].animate({config: charts[1].config, style: charts[1].style}, 0);
                return charts[0].animate({style: charts[1].style}, 0);
            });
        }
        let snapshot;
        chart = chart.then(chart => {
            snapshot = chart.store()
            return chart;
        });

        let button = document.getElementById(tutorial + "_" + number + "_" + "replay");
        button.onclick = () => {
            chart = chart.then(chart => {
                chart.animate(snapshot, 0);
                for (var i=0; i < anims.length; i++) {
                    chart = anims[i](chart);
                }
                return chart;
            });
        };
        button.click();

        return chart;
    }

}


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

    let chart1 = Snippet.display(Vizzu, data, "tutorial_01_03", "01", [
        chart => {
            return chart.animate({
                config: {
                    channels: {
                        y: { set: ["Popularity"] },
                        x: { set: ["Genres"] }
                    }
                }
            });
        }
    ])

    let chart2 = Snippet.display(Vizzu, data, "tutorial_01_03", "02", [
        chart => {
            return chart.animate({
                config: {
                    channels: {
                            x: { set: null },
                            y: { set: ["Genres", "Popularity"] }
                    }
                }
            });
        }
    ], chart1)

    let chart3 = Snippet.display(Vizzu, data, "tutorial_01_03", "03", [
        chart => {
            return chart.animate({
                config: {
                    channels: {
                        y: { detach: ["Popularity"] },
                        x: { attach: ["Popularity"] }
                    }
                }
            });
        }
    ], chart2)

    let chart4 = Snippet.display(Vizzu, data, "tutorial_01_03", "04", [
        chart => {
            return chart.animate({ title: "My first chart" });
        }
    ], chart3)

    let chart5 = Snippet.display(Vizzu, data, "tutorial_01_03", "05", [
        chart => {
            chart.feature("tooltip", true);
            return chart;
        }
    ], chart4)
});