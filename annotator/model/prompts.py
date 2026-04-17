# Strict sets of categories and materials
WASTE_CATEGORIES = [
    "Aluminum Structure/Struts",
    "Clothing",
    "Drink Pouch",
    "Gloves",
    "Nomex Bag",
    "Reclosable Bag",
    "Rehydratable Pouch",
    "Zotek F30 Aviation",
    "Other"
]

# Fixed mapping for YOLO class IDs
CATEGORY_TO_ID = {category: i for i, category in enumerate(WASTE_CATEGORIES)}

MATERIAL_LABELS = [
    "Aluminum",
    "Cotton",
    "Polyethylene",
    "Nitrile",
    "Nomex",
    "Nylon",
    "EVOH",
    "Zotek F30 Aviation Foam"
]

SYSTEM_PROMPT = f"""You are a specialized waste classification assistant. 
Your task is to analyze the provided image and output a structured JSON response.

You MUST choose the category from this list: {WASTE_CATEGORIES}. If unsure, use "Other".
You MUST choose the material from this list: {MATERIAL_LABELS}.

Output format MUST be a single JSON object with these fields:
{{
  "category": "...",
  "material": "...",
  "caption": "..."
}}

Return ONLY raw JSON. Do NOT wrap in markdown or code blocks. Do NOT include any text outside the JSON.
ALWAYS include ALL three fields (category, material, caption)."""

def get_annotation_prompt() -> str:
    return "Analyze this image and provide the classification as a raw JSON object only. No markdown, no explanation."

