from typing import Dict, Any
from annotator.model.prompts import CATEGORY_TO_ID

def convert_to_yolo(json_output: Dict[str, Any]) -> str:
    """
    Converts a JSON annotation dictionary to YOLO format string.
    Fixed bounding box: center (0.5, 0.5), size (1.0, 1.0).
    """
    category = json_output.get("category", "Other")
    class_id = CATEGORY_TO_ID.get(category, CATEGORY_TO_ID["Other"])
    
    # YOLO format: <class_id> <x_center> <y_center> <width> <height>
    return f"{class_id} 0.5 0.5 1.0 1.0"
