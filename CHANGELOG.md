# Changelog

## [Unreleased]

## [0.10.0] - 2022-05-25

### Added

- Added `Chart._repr_html_()` method.

## [0.9.0] - 2022-04-29

### Added

- Changed the DataFrame column's type recognition with checking `dtype` is a numeric type or not .
- Deprecated `infer_types` parameter of `Data.add_data_frame()`, because it can be set via `dtype`.
- Added `Data().add_data_frame_index(data_frame, name)`, with this `pandas.DataFrame.index` can be added to `Data()`.
- Added `Data` verification by schema.

## [0.8.1] - 2022-04-14

### Fixed

- Revert pip-compiled dependencies.

## [0.8.0] - 2022-04-14

### Fixed

- Fixed `Data.add_data_frame()` in order to handle `None` and `pd.Series` as `data_frame` parameter.

### Added

- Changed default value of the `Chart.scroll_into_view` property to `False`.
- Separated the JavaScript code into a JavaScript file instead of the previous string template.
- Added `Chart.show()` and `DisplayTarget.MANUAL`, with these the displaying of the chart can be controlled.

## [0.7.0] - 2022-03-29

### Fixed

- Fixed image url in the README.
- Fixed animation display when the first animation is not just Data.

### Added

- Added `Data.add_data_frame()` function to support `pandas.DataFrame`.
- Added `scroll_into_view` chart property.
- Added example gallery.

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
