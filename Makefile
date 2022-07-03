.PHONY: install dev clean check test format check-format lint

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG
NOTEBOOKS = $(shell find docs -type f -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*')

install:
	$(VIRTUAL_ENV)/bin/python setup.py install

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/python setup.py install
	$(VIRTUAL_ENV)/bin/pip install -r dev-requirements.txt
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user
	touch $(DEV_BUILD_FLAG)

clean:
	rm -rf $(VIRTUAL_ENV)
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

requirements:
	$(VIRTUAL_ENV)/bin/pip-compile --upgrade dev-requirements.in

doc: $(NOTEBOOKS:.ipynb=.html)

%.html: %.ipynb $(DEV_BUILD_FLAG)
	cd tools/html-generator; ../../$(VIRTUAL_ENV)/bin/jupyter nbconvert --Exporter.preprocessors=preprocessor.NbPreprocessor --to html --template classic --execute ../../$<

check: check-format lint test

test: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/coverage run --branch --source ipyvizzu -m unittest discover tests
	$(VIRTUAL_ENV)/bin/coverage html
	$(VIRTUAL_ENV)/bin/coverage report -m --fail-under=100

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black src tests tools docs

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check src tests tools docs

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint src tests tools
