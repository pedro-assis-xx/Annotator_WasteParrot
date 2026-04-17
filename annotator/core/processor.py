import json
from typing import Dict, Any
from annotator.model.prompts import WASTE_CATEGORIES, MATERIAL_LABELS

def validate_annotation(response_text: str) -> Dict[str, Any]:
    """
    Parses the model response and validates it against allowed categories and materials.
    """
    fallback = {
        "category": "Other",
        "material": "Unknown",
        "caption": "Invalid model output"
    }

    try:
        # Try to parse JSON
        data = json.loads(response_text)
        
        # Check for required keys
        if not all(k in data for k in ("category", "material", "caption")):
            return fallback
        
        # Validate category
        if data["category"] not in WASTE_CATEGORIES:
            data["category"] = "Other"
            
        # Validate material
        if data["material"] not in MATERIAL_LABELS:
            data["material"] = "Unknown"
            
        return {
            "category": data["category"],
            "material": data["material"],
            "caption": data["caption"]
        }
    except Exception:
        return fallback
