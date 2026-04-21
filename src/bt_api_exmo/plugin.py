from bt_api_base.plugins.protocol import PluginInfo


class ExmoPluginInfo(PluginInfo):
    name = "exmo"
    version = "0.1.0"
    description = "EXMO exchange plugin"
    supported_modes = {"SPOT"}


def register_plugin():
    pass
