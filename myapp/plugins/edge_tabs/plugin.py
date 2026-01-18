from langchain_core.tools import tool

@tool
def get_current_tab() -> str:
    return "你当前正在浏览：weather_agent 项目主页"
