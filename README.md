# Adobe Hackathon Project – PDF Intelligence Suite

This repository contains solutions for the Adobe Hackathon, focused on extracting structured information and actionable insights from PDF documents. The project addresses two main challenges:

---

## Challenge 1a: PDF Outline Extractor

**Objective:**  
Automatically extract structured outlines (document titles and hierarchical headings) from PDF files and output the results as `.json` files.

**Key Features:**
- Processes all PDF files in the `Challenge_1a/input` directory.
- Extracts document titles and hierarchical headings (H1, H2, etc.).
- Outputs a JSON file for each PDF in the `Challenge_1a/output` directory.

**Sample Output:**
```json
{
  "title": "Extracted document title",
  "outline": [
    {
      "level": "H1",
      "text": "Heading text ",
      "page": 0
    },
    {
      "level": "H2",
      "text": "Subheading text ",
      "page": 1
    }
  ]
}
```

**How to Run:**
```sh
cd Challenge_1a
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

---

## Challenge 1b: PDF Section Relevance Extractor

**Objective:**  
Given a set of PDF documents and a user persona/task, extract and rank the most relevant sections to help the user accomplish their goal.

**Key Features:**
- Uses NLP (sentence-transformers) to semantically rank PDF sections by relevance to the persona and task.
- Outputs a summary of the top 5 most relevant sections and their refined content.
- Includes metadata about the input and processing.

**Sample Output:**  
See [`Challenge_1b/output/challenge1b_output.json`](Challenge_1b/output/challenge1b_output.json) for a full example.

**How to Run:**
```sh
cd Challenge_1b
docker build -t pdf-section-extractor:latest .
docker run --rm \
  -v $(pwd)/inputs:/app/inputs \
  -v $(pwd)/output:/app/output \
  pdf-section-extractor:latest
```

---


## Authors

Team ARuva Adobe

