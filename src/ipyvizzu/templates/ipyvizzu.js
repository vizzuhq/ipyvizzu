window.IpyVizzu = class 
{
    constructor(id, c_id, vizzulib, div_width, div_height)
    {
        this.inhibitScroll = false;
        document.addEventListener('wheel', function (evt) { this.inhibitScroll = true }, true);
        document.addEventListener('keydown', function (evt) { this.inhibitScroll = true }, true);
        document.addEventListener('touchstart', function (evt) { this.inhibitScroll = true }, true);

        this.elements = {};
        this.elements[c_id] = document.createElement("div");
        this.elements[c_id].style.cssText = `width: ${div_width}; height: ${div_height};`;

        this.charts = {};
        this.charts[c_id] = import(vizzulib).then(Vizzu => new Vizzu.default(this.elements[c_id]).initializing);
        this._getElement(id).parentNode.insertBefore(this.elements[c_id], this._getElement(id));

        this.snapshots = {};
        this.displays = {};
    }

    _getElement(id)
    {
        return document.getElementById(`vizzu_${id}`);
    }

    move(id, c_id)
    {
        if (this.elements[c_id].parentNode && this.elements[c_id].parentNode.parentNode) {
            this.elements[c_id].parentNode.parentNode.style.display = "none";
        }
        this._getElement(id).parentNode.parentNode.style.display = this.displays[id];
        this._getElement(id).parentNode.insertBefore(this.elements[c_id], this._getElement(id));
    }

    scroll(c_id, enabled)
    {
        if (!this.inhibitScroll && enabled) {
            this.elements[c_id].scrollIntoView({ behavior: "auto", block: "center" });
        }
    }

    static clearInhibitScroll()
    {
        this.inhibitScroll = false;
    }

    animate(displayTarget, id, c_id, scrollEnabled, chartTarget, chartAnimOpts)
    {
        if (displayTarget !== 'begin') {
            this.displays[id] = this._getElement(id).parentNode.parentNode.style.display;
        }
        this._getElement(id).parentNode.parentNode.style.display = "none";
        if (displayTarget !== 'end') this.move(id, c_id);
        this.charts[c_id] = this.charts[c_id].then(chart => {
            if (displayTarget !== 'actual') this.move(id, c_id);
            this.scroll(c_id, scrollEnabled);
            if (typeof chartTarget === 'string') {
                let snapshot = this.snapshots[chartTarget];
                chartTarget = snapshot;
            }
            chart.animate(chartTarget, chartAnimOpts);
            return chart;
        });
    }

    store(id, c_id)
    {
        this._getElement(id).parentNode.parentNode.style.display = "none";
        this.charts[c_id] = this.charts[c_id].then(chart => {
            this.snapshots[id] = chart.store();
            return chart;
        });
    }

    feature(id, c_id, name, enabled)
    {
        this._getElement(id).parentNode.parentNode.style.display = "none";
        this.charts[c_id] = this.charts[c_id].then(chart => {
            chart.feature(name, enabled);
            return chart;
        });
    }
}