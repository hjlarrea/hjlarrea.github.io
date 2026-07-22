"""Read YAML front matter while keeping Pelican content local and portable."""

from markdown import Markdown
import yaml

from pelican.plugins import signals
from pelican.readers import MarkdownReader
from pelican.utils import pelican_open


class YamlMarkdownReader(MarkdownReader):
    """Markdown reader supporting a leading ``---`` YAML metadata block."""

    def read(self, source_path):
        with pelican_open(source_path) as source_file:
            source = source_file

        metadata = {}
        body = source
        if source.startswith("---\n"):
            _, front_matter, body = source.split("---", 2)
            raw_metadata = yaml.safe_load(front_matter) or {}
            if raw_metadata.get("content_type") == "project" and "status" in raw_metadata:
                raw_metadata["project_status"] = raw_metadata.pop("status")
            metadata = {
                str(name).lower(): self.process_metadata(str(name).lower(), value)
                for name, value in raw_metadata.items()
                if value is not None
            }

        markdown = Markdown(**self.settings["MARKDOWN"])
        return markdown.convert(body), metadata


def register_reader(readers):
    readers.reader_classes["md"] = YamlMarkdownReader
    readers.reader_classes["markdown"] = YamlMarkdownReader


def register():
    signals.readers_init.connect(register_reader)
