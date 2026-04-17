import sys
import os
from annotator.core.runner import run_single_image

def main():
    if len(sys.argv) != 2:
        print("Error: No image path provided.")
        print("Usage: python main.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Error: File not found: {image_path}")
        sys.exit(1)

    run_single_image(image_path)

if __name__ == "__main__":
    main()
