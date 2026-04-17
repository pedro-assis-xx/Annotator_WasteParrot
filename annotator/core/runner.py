import sys
import json
import os
from annotator.core.pipeline import AnnotationPipeline
from annotator.utils.file_io import save_json_annotation, save_text_file, ensure_dir
from annotator.formats.yolo import convert_to_yolo
from annotator.formats.json import convert_to_json

def run_pipeline(path: str, output_folder: str = None, output_format: str = "json"):
    """
    Runs the pipeline on a single image or a folder of images.
    If output_folder is provided, saves results to specified formats.
    Terminal output matches the selected output_format.
    """
    pipeline = AnnotationPipeline()
    supported_extensions = ('.jpg', '.jpeg', '.png')

    if output_folder:
        ensure_dir(output_folder)

    def process_item(item_path: str, filename: str):
        result = pipeline.process_image(item_path)
        
        # Terminal Output
        print("=" * 50)
        print(f"File: {filename}\n")
        
        if output_format in ("json", "both"):
            print("  JSON:")
            print(f"    category: {result.get('category')}")
            print(f"    material: {result.get('material')}")
            print(f"    caption: {result.get('caption')}")
            
        if output_format == "both":
            print() # Blank line between JSON and YOLO
            
        if output_format in ("yolo", "both"):
            print("  YOLO:")
            yolo_content = convert_to_yolo(result)
            print(f"    {yolo_content}")
        
        # Save to file if output_folder is provided
        if output_folder:
            base_name = os.path.splitext(filename)[0]
            
            # Save JSON
            if output_format in ("json", "both"):
                json_path = os.path.join(output_folder, f"{base_name}.json")
                save_json_annotation(result, json_path)
            
            # Save YOLO
            if output_format in ("yolo", "both"):
                yolo_content = convert_to_yolo(result)
                yolo_path = os.path.join(output_folder, f"{base_name}.txt")
                save_text_file(yolo_content, yolo_path)

    if os.path.isdir(path):
        # Process folder
        files = [f for f in os.listdir(path) if f.lower().endswith(supported_extensions)]
        for filename in sorted(files):
            file_path = os.path.join(path, filename)
            process_item(file_path, filename)
            print() # Extra newline for readability between entries
    elif os.path.isfile(path):
        # Process single file
        process_item(path, os.path.basename(path))
    else:
        print(f"Error: Path is not a file or directory: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m annotator.core.runner <input_path> [output_folder] [--format json|yolo|both]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_folder = None
    output_format = "json"

    # Minimal manual parsing for runner direct execution
    args = sys.argv[2:]
    if args and not args[0].startswith("--"):
        output_folder = args.pop(0)
    
    if "--format" in args:
        idx = args.index("--format")
        if idx + 1 < len(args):
            output_format = args[idx + 1]

    run_pipeline(input_path, output_folder, output_format)
