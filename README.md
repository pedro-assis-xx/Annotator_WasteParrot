# Annotator_WasteParrot

A modular Python pipeline for automated image annotation using a local vision-language model.

---

## Overview

Annotator is a tool that automatically converts raw images into structured annotations using a local vision-language model. It is designed for dataset generation in machine learning workflows.

The system processes images, generates labels using AI, and exports structured datasets in multiple formats.

---

## Key Features

- Automated image annotation pipeline
- Local inference using Ollama + LLaVA (no cloud dependency)
- Structured outputs (JSON / YOLO)
- Config-driven prompts and categories

---

## Model Setup

This project uses:

- Ollama (local model server)
- LLaVA (vision-language model)

The model runs locally at:

http://localhost:11434

No external API keys are required.

---

## Project Structure

annotator/
├── main.py
├── config.json
├── requirements.txt
├── core/
│ ├── runner.py
│ ├── pipeline.py
│ ├── processor.py
├── model/
│ ├── ollama_client.py
│ ├── prompts.py
├── formats/
│ ├── json.py
│ ├── yolo.py
├── utils/
│ ├── file_io.py
│ ├── image_utils.py
│ ├── logger.py


---

## How It Works

1. Load images from input folder
2. Send each image to LLaVA via Ollama API
3. Model returns structured prediction
4. Output is parsed and validated
5. Results are saved in selected format

---

## Output Format Example (JSON)

```json
{
  "category": "Reclosable Bag",
  "material": "polyethylene",
  "caption": "A reclosable bag on the ground"
}

Requirements

Install dependencies:
	pip install -r requirements.txt

Run
	python main.py

Notes
Requires Ollama running locally before execution
Designed for single-machine dataset generation
Optimized for research and prototyping workflows
