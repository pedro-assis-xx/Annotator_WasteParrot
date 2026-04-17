import os
import json
from typing import Dict, Any

def save_json_annotation(data: Dict[str, Any], output_path: str):
    """
    Saves the annotation dictionary as a JSON file.
    Warns if the file already exists.
    """
    if os.path.exists(output_path):
        print(f"\n  [WARNING] Overwriting {os.path.basename(output_path)}")
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

def save_text_file(content: str, output_path: str):
    """
    Saves a string content as a text file.
    Warns if the file already exists.
    """
    if os.path.exists(output_path):
        print(f"\n  [WARNING] Overwriting {os.path.basename(output_path)}")
    
    with open(output_path, 'w') as f:
        f.write(content)

def ensure_dir(directory: str):
    """
    Ensures a directory exists.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
