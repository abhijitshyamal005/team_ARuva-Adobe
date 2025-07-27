# 🧠 PDF Outline Extractor

A lightweight tool to extract structured outlines (document titles and hierarchical headings) from PDF files using **PyMuPDF**. The extracted data is exported as a `.json` file for each PDF.

## 🚧 Build Instructions

Run the following command to build the Docker image:

```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

## 🚀 Run Instructions

To execute the solution, use:

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier
```

✅ **Expected Behavior**:
- All PDFs inside `/app/input` will be automatically processed.
- For every `filename.pdf`, a corresponding `filename.json` will be saved inside `/app/output`.

## 📁 Example Output

For a file named `example.pdf`, the output `example.json` will look like:

```json
{
  "title": "Extracted Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Heading 1",
      "page": 1
    },
    {
      "level": "H2",
      "text": "Subheading 1.1",
      "page": 2
    }
  ]
}
```

## 📋 Constraints

| Constraint             | Requirement                            |
|------------------------|----------------------------------------|
| Execution Time         | ≤ 10 seconds for a 50-page PDF         |
| Model Size (if any)    | ≤ 200MB                                |
| Network                | ❌ No internet access allowed           |
| Runtime Environment    | CPU only (amd64, 8 CPUs, 16 GB RAM)    |

## 🔧 Approach

### 📄 PDF Parsing:
- Uses **PyMuPDF** to extract text, font styles, sizes, and positions.
- Applies **custom heuristics** to detect headings based on:
  - Font size and weight
  - Relative positioning
  - Text formatting

### 🧱 Output Format:
- JSON output per PDF.
- Includes:
  - Extracted title
  - Structured heading hierarchy with levels (H1, H2, etc.)
  - Page numbers

### ⚡ Performance:
- Optimized to process medium-sized PDFs (~50 pages) in **under 10 seconds**.
- All dependencies pre-installed inside the container for fast, offline execution.

## 📦 Dependencies

- `PyMuPDF`: For text extraction and layout analysis  
- Installed via `requirements.txt` during image build

## 🐳 Dockerfile Summary

- **Base image:** `python:3.11-slim`
- **Steps:**
  - Install Python dependencies
  - Copy application source code
  - Set `main.py` as the container entrypoint

## ✅ Submission Checklist

- [x] Dockerfile in root directory  
- [x] Functional solution with tested `.json` output  
- [x] All required dependencies installed in container  
- [x] Self-contained execution without internet  
- [x] This well-structured `README.md` included in repo
