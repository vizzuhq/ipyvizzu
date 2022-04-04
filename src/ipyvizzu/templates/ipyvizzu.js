class IpyVizzu 
{
    constructor(element, chartId, vizzulib, divWidth, divHeight)
    {
        this.inhibitScroll = false;
        document.addEventListener('wheel', function (evt) { this.inhibitScroll = true }, true);
        document.addEventListener('keydown', function (evt) { this.inhibitScroll = true }, true);
        document.addEventListener('touchstart', function (evt) { this.inhibitScroll = true }, true);

        this.elements = {};
        this.elements[chartId] = document.createElement("div");
        this.elements[chartId].style.cssText = `width: ${divWidth}; height: ${divHeight};`;

        this.charts = {};
        this.charts[chartId] = import(vizzulib).then(Vizzu => new Vizzu.default(this.elements[chartId]).initializing);
        this._moveHere(chartId, element);

        this.snapshots = {};
        this.displays = {};
    }

    static clearInhibitScroll()
    {
        this.inhibitScroll = false;
    }

    animate(element, chartId, displayTarget, scrollEnabled, chartTarget, chartAnimOpts)
    {
        if (displayTarget === 'end') this._moveHere(chartId, element);
        this.charts[chartId] = this.charts[chartId].then(chart => {
            if (displayTarget === 'actual') this._moveHere(chartId, element);
            this._scroll(chartId, scrollEnabled);
            return chart.animate(chartTarget, chartAnimOpts);
        });
    }

    store(chartId, id)
    {
        this.charts[chartId] = this.charts[chartId].then(chart => {
            this.snapshots[id] = chart.store();
            return chart;
        });
    }

    stored(id)
    {
        return this.snapshots[id];
    }

    feature(chartId, name, enabled)
    {
        this.charts[chartId] = this.charts[chartId].then(chart => {
            chart.feature(name, enabled);
            return chart;
        });
    }

    _moveHere(chartId, element)
    {
        element.append(this.elements[chartId]);
    }

    _scroll(chartId, enabled)
    {
        if (!this.inhibitScroll && enabled) {
            this.elements[chartId].scrollIntoView({ behavior: "auto", block: "center" });
        }
    }
}

window.IpyVizzu = IpyVizzu;