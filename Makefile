PACKAGE = ipyvizzu
OS_TYPE = linux
PYTHON_BIN = python3
BIN_PATH = bin
ifeq ($(OS), Windows_NT)
	OS_TYPE = windows
	PYTHON_BIN = python
	BIN_PATH = Scripts
endif



.PHONY: clean \
	clean-dev update-dev-req install-dev-req install-kernel install touch-dev \
	check format check-format lint check-typing clean-test test-wo-install test \
	format-js \ lint-js \ check-js \
	clean-doc doc \
	clean-build build-release check-release release

VIRTUAL_ENV = .venv

DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG
DEV_JS_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_JS_BUILD_FLAG

NOTEBOOKS = $(shell find docs -type f -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*')



clean: clean-dev clean-test clean-doc clean-build



# init

clean-dev:
ifeq ($(OS_TYPE), windows)
	if exist $(VIRTUAL_ENV) ( rd /s /q $(VIRTUAL_ENV) )
else
	rm -rf $(VIRTUAL_ENV)
endif

update-dev-req: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/pip-compile --upgrade dev-requirements.in

install-dev-req:
	$(VIRTUAL_ENV)/$(BIN_PATH)/pip install -r dev-requirements.txt
	$(VIRTUAL_ENV)/$(BIN_PATH)/python tools/mdformat/customise_mdformat_black.py -v $(VIRTUAL_ENV) -l 78

install-kernel:
	$(VIRTUAL_ENV)/$(BIN_PATH)/ipython kernel install --user --name "$(VIRTUAL_ENV)"

install:
	$(VIRTUAL_ENV)/$(BIN_PATH)/pip install --use-pep517 .

touch-dev:
ifeq ($(OS_TYPE), windows)
	type NUL >> $(DEV_BUILD_FLAG)
else
	touch $(DEV_BUILD_FLAG)
endif

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	$(PYTHON_BIN) -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/$(BIN_PATH)/python -m pip install --upgrade pip
	$(MAKE) -f Makefile install
	$(MAKE) -f Makefile install-dev-req
	$(MAKE) -f Makefile install-kernel
	$(VIRTUAL_ENV)/$(BIN_PATH)/pre-commit install --hook-type pre-commit --hook-type pre-push
	$(MAKE) -f Makefile touch-dev

touch-dev-js:
ifeq ($(OS_TYPE), windows)
	type NUL >> $(DEV_JS_BUILD_FLAG)
else
	touch $(DEV_JS_BUILD_FLAG)
endif


$(DEV_JS_BUILD_FLAG):
	cd tools/javascripts && \
		npm update
	$(MAKE) -f Makefile touch-dev-js



# ci

check: check-format lint check-typing test

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/black src tests tools setup.py
	$(VIRTUAL_ENV)/$(BIN_PATH)/black docs
	$(VIRTUAL_ENV)/$(BIN_PATH)/python tools/mdformat/mdformat.py $(VIRTUAL_ENV)/$(BIN_PATH)/mdformat --wrap 80 --end-of-line keep docs README.md CONTRIBUTING.md CODE_OF_CONDUCT.md

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/black --check src tests tools setup.py
	$(VIRTUAL_ENV)/$(BIN_PATH)/black --check docs
	$(VIRTUAL_ENV)/$(BIN_PATH)/python tools/mdformat/mdformat.py $(VIRTUAL_ENV)/$(BIN_PATH)/mdformat --check --wrap 80 --end-of-line keep docs README.md CONTRIBUTING.md CODE_OF_CONDUCT.md

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/pylint src tests tools setup.py

check-typing: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/mypy src tests tools setup.py

clean-test:
ifeq ($(OS_TYPE), windows)
	if exist tests\coverage ( rd /s /q tests\coverage )
else
	rm -rf tests/coverage
endif

test-wo-install: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/coverage run --data-file tests/coverage/.coverage --branch --source ipyvizzu -m unittest discover tests
	$(VIRTUAL_ENV)/$(BIN_PATH)/coverage html --data-file tests/coverage/.coverage -d tests/coverage
	$(VIRTUAL_ENV)/$(BIN_PATH)/coverage report --data-file tests/coverage/.coverage -m --fail-under=100

test: $(DEV_BUILD_FLAG) install test-wo-install

format-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run prettier

lint-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run eslint

check-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run check



# doc

clean-doc:
	rm -rf docs/**/*.html

doc: $(NOTEBOOKS:.ipynb=.html)

%.html: %.ipynb $(DEV_BUILD_FLAG)
	cd tools/html-generator; ../../$(VIRTUAL_ENV)/$(BIN_PATH)/jupyter nbconvert --Exporter.preprocessors=preprocessor.NbPreprocessor --to html --template classic --execute ../../$<

mkdocs: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/mkdocs build -f ./tools/mkdocs/mkdocs.yml -d ../../site



# release

clean-build:
ifeq ($(OS_TYPE), windows)
	if exist build ( rd /s /q build )
	if exist dist ( rd /s /q dist )
	for /d /r src %%d in (*.egg-info) do @if exist "%%d" rd /s /q "%%d"
	for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
else
	rm -rf build
	rm -rf dist
	rm -rf `find src -name '*.egg-info'`
	rm -rf `find . -name '__pycache__'`
endif

build-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/python -m build

check-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/python -m twine check dist/*.tar.gz dist/*.whl

release: clean-build build-release check-release
