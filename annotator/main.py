import sys
import os
from annotator.core.runner import run_pipeline

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error: Invalid arguments.")
        print("Usage: python main.py <input_path> [output_folder]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) == 3 else None
    
    if not os.path.exists(input_path):
        print(f"Error: Input path not found: {input_path}")
        sys.exit(1)

    run_pipeline(input_path, output_folder)

if __name__ == "__main__":
    main()
