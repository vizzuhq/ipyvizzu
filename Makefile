.PHONY: install dev clean check test format check-format lint

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG
NOTEBOOKS = $(shell find docs -type f -name '*.ipynb')

install:
	$(VIRTUAL_ENV)/bin/python setup.py install

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install -e .
	$(VIRTUAL_ENV)/bin/pip install notebook
	$(VIRTUAL_ENV)/bin/pip install pandas
	$(VIRTUAL_ENV)/bin/pip install click==8.0.4 black==22.1.0 tokenize-rt pylint jupytext==1.13.7
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user
	touch $(DEV_BUILD_FLAG)

clean:
	-rm -rf $(VIRTUAL_ENV)

doc: $(NOTEBOOKS:.ipynb=.html)

%.html: %.ipynb $(DEV_BUILD_FLAG)
	cd tools/html-generator; ../../$(VIRTUAL_ENV)/bin/jupyter nbconvert --Exporter.preprocessors=preprocessor.NbPreprocessor --to html ../../$<

check: check-format lint test

test: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m unittest discover tests/

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black ipyvizzu.py tests

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check ipyvizzu.py tests

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint \
		--disable missing-function-docstring \
		--disable missing-class-docstring \
		--disable missing-module-docstring \
		--disable too-few-public-methods \
		ipyvizzu.py tests
