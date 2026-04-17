import base64
import requests
import json
from typing import Dict, Any, Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llava:13b"):
        self.base_url = base_url
        self.model = model

    def _encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def annotate_image(self, image_path: str, system_prompt: str, user_prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        
        image_data = self._encode_image(image_path)
        
        # Combine system and user prompt for strict adherence to the requested format
        combined_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        payload = {
            "model": self.model,
            "prompt": combined_prompt,
            "images": [image_data],
            "stream": False
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "")
        except Exception:
            return ""
