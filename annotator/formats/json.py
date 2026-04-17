import json
from typing import Dict, Any

def convert_to_json(data: Dict[str, Any]) -> str:
    """
    Converts annotation dictionary to a formatted JSON string.
    """
    return json.dumps(data, indent=2)
