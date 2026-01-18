from myapp.core.registry import discover_plugins, get_ui_plugin
from myapp.core.engine import build_agent
import os


if __name__ == "__main__":
    base = os.path.dirname(__file__)

    plugins = discover_plugins(
        os.path.join(base, "myapp", "plugins"),
        os.path.join(base, "myapp", "ui_plugins"),
    )

    ui = get_ui_plugin(plugins)
    ui.entry(build_agent)
