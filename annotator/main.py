import argparse
import os
import sys
from annotator.core.runner import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="Annotator WasteParrot - VLM Image Annotation Pipeline")
    parser.add_argument("input_path", help="Path to a single image or a folder of images")
    parser.add_argument("output_folder", nargs="?", help="Folder where annotations will be saved")
    parser.add_argument("--format", choices=["json", "yolo", "both"], default="json", 
                        help="Output format (default: json)")

    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        print(f"Error: Input path not found: {args.input_path}")
        sys.exit(1)

    run_pipeline(args.input_path, args.output_folder, args.format)

if __name__ == "__main__":
    main()
