.PHONY: install dev clean test check format check-format

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG

install:
	python3 setup.py install

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install -e .
	$(VIRTUAL_ENV)/bin/pip install notebook
	$(VIRTUAL_ENV)/bin/pip install black==22.1.0 pylint sphinx myst-nb
	touch $(DEV_BUILD_FLAG)

clean:
	-rm -rf $(VIRTUAL_ENV)

doc:
	. .venv/bin/activate && $(MAKE) -C docs html

%.html: %.ipynb $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/jupyter nbconvert --to html $<

check: check-format test lint

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
