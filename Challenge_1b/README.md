# 🧠 Challenge 1B – Persona-Driven Document Intelligence

## 📘 Overview

This project addresses **Round 1B** of the Adobe "Connecting the Dots" Hackathon. The goal is to build an intelligent system that analyzes a set of documents and extracts **contextually relevant sections** based on a specific **persona** and their **job-to-be-done**.

---

## 🔧 Solution Architecture

### 1. **Section Extraction**

Implemented in `extractor.py` using `pdfplumber`:
- Parses each PDF page.
- Detects candidate section titles based on text style heuristics (Title Case or ALL CAPS).
- Associates each title with its page number and full page content.

### 2. **Semantic Relevance Ranking**

Implemented in `scorer.py` using `sentence-transformers`:
- Loads a lightweight Sentence-BERT model (`all-MiniLM-L6-v2`).
- Converts both the query (persona + job) and section content to embeddings.
- Uses cosine similarity to compute a relevance score.

### 3. **Ranking & Selection**

Implemented in `processor.py`:
- Selects top 5 sections based on relevance.
- Outputs two lists:
  - **Extracted Sections**: Ranked headings with metadata.
  - **Subsection Analysis**: Full content of those sections.

---

## 🗂️ Input/Output Structure

### 📥 Input JSON (`inputs/input.json`)
```json
{
  "documents": [
    { "filename": "example.pdf" }
  ],
  "persona": {
    "role": "Investment Analyst"
  },
  "job_to_be_done": {
    "task": "Analyze revenue trends and R&D investments"
  }
}
```

### 📤 Output JSON (`output/challenge1b_output.json`)
```json
{
  "metadata": {
    "input_documents": ["example.pdf"],
    "persona": "Investment Analyst",
    "job_to_be_done": "Analyze revenue trends and R&D investments",
    "processing_timestamp": "2025-07-27T10:00:00"
  },
  "extracted_sections": [
    {
      "document": "example.pdf",
      "section_title": "Financial Highlights",
      "importance_rank": 1,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "document": "example.pdf",
      "refined_text": "...full section content...",
      "page_number": 3
    }
  ]
}
```

---

## 🐳 Docker Instructions

### 🔨 Build the Docker Image

```bash
docker build --platform linux/amd64 -t doc-analyzer:v1 .
```

### 🚀 Run the Container

```bash
docker run --rm \
  -v $(pwd)/inputs:/app/inputs \
  -v $(pwd)/output:/app/output \
  --network none \
  doc-analyzer:v1
```

---

## 📦 Dependencies

- `pdfplumber`
- `sentence-transformers`
- `torch`
- `transformers`
- `scikit-learn`

All dependencies are installed via `requirements.txt` during Docker build.

---

## 🛡️ Constraints & Compliance

| Constraint        | Status                     |
|-------------------|----------------------------|
| CPU-only          | ✅ Supported               |
| No Internet       | ✅ Fully Offline           |
| ≤ 1GB Model Size  | ✅ Model is ~66MB          |
| ≤ 60 sec Runtime  | ✅ Optimized for speed     |

---

## 🧠 Authors & Credits

Built for Adobe India Hackathon 2025 – Challenge 1B  
Powered by Open Source: `pdfplumber`, `sentence-transformers`

---

