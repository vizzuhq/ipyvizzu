window.IpyVizzu = class 
{
    constructor(id, chartId, vizzulib, divWidth, divHeight)
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
        this._getElement(id).parentNode.insertBefore(this.elements[chartId], this._getElement(id));

        this.snapshots = {};
        this.displays = {};
    }

    static clearInhibitScroll()
    {
        this.inhibitScroll = false;
    }

    animate(displayTarget, id, chartId, scrollEnabled, chartTarget, chartAnimOpts)
    {
        if (displayTarget !== 'begin') {
            this.displays[id] = this._getElement(id).parentNode.parentNode.style.display;
        }
        this._getElement(id).parentNode.parentNode.style.display = "none";
        if (displayTarget !== 'end') this._move(id, chartId);
        this.charts[chartId] = this.charts[chartId].then(chart => {
            if (displayTarget !== 'actual') this._move(id, chartId);
            this._scroll(chartId, scrollEnabled);
            chart.animate(chartTarget, chartAnimOpts);
            return chart;
        });
    }

    store(id, chartId)
    {
        this._getElement(id).parentNode.parentNode.style.display = "none";
        this.charts[chartId] = this.charts[chartId].then(chart => {
            this.snapshots[id] = chart.store();
            return chart;
        });
    }

    stored(id)
    {
        return this.snapshots[id];
    }

    feature(id, chartId, name, enabled)
    {
        this._getElement(id).parentNode.parentNode.style.display = "none";
        this.charts[chartId] = this.charts[chartId].then(chart => {
            chart.feature(name, enabled);
            return chart;
        });
    }

    _getElement(id)
    {
        return document.getElementById(`vizzu_${id}`);
    }

    _move(id, chartId)
    {
        if (this.elements[chartId].parentNode && this.elements[chartId].parentNode.parentNode) {
            this.elements[chartId].parentNode.parentNode.style.display = "none";
        }
        this._getElement(id).parentNode.parentNode.style.display = this.displays[id];
        this._getElement(id).parentNode.insertBefore(this.elements[chartId], this._getElement(id));
    }

    _scroll(chartId, enabled)
    {
        if (!this.inhibitScroll && enabled) {
            this.elements[chartId].scrollIntoView({ behavior: "auto", block: "center" });
        }
    }
}