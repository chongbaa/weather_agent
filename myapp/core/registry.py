# myapp/core/registry.py
import importlib
import pkgutil
import yaml
import os
from langchain_core.tools import Tool
from myapp.utils.logging import init_logger

logger = init_logger("plugin-loader")

def discover_plugins():
    tools = []
    from myapp.plugins import __path__ as plugin_path

    for _, name, _ in pkgutil.iter_modules(plugin_path):
        plugin_dir = os.path.join(plugin_path[0], name)
        config_path = os.path.join(plugin_dir, "plugin.yaml")

        if not os.path.exists(config_path):
            logger.warning(f"插件 {name} 缺少 plugin.yaml，已跳过")
            continue

        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        if not config.get("enabled", False):
            logger.info(f"插件 {name} 被禁用，已跳过")
            continue

        try:
            module = importlib.import_module(f"myapp.plugins.{name}.plugin")
            for attr in dir(module):
                obj = getattr(module, attr)
                if callable(obj) and hasattr(obj, "__tool"):
                    tools.append(Tool.from_function(obj))
                    logger.info(f"插件 {name} 中的工具 {attr} 已加载")
        except Exception as e:
            logger.error(f"加载插件 {name} 失败: {e}")

    return tools

