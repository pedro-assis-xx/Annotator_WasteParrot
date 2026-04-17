# Annotator WasteParrot

Annotator WasteParrot is a modular Python-based pipeline for automated image annotation using local vision-language models (VLM). It leverages **Ollama** and the **LLaVA** model to perform inference without cloud dependencies, generating structured datasets for waste classification.

## Features

- **Single Image Processing**: Annotate a single image file.
- **Batch Folder Processing**: Process all images (`.jpg`, `.jpeg`, `.png`) within a directory.
- **Multiple Output Formats**: Supports JSON and YOLO (classification-style) exports.
- **Automated Validation**: Ensures model output conforms to a strict taxonomy of categories and materials.
- **Local Inference**: Runs entirely on your hardware via Ollama.

## Installation

### Prerequisites

1.  **Ollama**: [Download and install Ollama](https://ollama.com/).
2.  **LLaVA Model**: Pull the required model:
    ```bash
    ollama pull llava:13b
    ```

### Setup

Install Python dependencies:
```bash
pip install -r annotator/requirements.txt
```

## Usage

Run the pipeline using `main.py`. The tool accepts an input path (file or folder), an optional output folder, and a format specification.

### Examples

**Process a single image and save JSON:**
```bash
python main.py image.jpg output/
```

**Batch process a folder:**
```bash
python main.py images/ output/
```

**Specify output format (json, yolo, or both):**
```bash
python main.py images/ output/ --format yolo
python main.py images/ output/ --format both
```

## Output Formats

### JSON (Default)
Saves a `.json` file containing:
- `category`: Predefined waste category.
- `material`: Predominant material detected.
- `caption`: A brief descriptive caption.

### YOLO
Saves a `.txt` file in YOLO format:
`<class_id> <x_center> <y_center> <width> <height>`

*Note: As this tool currently performs classification, the bounding box is fixed to the entire image (`0.5 0.5 1.0 1.0`).*

## Class Mapping (YOLO)

| ID | Category |
|----|----------|
| 0 | Aluminum Structure/Struts |
| 1 | Clothing |
| 2 | Drink Pouch |
| 3 | Gloves |
| 4 | Nomex Bag |
| 5 | Reclosable Bag |
| 6 | Rehydratable Pouch |
| 7 | Zotek F30 Aviation |
| 8 | Other |

## Limitations

- **Bounding Boxes**: Does not currently detect object boundaries; assumes the object of interest occupies the full image.
- **Model Accuracy**: Results are dependent on the `llava:13b` model's performance.
- **Single Object**: Optimized for images containing a single primary waste item.
