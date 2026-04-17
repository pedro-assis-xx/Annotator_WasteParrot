from annotator.model.ollama_client import OllamaClient
from annotator.model.prompts import SYSTEM_PROMPT, get_annotation_prompt
from annotator.core.processor import validate_annotation
from typing import Dict, Any

class AnnotationPipeline:
    def __init__(self, ollama_url: str = "http://localhost:11434", model: str = "llava:13b"):
        self.client = OllamaClient(base_url=ollama_url, model=model)

    def process_image(self, image_path: str) -> Dict[str, Any]:
        """
        Orchestrates the annotation of a single image.
        """
        user_prompt = get_annotation_prompt()
        response_text = self.client.annotate_image(
            image_path=image_path,
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt
        )
        return validate_annotation(response_text)
