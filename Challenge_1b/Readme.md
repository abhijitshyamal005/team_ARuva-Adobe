# 🧠 Persona-Driven Document Intelligence System

## 📌 Challenge Overview
This project is built for **Round 1B: “Connect What Matters — For the User Who Matters”** of the Document Intelligence Challenge.

Your task is to build an intelligent system that:
- Understands a **persona** (e.g., Travel Planner)
- Understands a **job-to-be-done** (e.g., Plan a 4-day trip)
- Analyzes a collection of **PDF documents**
- Extracts, prioritizes, and refines the most **relevant sections**
- Outputs in a **predefined JSON format**

---

## 📁 Project Structure

persona_doc_intelligence/
├── app/ # Core logic modules
│ ├── processor.py # Main logic to orchestrate extraction + scoring
│ ├── extractor.py # PDF text + section extraction
│ ├── scorer.py # Embedding similarity-based ranking
│ └── utils.py # Utility functions
├── inputs/
│ ├── input.json # Persona + Job + Document metadata
│ └── documents/ # All input PDFs here
├── output/
│ └── challenge1b_output.json # Final output JSON
├── models/ # (Optional) Pre-downloaded transformer model
├── wheels/ # Pre-downloaded .whl files (e.g. torch)
├── requirements.txt # Python dependencies (excluding torch)
├── Dockerfile # Docker build instructions
├── main.py # Entry point for processing
└── README.md # This file

yaml
Copy
Edit

---

## 🔧 Requirements

- Python 3.10+
- Docker (Recommended for isolated execution)
- CPU-only model under 1GB
- No internet access at runtime

---

## 🛠️ Installation & Usage

### 🐳 Docker Instructions

#### Step 1: Pre-download `torch` CPU `.whl` manually
Put it in `wheels/`, e.g.

```bash
./wheels/torch-2.1.2+cpu-cp310-cp310-linux_x86_64.whl
Step 2: Build Docker image
bash
Copy
Edit
docker build -t doc-analyzer .
Step 3: Run the container
bash
Copy
Edit
docker run --rm -v "$(pwd)/inputs":/app/inputs -v "$(pwd)/output":/app/output doc-analyzer
✅ This generates output/challenge1b_output.json.

✅ Input Format (inputs/input.json)
json
Copy
Edit
{
  "challenge_info": {
    "challenge_id": "round_1b_002",
    "test_case_name": "travel_planner",
    "description": "France Travel"
  },
  "documents": [
    { "filename": "South of France - Cities.pdf", "title": "South of France - Cities" },
    ...
  ],
  "persona": {
    "role": "Travel Planner"
  },
  "job_to_be_done": {
    "task": "Plan a trip of 4 days for a group of 10 college friends."
  }
}
✅ Output Format (output/challenge1b_output.json)
json
Copy
Edit
{
  "metadata": {
    "input_documents": [...],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a trip of 4 days...",
    "processing_timestamp": "2025-07-25T10:22:00.000Z"
  },
  "extracted_sections": [
    {
      "document": "...",
      "section_title": "...",
      "importance_rank": 1,
      "page_number": 2
    },
    ...
  ],
  "subsection_analysis": [
    {
      "document": "...",
      "refined_text": "...",
      "page_number": 2
    },
    ...
  ]
}
🧠 Approach Summary
PDF text is extracted page-wise using pdfplumber.

Heuristics are applied to identify potential section headers.

Each section is embedded using sentence-transformers (MiniLM-L6-v2).

Cosine similarity is calculated between section embedding and the persona + job context.

Top 5 relevant sections are selected and written in the required JSON schema.

Detailed explanation is available in approach_explanation.md.