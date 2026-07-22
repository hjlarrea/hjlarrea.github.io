# Hernán Larrea — Personal Portfolio

Source for [larrea.com.ar](https://larrea.com.ar), Hernán Larrea’s professional portfolio. The site is built with Python and Pelican, uses a custom local theme, and deploys to GitHub Pages. Writing, videos and experiments remain at [ColoLabs](https://cololabs.com.ar).

## Local setup

The repository uses Python 3.12.6 through `pyenv` and an isolated virtual environment:

```sh
pyenv install 3.12.6       # skip if already installed
pyenv local 3.12.6
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Common commands:

```sh
make dev      # build, watch, and serve at http://localhost:8000
make build    # development build with relative URLs
make publish  # production build for https://larrea.com.ar
make clean    # remove output/
```

Generated files in `output/` are deliberately ignored. Run `make publish` before opening a pull request.

## Editing site content

Standard pages live in `content/pages/`. Edit their YAML front matter for page titles, summaries and routes, and write the body in Markdown. The custom `plugins/portfolio.py` reader adds YAML front-matter support without an external Pelican plugin.

Project case studies live in `content/projects/`. To add one:

1. Copy an existing project file and choose a unique, lower-case slug.
2. Set `content_type: project`, `template: project`, and matching `url` and `save_as` values under `/work/`.
3. Complete every case-study section and remove its `Content needed` markers.
4. Set `featured` and `featured_order` to control homepage placement.
5. Run `make publish` and inspect the project page and `/work/`.

Do not publish confidential names, unsupported metrics, or invented outcomes.

## Curating ColoLabs links

Edit `data/cololabs.yml` to add up to three featured links. Each entry must point to its canonical `cololabs.com.ar` URL. Full articles are not copied into this repository. Automatic RSS ingestion could be added later as a build-time plugin, but the initial list is intentionally manual and deterministic.

## Theme and configuration

Shared Jinja templates and components are in `theme/templates/`; plain CSS and minimal JavaScript are in `theme/static/`. Development settings live in `pelicanconf.py`, while `publishconf.py` provides the production URL and clean-output behavior. `content/extra/CNAME` is copied into every build artifact.

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`. The workflow installs pinned dependencies, builds with `publishconf.py`, uploads `output/` as the Pages artifact, and deploys through GitHub’s official Pages actions. It can also be started manually from the Actions tab.
