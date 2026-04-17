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

    # Clean the response text from markdown code blocks
    cleaned_text = response_text.strip()
    if cleaned_text.startswith("```"):
        # Remove starting ```json or ```
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[len("```json"):]
        else:
            cleaned_text = cleaned_text[len("```"):]
            
        # Remove ending ```
        if cleaned_text.endswith("```"):
            cleaned_text = cleaned_text[:-3]
    
    cleaned_text = cleaned_text.strip()

    try:
        # Try to parse JSON
        data = json.loads(cleaned_text)
        
        # Ensure category and material exist
        if "category" not in data:
            data["category"] = "Other"
        if "material" not in data:
            data["material"] = "Unknown"
            
        # Handle missing caption
        if "caption" not in data:
            data["caption"] = "No caption provided"
        
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
