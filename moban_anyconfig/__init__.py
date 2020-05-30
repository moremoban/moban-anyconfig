# flake8: noqa
import moban.constants as constants
from lml.plugin import PluginInfo, PluginInfoChain

from moban_anyconfig._version import __author__, __version__

PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        constants.DATA_LOADER_EXTENSION,
        "%s.adapter.loads" % __name__,
        tags=[
            "toml",
            "pickle",
            "xml",
            "ini",
            "properties",
            "shellvars",
            "ion",
            "bson",
            "cbor",
            "configobj",
            "msgpack",
        ],
    )
)
