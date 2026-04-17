# Annotator WasteParrot - System Architecture

This document provides a technical overview of the Annotator WasteParrot system for AI agents and developers.

## System Overview

The system follows a linear end-to-end flow for processing images:
**Input Path** (CLI) → **Runner** → **Pipeline** → **Model (Ollama)** → **Processor (Validation)** → **Formats** → **Output (Files/Terminal)**

## Key Modules

- **`annotator/core/runner.py`**: Entry point for orchestration. Handles CLI arguments (`argparse`), manages batch/single processing, and coordinates format selection for terminal display and file saving.
- **`annotator/core/pipeline.py`**: Coordinates the high-level data flow. Retrieves prompts, calls the model client, and passes the raw response to the processor.
- **`annotator/core/processor.py`**: Responsible for sanitizing model output (removing markdown blocks) and validating it against the allowed taxonomy. Handles missing fields with defaults.
- **`annotator/model/ollama_client.py`**: Low-level interface to the Ollama local API (`/api/generate`). Encodes images to base64 and handles HTTP communication.
- **`annotator/model/prompts.py`**: Defines the system/user prompts and the strict taxonomy (Categories and Materials). Includes YOLO class ID mapping.
- **`annotator/formats/json.py`**: Logic for exporting validated data to JSON format.
- **`annotator/formats/yolo.py`**: Logic for converting validated JSON data into YOLO-formatted text strings (using fixed full-image bounding boxes).
- **`annotator/utils/file_io.py`**: Helper functions for directory management and safely writing JSON/Text files to disk with overwrite warnings.

## Data Flow

1.  **Image Loading**: Base64 encoding of the input image.
2.  **Model Inference**: VLM (LLaVA) generates a raw text response based on strict formatting instructions.
3.  **Sanitization**: `processor.py` strips markdown code blocks (e.g., ` ```json `) and extra whitespace.
4.  **Validation**: Parsed JSON is checked against `WASTE_CATEGORIES` and `MATERIAL_LABELS`.
5.  **Transformation**: The "source of truth" JSON is converted into the requested output formats (JSON/YOLO).
6.  **Delivery**: Results are printed to the terminal and/or saved to the output directory.

## Output Formats

- **JSON**: Full metadata (Category, Material, Caption).
- **YOLO**: Classification-style annotation with fixed coordinates (`0.5 0.5 1.0 1.0`) representing the full image.

## Design Constraints

- **Local-Only**: Dependencies are limited to local services (Ollama) to ensure data privacy and no cloud costs.
- **Efficiency**: Only one model call is performed per image. All export formats are derived from the initial successful model response.
- **Consistency**: JSON is treated as the primary internal representation and source of truth for all subsequent exports.

## Extension Guidelines

- **Adding Formats**: Create a new module in `annotator/formats/` and integrate it into `runner.py`.
- **Batch Features**: Modify `runner.py` to add parallel processing or advanced filtering logic.
- **GUI**: Implement a wrapper around `run_pipeline` in a new top-level module (e.g., `gui.py`).
