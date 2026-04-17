import sys
import json
from annotator.core.pipeline import AnnotationPipeline

def run_single_image(image_path: str):
    """
    Runs the pipeline on a single image and prints the JSON result.
    """
    pipeline = AnnotationPipeline()
    result = pipeline.process_image(image_path)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m annotator.core.runner <path_to_image>")
        sys.exit(1)
    
    img_path = sys.argv[1]
    run_single_image(img_path)
