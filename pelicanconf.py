from datetime import date
from pathlib import Path

import yaml


AUTHOR = "Hernán Larrea"
SITENAME = "Hernán Larrea"
SITESUBTITLE = "Technical Product Manager"
SITEURL = ""

PATH = "content"
THEME = "theme"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["portfolio"]

TIMEZONE = "America/Argentina/Buenos_Aires"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%B %-d, %Y"
RELATIVE_URLS = True

ARTICLE_PATHS = []
PAGE_PATHS = ["pages", "projects"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
DIRECT_TEMPLATES = ["index", "404", "robots", "sitemap"]
PAGINATED_TEMPLATES = {}

INDEX_SAVE_AS = "index.html"
ERROR_404_SAVE_AS = "404.html"
ROBOTS_SAVE_AS = "robots.txt"
SITEMAP_SAVE_AS = "sitemap.xml"

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}

DEFAULT_PAGINATION = False
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITE_DESCRIPTION = (
    "Hernán Larrea is a Technical Product Manager working across product "
    "strategy, platform engineering, infrastructure, and developer experience."
)
SOCIAL_IMAGE = "images/social-preview.png"
FAVICON = "images/favicon.png"
CURRENT_YEAR = date.today().year

MARKDOWN = {
    "extensions": ["markdown.extensions.extra", "markdown.extensions.smarty"],
    "extension_configs": {
        "markdown.extensions.smarty": {"smart_quotes": False},
    },
    "output_format": "html5",
}


def project_pages(pages, featured_only=False):
    """Return project pages in their intentional display order."""
    projects = [
        page
        for page in pages
        if page.metadata.get("content_type") == "project"
        and not page.metadata.get("draft", False)
        and (not featured_only or page.metadata.get("featured", False))
    ]
    return sorted(projects, key=lambda page: page.metadata.get("featured_order", 99))


JINJA_FILTERS = {"project_pages": project_pages}
JINJA_ENVIRONMENT = {
    "trim_blocks": True,
    "lstrip_blocks": True,
    "autoescape": True,
}

data_path = Path(__file__).parent / "data" / "cololabs.yml"
with data_path.open(encoding="utf-8") as data_file:
    COLOLABS_ITEMS = yaml.safe_load(data_file) or []
