.PHONY: install dev clean doc

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG

install:
	python3 setup.py install

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install -e .
	$(VIRTUAL_ENV)/bin/pip install notebook
	touch $(DEV_BUILD_FLAG)

clean:
	-rm -rf $(VIRTUAL_ENV)

doc: dev docs/ipyvizzu.html
	$(VIRTUAL_ENV)/bin/jupyter nbconvert --to html docs/ipyvizzu.ipynb
