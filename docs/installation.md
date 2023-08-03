# Installation

`ipyvizzu` requires the `IPython` and `jsonschema` packages.

!!! info
    `ipyvizzu` requires and downloads the
    [Vizzu](https://github.com/vizzuhq/vizzu-lib) `JavaScript`/`C++`
    [library](https://www.jsdelivr.com/package/npm/vizzu) from `jsDelivr CDN`,
    but you can also use a different or self-hosted version of it. Check
    [Chart settings chapter](./tutorial/chart_settings.md) for more details.

## pypi

Run the following command to install `ipyvizzu` from
[pypi](https://pypi.org/project/ipyvizzu/)

```sh
pip install ipyvizzu
```

and this is how to upgrade it.

```sh
pip install -U ipyvizzu
```

!!! note
    `ipyvizzu` has some extra dependencies such as `pandas` and `fugue`.

    For example if you would like to work with `pandas` `DataFrame` and
    `ipyvizzu`, you can install `pandas` as an extra:

    ```sh
    pip install ipyvizzu[pandas]
    ```

You can use `ipyvizzu` in `Jupyter/IPython`, `Streamlit` or `Panel` (see
[Environments chapter](environments/index.md) for more details).

### Jupyter/IPython

You can install `ipyvizzu` in your notebook without using the command line by
entering the following code into a cell.

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

and this is how to upgrade it.

```sh
conda update ipyvizzu

# or with mamba:

mamba update ipyvizzu
```
