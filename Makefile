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
	touch-dev-js dev-js \
	check format check-format check-lint check-typing clean-test test \
	check-js format-js check-format-js lint-js check-lint-js \
	clean-doc doc \
	clean-build set-version build-release check-release release

VIRTUAL_ENV = .venv_ipyvizzu

DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG
DEV_JS_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_JS_BUILD_FLAG



clean: clean-dev clean-test clean-doc clean-build



# init

clean-dev:
	$(PYTHON_BIN) -c "import os, shutil;shutil.rmtree('$(VIRTUAL_ENV)') if os.path.exists('$(VIRTUAL_ENV)') else print('Nothing to be done for \'clean-dev\'')"

update-dev-req: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/pip-compile --upgrade dev-requirements.in

install-dev-req:
	$(VIRTUAL_ENV)/$(BIN_PATH)/pip install -r dev-requirements.txt

install-kernel:
	$(VIRTUAL_ENV)/$(BIN_PATH)/ipython kernel install --user --name "$(VIRTUAL_ENV)"

install:
	$(VIRTUAL_ENV)/$(BIN_PATH)/pip install --use-pep517 .

touch-dev:
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) tools/make/touch.py -f $(DEV_BUILD_FLAG)

touch-dev-js:
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) tools/make/touch.py -f $(DEV_JS_BUILD_FLAG)

dev: $(DEV_BUILD_FLAG)

dev-js: $(DEV_BUILD_FLAG)
	npm install ./tools/javascripts/

$(DEV_BUILD_FLAG):
	$(PYTHON_BIN) -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) -m pip install --upgrade pip
	$(MAKE) -f Makefile install
	$(MAKE) -f Makefile install-dev-req
	$(MAKE) -f Makefile install-kernel
	$(VIRTUAL_ENV)/$(BIN_PATH)/pre-commit install --hook-type pre-commit --hook-type pre-push
	$(MAKE) -f Makefile touch-dev

$(DEV_JS_BUILD_FLAG):
	npm install ./tools/javascripts/
	$(MAKE) -f Makefile touch-dev-js



# ci

check: check-format check-lint check-typing test

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/black src tests tools setup.py
	$(VIRTUAL_ENV)/$(BIN_PATH)/black -l 70 docs
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) tools/mdformat/mdformat.py $(VIRTUAL_ENV)/$(BIN_PATH)/mdformat \
		--wrap 80 \
		--end-of-line keep \
		--line-length 70 \
		docs README.md CONTRIBUTING.md CODE_OF_CONDUCT.md

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/black --check src tests tools setup.py
	$(VIRTUAL_ENV)/$(BIN_PATH)/black --check -l 70 docs
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) tools/mdformat/mdformat.py $(VIRTUAL_ENV)/$(BIN_PATH)/mdformat \
		--check \
		--wrap 80 \
		--end-of-line keep \
		--line-length 70 \
		docs README.md CONTRIBUTING.md CODE_OF_CONDUCT.md

check-lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/pylint src tests tools setup.py

check-typing: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/mypy src tests tools setup.py

clean-test:
ifeq ($(OS_TYPE), windows)
	if exist tests\coverage ( rd /s /q tests\coverage )
else
	rm -rf tests/coverage
endif

test: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/coverage run \
		--data-file tests/coverage/.coverage --branch --source ipyvizzu -m unittest discover tests
	$(VIRTUAL_ENV)/$(BIN_PATH)/coverage html \
	 	--data-file tests/coverage/.coverage -d tests/coverage
	$(VIRTUAL_ENV)/$(BIN_PATH)/coverage report \
		--data-file tests/coverage/.coverage -m --fail-under=100



check-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run check

format-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run prettier

check-format-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run check-prettier

lint-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run eslint

check-lint-js: $(DEV_JS_BUILD_FLAG)
	cd tools/javascripts && \
		npm run check-eslint



# doc

clean-doc:
ifeq ($(OS_TYPE), windows)
	if exist site ( rd /s /q site )
	for /d /r docs %%d in (.ipynb_checkpoints) do @if exist "%%d" rd /s /q "%%d"
else
	rm -rf site
	rm -rf `find docs -name '.ipynb_checkpoints'`
endif

doc: $(DEV_BUILD_FLAG) $(DEV_JS_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/mkdocs build -f ./tools/mkdocs/mkdocs.yml



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

set-version: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) tools/release/set_version.py 

build-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) -m build

check-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/$(BIN_PATH)/$(PYTHON_BIN) -m twine check dist/*.tar.gz dist/*.whl

release: clean-build set-version build-release check-release
