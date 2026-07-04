# Social Determinants of Health (SDoH) Extraction from Clinical Notes using NLP

## Overview
This project implements an automated Natural Language Processing (NLP) system to extract **Social Determinants of Health (SDoH)** from unstructured clinical notes. The system identifies social factors such as housing, employment, transportation, income, education, substance use, and social support, then recommends relevant healthcare and community resources to support clinical decision-making.

---

## Workflow
- Input clinical notes
- Text normalization (case-insensitive processing)
- Rule-based keyword matching
- SDoH category detection (21 categories)
- Resource mapping for detected social needs
- Generate human-readable and JSON-formatted outputs

---

## Features
- Extracts 21 Social Determinants of Health (SDoH) categories
- Rule-based NLP keyword detection
- Provides healthcare and community support recommendations
- Generates structured JSON output
- Lightweight Python implementation
- Easy to extend with Machine Learning and Large Language Models (LLMs)

---

## Technologies Used
- Python 3.x
- Natural Language Processing (NLP)
- JSON
- VS Code
- Windows PowerShell

---

## Files in this Repository
- `main.py` – Main program execution
- `Rules_solution.py` – SDoH knowledge base and resource mapping
- `requirements.txt` – Required Python libraries
- `README.md` – Project documentation

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Output
The system identifies SDoH factors from clinical notes and generates:
- Human-readable report
- JSON-formatted structured output
- Recommended healthcare and community support resources

---

## Project Documents
- **Project Report:** `project report.pdf`
- **Project Presentation:** `project presentation.pptx`

---

## Future Work
The project can be enhanced by integrating Machine Learning and Large Language Models (LLaMA, ClinicalBERT), supporting multilingual clinical notes, connecting with Electronic Health Record (EHR) systems, storing historical patient data, and developing a web-based dashboard for healthcare professionals.

---

## Authors
- G. Tejaswi
- K. Pranitha
- S. Surekha
- S. Pavankumar
