# Repository Guidelines

## Project Structure & Module Organization

This repository contains the official `larrea.com.ar` portfolio, built with Python and Pelican. Standard pages live in `content/pages/`; portfolio case studies live in `content/projects/`; shared images live in `content/images/`. The custom presentation layer is under `theme/`, with Jinja templates in `theme/templates/` and CSS and JavaScript in `theme/static/`. Curated external writing is maintained in `data/cololabs.yml`, while the YAML reader lives in `plugins/portfolio.py`. Treat `output/` as generated content—do not edit or commit it.

## Build, Test, and Development Commands

Use the version in `.python-version` through `pyenv` and install dependencies only in the project virtual environment:

```sh
pyenv local 3.12.6
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
make dev      # build, watch, and serve on localhost:8000
make build    # build with development settings
make publish  # build with production URLs
make clean    # remove generated output
```

Run `make publish` before submitting changes to catch canonical URL, metadata, and asset-path issues.

## Coding Style & Naming Conventions

Follow PEP 8 for Python: four-space indentation, descriptive `snake_case` names, and uppercase Pelican setting names such as `SITEURL`. Keep Jinja templates readable and avoid business logic in templates. Name Markdown files with lowercase, hyphen-separated slugs (for example, `content/projects/ownership-registry.md`). Use lower-case YAML front-matter fields. Every page needs `title`, `slug`, and `summary`; projects must follow the metadata and section structure documented in `README.md`.

## Testing Guidelines

There is currently no automated test suite. A clean production build is required: run `make clean && make publish`, then inspect affected routes locally. Check navigation, internal links, responsive layout, images, metadata and keyboard behavior. Add focused tests when extending Python plugins or other executable site logic.

## Commit & Pull Request Guidelines

Use short, imperative commit subjects consistent with the related ColoLabs history, such as `Configure custom domain publishing`. Keep each commit focused and exclude `.venv/`, caches, and generated `output/`. Pull requests should explain the user-visible change, list validation performed, link relevant issues, and include before/after screenshots for layout or theme changes. Call out configuration, domain, or deployment changes explicitly.

## Site Scope & Configuration

Keep this site professional and portfolio-oriented; experimental or blog-first material belongs under the separate ColoLabs brand. Never commit credentials, deployment keys, or local environment files. The production canonical URL should be `https://larrea.com.ar`.
