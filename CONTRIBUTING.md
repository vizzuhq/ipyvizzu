# Contributing

# Issues

You can find our open issues in the project's [issue tracker](https://github.com/vizzuhq/ipyvizzu/issues). Please let us know if you find any issues or have any feature requests there.

# CI check

The `check` make target collects the targets which are run by the `CI check` workflow.
The `CI check` workflow invokes the `check-format`, the `lint` and the `test` targets.

```sh
make check
```

### Formatting

The ipyvizzu project is formatted with `black`.
Run the `check-format` target to check that the python files are formatted with `black`.

```sh
make check-format
```

`black` can be run with the `format` make target.

```sh
make format
```

### Linter

The `lint` target runs `pylint` over the ipyvizzu project.

```sh
make lint
```

### Testing

The unit tests can be run with the `test` make target. As part of the unit
tests the notebooks under the `docs/examples` are executed, too.

```sh
make test
```

## Generating documentation

Documentation can be build with the `doc` make target.

```sh
make doc
```

The `Publish documentation` workflow invokes the `doc` target
and publish it to the gh-pages branch.

Online version can be read at [Tutorial & Examples](https://ipyvizzu.vizzuhq.com/).


### Releasing the project

Visit our [releasing guide](https://github.com/vizzuhq/ipyvizzu/blob/main/RELEASE.md) for further info.
