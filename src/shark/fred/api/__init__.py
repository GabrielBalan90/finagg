"""FRED top-level interface."""

from ._api import get
from .category import category
from .release import release, releases
from .series import series
from .source import source, sources
from .tags import related_tags, tags
