# Annotator WasteParrot - System Architecture

This document provides a technical overview of the Annotator WasteParrot system for AI agents and developers.

## System Overview

The system follows a modular architecture where core processing logic is shared between multiple interfaces:

**Interface** (CLI/GUI) → **Runner** → **Pipeline** → **Model (Ollama)** → **Processor** → **Exporters**

## Key Modules

- **`gui.py`**: Tkinter-based frontend. Implements a **threaded execution model** (using `threading`) to maintain UI responsiveness. It schedules thread-safe UI updates via `root.after()` and uses a progress log panel.
- **`annotator/core/runner.py`**: The orchestration engine. Handles file discovery for batch processing and supports an optional **callback system** for real-time progress reporting (`[index/total] filename → done`).
- **`annotator/core/pipeline.py`**: Manages the high-level VLM data flow, coordinating between the model client and the validation processor.
- **`annotator/core/processor.py`**: Sanitizes raw model output and validates it against the allowed taxonomy.
- **`annotator/model/ollama_client.py`**: Low-level HTTP interface to the local Ollama API (`/api/generate`).
- **`annotator/model/prompts.py`**: Source of truth for the system prompt, waste categories, and material taxonomy.
- **`annotator/formats/`**: Specialized exporters for JSON and YOLO.
- **`annotator/utils/file_io.py`**: Safe file operations, including overwrite warnings and directory creation.

## Data Flow

1.  **Orchestration**: `runner.py` iterates through input files.
2.  **Inference**: `pipeline.py` sends base64 image data to the LLaVA model via Ollama.
3.  **Sanitization & Validation**: `processor.py` ensures the model followed formatting rules and matches the taxonomy.
4.  **Transformation**: The validated JSON is converted into the requested formats (JSON, YOLO).
5.  **Reporting**: A callback notifies the UI (CLI or GUI) of the completion of each image.
6.  **Persistence**: Files are saved to the designated output folder.

## Design Decisions

- **Local-Only Inference**: Relies exclusively on local Ollama services to ensure data privacy and eliminate cloud latency/costs.
- **JSON as Primary Source**: JSON is treated as the internal "source of truth." All other formats (like YOLO) are derived from the validated JSON metadata.
- **Async reporting in Sync Pipeline**: While the pipeline runs synchronously within its thread, the callback system provides asynchronous-like updates to the user interface.
- **Minimal Dependencies**: Keeps the core library light, relying on `requests` for API communication and `tkinter` for the GUI.

## Extension Guidelines

- **New Formats**: Add a module to `annotator/formats/` and integrate it into `runner.py`.
- **Taxonomy Changes**: Modify `WASTE_CATEGORIES` or `MATERIAL_LABELS` in `annotator/model/prompts.py`.
- **UI Enhancements**: Add widgets to `AnnotatorGUI` in `gui.py`. Always ensure long-running logic remains inside the `worker` thread to prevent freezing.
