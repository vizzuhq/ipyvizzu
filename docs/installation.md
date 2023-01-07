# Installation

`ipyvizzu` requires `IPython`, `jsonschema` and `pandas` packages.

!!! info
    `ipyvizzu` requires and downloads [Vizzu](https://lib.vizzuhq.com/)
    JavaScript/C++ library from
    [jsDelivr CDN](https://www.jsdelivr.com/package/npm/vizzu), but obviously
    you can use a self-hosted version of `Vizzu`, see
    [Chart settings chapter](./tutorial/chart_settings.md) of our tutorial.

## pypi

Run the following command to install `ipyvizzu` from
[pypi](https://pypi.org/project/ipyvizzu/)

```sh
pip install ipyvizzu
```

or the command below to upgrade it.

```sh
pip install -U ipyvizzu
```

You can use `ipyvizzu` in `Jupyter/IPython`, `Streamlit` or `Panel` (see
[Environments chapter](environments/index.md) of our documentation site).

### Jupyter/IPython

You can easily install `ipyvizzu` in your notebook without using the command
line if you place the following code into a cell.

```
!pip install ipyvizzu
```

## conda / mamba

Installing `ipyvizzu` from `conda-forge` can be achieved by adding `conda-forge`
to your channels with:

```sh
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled, run the following command to
install `ipyvizzu` from [conda](https://anaconda.org/conda-forge/ipyvizzu/)

```sh
conda install ipyvizzu

# or with mamba:

mamba install ipyvizzu
```

or the command below to upgrade it.

```sh
conda update ipyvizzu

# or with mamba:

mamba update ipyvizzu
```
