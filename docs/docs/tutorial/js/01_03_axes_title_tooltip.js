import("./tutorial.js").then(Tutorial => {
    let tutorial = new Tutorial.default(
        "./data.js",
        "./vizzu.js",
    )

    tutorial.create(
        [
            [
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
            ],
            [
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
            ],
            [
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
            ],
            [
                chart => {
                    console.log(chart.config);
                    return chart;
                },
                chart => {
                    return chart.animate({ title: "My first chart" });
                }
            ],
            [
                chart => {
                    chart.feature("tooltip", true);
                    return chart;
                }
            ]
        ]
    );
});

