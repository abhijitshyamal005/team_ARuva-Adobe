# 📄 Approach Explanation – Challenge 1B

## 🔍 Objective

The goal of this challenge is to extract and prioritize the **most relevant sections** from a set of documents based on a **given persona** and their **job-to-be-done**. Our solution mimics an intelligent document analyst that interprets and selects contextually meaningful content tailored to the user's role and task.

---

## 🧠 Methodology

### 1. **Section Extraction (extractor.py)**

We use **pdfplumber**, a lightweight and efficient PDF parsing library, to extract text from each page. The extracted text is heuristically parsed to detect potential section headers. A line is considered a potential heading if:
- It has a character length between 8 and 100, and
- It appears in **Title Case** or **ALL CAPS**, suggesting it might be a heading.

For each such line, we store:
- The heading as `title`
- The full page text as `content`
- The source filename and page number

This simple yet robust heuristic works reasonably well across a variety of document styles without relying on font metadata, ensuring broader generalization.

---

### 2. **Relevance Ranking (scorer.py)**

We leverage the **Sentence-BERT** model `all-MiniLM-L6-v2` from `sentence-transformers` to perform semantic similarity matching. A query is dynamically generated from the persona and job description:

## **Persona needs to : Job to be done


This query is embedded and compared to the embedding of each extracted section using **cosine similarity** via `pytorch_cos_sim`. Each section receives a relevance score based on this similarity, capturing both context and intent.

---

### 3. **Section Prioritization (processor.py)**

The top 5 sections are selected based on descending similarity scores. Two structured outputs are produced:
- **Extracted Sections**: Metadata including section title, document name, rank, and page number.
- **Subsection Analysis**: Detailed content (`refined_text`) of the selected sections for deeper understanding or downstream applications.

The results are serialized to a JSON file with an additional timestamp for traceability.

---

## 🚀 Why This Works

- **Generalization**: Our rule-based heading detection is document-agnostic and avoids hardcoding formats or font features.
- **Offline & Lightweight**: The solution uses a 66MB SBERT model and complies with all offline and CPU-only constraints.
- **Modular Design**: The codebase is cleanly separated into extraction, processing, and scoring modules, enabling future extensibility (e.g., integrating more advanced NLP models or PDF layouts).
- **Context-Aware**: Embedding-based ranking captures nuanced relationships between persona intent and document content.

---

## ✅ Compliance & Optimization

- ✔️ Runs within 60 seconds for 3–5 documents.
- ✔️ Model size: 66MB (< 1GB).
- ✔️ CPU-only and network-disabled Docker container.
- ✔️ Outputs compliant with the expected JSON schema.

---
