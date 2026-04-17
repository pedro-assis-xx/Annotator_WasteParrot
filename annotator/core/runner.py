import sys
import json
import os
from annotator.core.pipeline import AnnotationPipeline
from annotator.utils.file_io import save_json_annotation, ensure_dir

def run_pipeline(path: str, output_folder: str = None):
    """
    Runs the pipeline on a single image or a folder of images.
    If output_folder is provided, saves results to JSON files.
    """
    pipeline = AnnotationPipeline()
    supported_extensions = ('.jpg', '.jpeg', '.png')

    if output_folder:
        ensure_dir(output_folder)

    if os.path.isdir(path):
        # Process folder
        files = [f for f in os.listdir(path) if f.lower().endswith(supported_extensions)]
        for filename in sorted(files):
            file_path = os.path.join(path, filename)
            print(f"Filename: {filename}")
            result = pipeline.process_image(file_path)
            
            # Print to terminal
            print(json.dumps(result, indent=2))
            
            # Save to file if output_folder is provided
            if output_folder:
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, f"{base_name}.json")
                save_json_annotation(result, output_path)
            
            print() # Extra newline for readability between entries
    elif os.path.isfile(path):
        # Process single file
        result = pipeline.process_image(path)
        
        # Print to terminal
        print(json.dumps(result, indent=2))
        
        # Save to file if output_folder is provided
        if output_folder:
            filename = os.path.basename(path)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.json")
            save_json_annotation(result, output_path)
    else:
        print(f"Error: Path is not a file or directory: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m annotator.core.runner <input_path> [output_folder]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    run_pipeline(input_path, output_folder)
