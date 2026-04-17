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

Output format MUST be:
{{
  "category": "...",
  "material": "...",
  "caption": "..."
}}

Return ONLY JSON (no extra text)."""

def get_annotation_prompt() -> str:
    return "Analyze this image and provide the classification in the specified JSON format."
