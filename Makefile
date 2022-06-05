.PHONY: install dev dev-req clean check test format check-format lint release release-build release-validate

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG
NOTEBOOKS = $(shell find docs -type f -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*')

install: $(DEV_BUILD_FLAG)
	echo "pyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py install
	echo "ipyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py install
	echo "stpyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py install

dev-req: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pip-compile --upgrade dev-requirements.in

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install pip==22.0.4
	$(VIRTUAL_ENV)/bin/pip install -r dev-requirements.txt
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user
	echo "pyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py install
	echo "ipyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py install
	echo "stpyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py install
	touch $(DEV_BUILD_FLAG)

clean:
	-rm -rf $(VIRTUAL_ENV)
	-rm -rf build
	-rm -rf dist
	-rm -rf *.egg-info


doc: $(NOTEBOOKS:.ipynb=.html)

%.html: %.ipynb $(DEV_BUILD_FLAG)
	cd tools/html-generator; ../../$(VIRTUAL_ENV)/bin/jupyter nbconvert --Exporter.preprocessors=preprocessor.NbPreprocessor --to html --template classic --execute ../../$<


check: check-format lint test

test: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m unittest discover tests/

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black src tests tools

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check src tests tools

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint \
		--disable missing-function-docstring \
		--disable missing-class-docstring \
		--disable missing-module-docstring \
		--disable too-few-public-methods \
		--disable duplicate-code \
		src tests tools


release-build: $(DEV_BUILD_FLAG)
	echo "pyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py sdist bdist_wheel
	echo "ipyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py sdist bdist_wheel
	echo "stpyvizzu" > PKG.cfg
	$(VIRTUAL_ENV)/bin/python setup.py sdist bdist_wheel

release-validate: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m twine check dist/*.tar.gz dist/*.whl

release: release-build release-validate
	
