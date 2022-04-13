class IpyVizzu 
{
    constructor(element, chartId, vizzulib, divWidth, divHeight)
    {
        IpyVizzu.inhibitScroll = false;
        document.addEventListener('wheel', (evt) => { IpyVizzu.inhibitScroll = true }, true);
        document.addEventListener('keydown', (evt) => { IpyVizzu.inhibitScroll = true }, true);
        document.addEventListener('touchstart', (evt) => { IpyVizzu.inhibitScroll = true }, true);

        this.elements = {};
        this.elements[chartId] = document.createElement("div");
        this.elements[chartId].style.cssText = `width: ${divWidth}; height: ${divHeight};`;

        this.charts = {};
        this.charts[chartId] = import(vizzulib).then(Vizzu => new Vizzu.default(this.elements[chartId]).initializing);
        this._moveHere(chartId, element);

        this.snapshots = {};
        this.displays = {};
    }

    static clearInhibitScroll(element)
    {
        if (window.nbconvert) IpyVizzu._hide(element);
        IpyVizzu.inhibitScroll = false;
    }

    animate(element, chartId, displayTarget, scrollEnabled, chartTarget, chartAnimOpts)
    {
        if (window.nbconvert) IpyVizzu._hide(element);
        if (displayTarget === 'end') this._moveHere(chartId, element);
        this.charts[chartId] = this.charts[chartId].then(chart => {
            if (displayTarget === 'actual') this._moveHere(chartId, element);
            this._scroll(chartId, scrollEnabled);
            return chart.animate(chartTarget, chartAnimOpts);
        });
    }

    store(element, chartId, id)
    {
        if (window.nbconvert) IpyVizzu._hide(element);
        this.charts[chartId] = this.charts[chartId].then(chart => {
            this.snapshots[id] = chart.store();
            return chart;
        });
    }

    stored(element, id)
    {
        if (window.nbconvert) IpyVizzu._hide(element);
        return this.snapshots[id];
    }

    feature(element, chartId, name, enabled)
    {
        if (window.nbconvert) IpyVizzu._hide(element);
        this.charts[chartId] = this.charts[chartId].then(chart => {
            chart.feature(name, enabled);
            return chart;
        });
    }

    _moveHere(chartId, element)
    {
        if (window.nbconvert) IpyVizzu._display(this.elements[chartId], element);
        element.append(this.elements[chartId]);
    }

    _scroll(chartId, enabled)
    {
        if (!IpyVizzu.inhibitScroll && enabled) {
            this.elements[chartId].scrollIntoView({ behavior: "auto", block: "center" });
        }
    }

    static _hide(element) {
        document.getElementById(element.selector.substring(1)).parentNode.style.display = 'none';
    }

    static _display(prevElement, element) {
        if (prevElement.parentNode) {
            prevElement.parentNode.style.display = "none";
        }
        document.getElementById(element.selector.substring(1)).parentNode.style.display = 'flex';
        document.getElementById(element.selector.substring(1)).parentNode.style.margin = 'auto';
    }
}

window.IpyVizzu = IpyVizzu;