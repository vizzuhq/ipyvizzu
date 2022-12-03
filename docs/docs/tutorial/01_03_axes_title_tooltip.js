import("./js/tutorial.js").then(Tutorial => {
    let tutorial = new Tutorial.default(
        "tutorial_01_03",
        window.location.pathname.slice(0, window.location.pathname.lastIndexOf('/')) + "/js/data.js",
        window.location.pathname.slice(0, window.location.pathname.lastIndexOf('/')) + "/js/vizzu.js",
    )
    
    let chart1 = tutorial.animate("01", [
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
    
    let chart2 = tutorial.animate("02", [
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
    
    let chart3 = tutorial.animate("03", [
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
    
    let chart4 = tutorial.animate("04", [
        chart => {
            return chart.animate({ title: "My first chart" });
        }
    ], chart3)
    
    let chart5 = tutorial.animate("05", [
        chart => {
            chart.feature("tooltip", true);
            return chart;
        }
    ], chart4)    
});

