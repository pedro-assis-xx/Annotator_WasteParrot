# Annotator WasteParrot

Annotator WasteParrot is a modular Python-based pipeline for automated image annotation using local vision-language models (VLM). It leverages **Ollama** and the **LLaVA** model to perform inference without cloud dependencies, generating structured datasets for waste classification.

The system features both a powerful **CLI** for automation and a user-friendly **Tkinter GUI** for desktop use, both supporting real-time progress tracking and batch processing.

## Features

- **Local Inference**: Runs entirely on your hardware via Ollama for privacy and zero cost.
- **Dual Interface**: Use the command line or the graphical interface.
- **Single & Batch Processing**: Annotate individual files or entire folders of images (`.jpg`, `.jpeg`, `.png`).
- **Real-time Progress**: Live log panel in the GUI and console updates show processing status.
- **Non-Blocking GUI**: Threaded execution ensures the interface remains responsive during long batch runs.
- **Multiple Output Formats**: Supports JSON metadata and YOLO (classification-style) exports.
- **Automated Validation**: Ensures model output conforms to a strict taxonomy of categories and materials.
- **File Safety**: Includes overwrite warnings and automatic directory management.

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
*Note: `tkinter` is standard with Python. On Linux, you may need to install `python3-tk` via your package manager.*

## Usage

### GUI (Graphical Interface)
Launch the GUI:
```bash
python gui.py
```
1. **Browse** for an **Input Folder** containing images.
2. **Browse** for an **Output Folder** to save annotations.
3. Select the **Output Format** (json, yolo, or both).
4. Click **Run Annotation**. Progress will be shown in the live log panel.

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/bb4d814f-820b-4a05-b7b5-428fbc378328"
    alt="gui"
    width="500"
  />
</p>


### CLI (Command Line)
Run the pipeline using `main.py`.

**Batch process a folder:**
```bash
python main.py images/ output/ --format both
```
<p align="center">
  <img
    src="https://github.com/user-attachments/assets/1e6ea7bd-60c5-4e6c-8acd-9a40c0f69fc4"
    alt="cli"
    width="800"
  />
</p>


**Process a single image:**
```bash
python main.py image.jpg output/ --format json
```

## Output Formats

### JSON
Saves a `.json` file containing structured metadata:
```json
{
  "category": "Nomex Bag",
  "material": "Fabric",
  "caption": "A white nomex bag used for storage."
}
```

### YOLO
Saves a `.txt` file in YOLO format. Since this tool performs classification, the bounding box is fixed to the full image:
`<class_id> 0.5 0.5 1.0 1.0`

## Project Structure

- `gui.py`: Tkinter-based graphical interface with threading.
- `main.py`: CLI entry point.
- `annotator/`:
    - `core/`: Runner orchestration and pipeline logic.
    - `model/`: Ollama client and prompt taxonomy.
    - `formats/`: Exporters for JSON and YOLO.
    - `utils/`: File I/O and utility functions.

## Limitations

- **Bounding Boxes**: Does not detect specific object boundaries; assumes the object of interest occupies the full image.
- **Single Object**: Optimized for images containing a single primary waste item.
