PYTHON ?= .venv/bin/python
PELICAN ?= .venv/bin/pelican
OUTPUT ?= output
PUBLISHCONF ?= publishconf.py
GITHUB_PAGES_BRANCH=gh-pages
GITHUB_PAGES_COMMIT_MESSAGE=Generate Pelican site

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif

.PHONY: help dev build publish clean

help:
	@echo "make dev      Build, watch, and serve at http://localhost:8000"
	@echo "make build    Build with local settings"
	@echo "make publish  Build with production settings"
	@echo "make github   Upload the web site via gh-pages"
	@echo "make clean    Remove generated output"

dev:
	$(PELICAN) content -o $(OUTPUT) -s "${PUBLISHCONF}" --listen --autoreload

build:
	$(PELICAN) content -o $(OUTPUT) -s "${PUBLISHCONF}"

publish:
	$(PELICAN) content -o $(OUTPUT) -s "${PUBLISHCONF}"

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUY)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

github: publish
	ghp-import -m "$(GITHUB_PAGES_COMMIT_MESSAGE)" -b $(GITHUB_PAGES_BRANCH) "$(OUTPUT)" --no-jekyll
	git push origin $(GITHUB_PAGES_BRANCH)

clean:
	$(PYTHON) -c 'import shutil; shutil.rmtree("$(OUTPUT)", ignore_errors=True)'
