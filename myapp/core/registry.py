import importlib
import os
import yaml
from dataclasses import dataclass


@dataclass
class Plugin:
    name: str
    type: str          # tool / ui
    module: object
    entry: callable | None
    config: dict

def get_ui_plugin(plugins):
    for p in plugins:
        if p.type == "ui":
            return p
    raise RuntimeError("没有启用的 UI 插件")

def get_tool_plugins(plugins):
    return [p for p in plugins if p.type == "tool"]

def discover_plugins(*roots):
    """
    扫描多个插件目录，返回 Plugin 对象列表
    """
    plugins = []

    for root in roots:
        for name in os.listdir(root):
            plugin_dir = os.path.join(root, name)
            yaml_path = os.path.join(plugin_dir, "plugin.yaml")

            if not os.path.isfile(yaml_path):
                continue

            with open(yaml_path, "r", encoding="utf-8") as f:
                cfg = yaml.safe_load(f)

            if not cfg.get("enabled", False):
                continue

            module = importlib.import_module(
                cfg.get(
                    "module",
                    # 默认模块路径规则
                    f"{root.replace(os.sep, '.')}.{name}.plugin"
                )
            )

            entry = (
                getattr(module, cfg["entry"])
                if "entry" in cfg else None
            )

            plugins.append(
                Plugin(
                    name=cfg["name"],
                    type=cfg["type"],
                    module=module,
                    entry=entry,
                    config=cfg,
                )
            )

    return plugins
