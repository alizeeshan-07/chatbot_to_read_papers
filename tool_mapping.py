import json
from paper_tools import search_papers, extract_info

tools = [
    {
        "name": "search_papers",
        "description": "Search for papers on arXiv based on a topic and store their information.",
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string", "description": "The topic to search for"},
                "max_results": {"type": "integer", "description": "Maximum number of results to retrieve", "default": 5}
            },
            "required": ["topic"]
        }
    },
    {
        "name": "extract_info",
        "description": "Search for information about a specific paper across all topic directories.",
        "input_schema": {
            "type": "object",
            "properties": {
                "paper_id": {"type": "string", "description": "The ID of the paper to look for"}
            },
            "required": ["paper_id"]
        }
    }
]

mapping_tool_function = {
    "search_papers": search_papers,
    "extract_info": extract_info
}

def execute_tool(tool_name, tool_args):
    result = mapping_tool_function[tool_name](**tool_args)
    if result is None:
        return "The operation completed but didn't return any results."
    elif isinstance(result, list):
        return ', '.join(result)
    elif isinstance(result, dict):
        return json.dumps(result, indent=2)
    else:
        return str(result)
