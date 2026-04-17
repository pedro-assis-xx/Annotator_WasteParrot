# Annotator WasteParrot - Project Context

## Project Overview
Annotator WasteParrot is a modular Python-based pipeline designed for automated image annotation using local vision-language models (VLM). It leverages **Ollama** and the **LLaVA** model to perform inference without cloud dependencies. The primary goal is to generate structured datasets (category, material, caption) for waste classification and machine learning workflows.

### Core Technologies
- **Language:** Python 3.10+
- **Inference Engine:** Ollama (running locally at `http://localhost:11434`)
- **VLM Model:** `llava:13b` (configurable)
- **Libraries:** `requests` for API communication

### Architecture
- `annotator/main.py`: Entry point for CLI usage.
- `annotator/core/`: Contains the logic for orchestration (`pipeline.py`) and execution (`runner.py`).
- `annotator/model/`: Handles Ollama API interaction (`ollama_client.py`) and prompt engineering (`prompts.py`).
- `annotator/formats/`: (Extensible) Modules for exporting data in various formats (e.g., JSON, YOLO).
- `annotator/utils/`: Helper modules for file I/O, imaging, and logging.

---

## Building and Running

### Prerequisites
1.  **Ollama installed and running**: [Download Ollama](https://ollama.com/)
2.  **Pull the model**: 
    ```bash
    ollama pull llava:13b
    ```

### Installation
Install dependencies via pip:
```bash
pip install -r annotator/requirements.txt
```

### Execution
To annotate a single image:
```bash
python -m annotator.main <path_to_image>
```
Alternative (runner direct):
```bash
python -m annotator.core.runner <path_to_image>
```

---

## Development Conventions

### Coding Style
- **Modular Design**: AI logic is separated from orchestration and formatting.
- **Type Hinting**: Extensive use of Python type hints (`Dict`, `Any`, etc.).
- **Error Handling**: Graceful failure in `ollama_client.py` returning a structured error JSON instead of crashing.

### Prompt Engineering
- The system uses a strict taxonomy defined in `annotator/model/prompts.py`.
- Categories and Materials are restricted to predefined lists to ensure consistency for ML dataset generation.
- The VLM is forced to output JSON via the `format: "json"` parameter in the Ollama API.

### Testing
- Tests are located in `annotator/tests/`. 
- **TODO**: Implement comprehensive integration tests for the Ollama client and pipeline.

---

## Key Files
- `annotator/main.py`: Main entry point.
- `annotator/model/ollama_client.py`: The low-level interface to the local AI model.
- `annotator/model/prompts.py`: Defines the taxonomy and system instructions.
- `annotator/core/pipeline.py`: Coordinates the data flow from image to annotation.
