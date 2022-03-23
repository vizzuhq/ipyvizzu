# Changelog

## [Unreleased]

### Fixed

- Fixed image url in the README.
- Fixed animation display when the first animation is not just Data.

### Added

- Added `Data.add_data_frame()` function to support `pandas.DataFrame`.
- Added `scroll_into_view` chart property.

## [0.6.0] - 2022-03-17

### Fixed

- Fixed code snippet in the README.
- Fixed `Publish documentation` workflow, pull requests skip push step.

### Added

- Added `Data.filter()` and `Data().set_filter()` methods.
- Added `Data.add_records()` function to add records' list in one step.
- Added CONTRIBUTING.md.
- Added `Release ipyvizzu` workflow.

## [0.5.0] - 2022-03-12

### Fixed

- Fixed `Style`, AnimationMerger conflict.
- Fixed `Style`, it can be None.
- Renamed `Data.add_serie()` to `Data.add_series()`.
- Restricted Vizzu's version to 0.4.x.

### Added

- Changed animation handling, Chart can be animated across the cells.
- Added `vizzu` Chart constructor parameter to change Vizzu's url.
- Added `width` and `height` Chart constructor parameters to change div's width and height.
- Added `display` Chart constructor parameter to change div's position.
- Added `Data.from_json()` function to import data from json file.
- Added `Snapshot` animation.
- Added `Chart.store()` function to save a `Snapshot`.
- Added Animation options handling through `**kwargs` of `Chart.animate()`, then `**kwargs` can not be configs anymore.
- Added shorter unique ids.
- Added unit tests.
- Added more notebook examples.
- Added test for notebook examples.
- Added `format` and `check-format` make parameters to format the code with `black`.
- Added `lint` make parameter to analyze the code with `pylint`.
- Added `test` make parameter to run tests.
- Added `check` make parameter to run CI check.
- Added pages build and deploy github action.

## [0.4.1] - 2022-02-15

### Added

- Added makefile github action.
- Added distinct animation handling in `Chart.animate()`.
- Added `Style` animation.

## [0.3.1] - 2022-01-08

### Fixed

- Fixed code snippet in the README.

## [0.3.0] - 2022-01-08

### Fixed

- Fixed notebook link in documentation.
- Fixed dev build flag, html targets build every time.

### Added

- Changed `Chart.set_feature()` to `Chart.feature()`.
- Changed `Chart.set_data()` and `Chart.set_config()` to `Chart.animate()`.
- Using modular examples in `make doc`.
- Added note about generated JavaScript code errors.

## [0.2.0] - 2022-01-07

### Added

- Added more notebook examples.
- Added `Chart.set_feature()`.
- Added unique div id.

## [0.1.1] - 2022-01-07

### Added

- First public release
