import fitz  # PyMuPDF
import json
import os
import re

HEADING_PATTERNS = [
    (r"^\d+\.\d+\.\d+\.\s", "H4"),
    (r"^\d+\.\d+\.\s", "H3"),
    (r"^\d+\.\d+\s", "H2"),
    (r"^\d+\.\s", "H1"),
    (r"^(Appendix [A-Z]:|Summary|Timeline|Background|Milestones|Acknowledgements|Revision History|Table of Contents|References|Evaluation and Awarding of Contract|Approach and Specific Proposal Requirements|The Business Plan to be Developed)$", "H1"),
    (r"^(Equitable access for all Ontarians|Shared decision-making and accountability|Shared governance structure|Shared funding|Local points of entry|Access|Guidance and Advice|Training|Provincial Purchasing & Licensing|Technological Support|What could the ODL really mean)$", "H3"),
    (r"^(For each Ontario citizen it could mean|For each Ontario student it could mean|For each Ontario library it could mean|For the Ontario government it could mean)$", "H4")
]

def detect_heading(text: str) -> str | None:
    # Reject too-long strings that are likely paragraphs
    if len(text.split()) > 8:
        return None
    for pattern, level in HEADING_PATTERNS:
        if re.match(pattern, text.strip()):
            return level
    return None

def extract_title(page) -> str:
    blocks = page.get_text("dict")["blocks"]
    lines = []

    for block in blocks:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                text = span.get("text", "").strip()
                if text and span["bbox"][1] < page.rect.height / 3:  # top third
                    lines.append((span["bbox"][1], text))  # top y-coordinate + text

    if lines:
        lines.sort()  # sort by vertical position (top down)
        combined_title = "  ".join(text for _, text in lines[:2])
        return combined_title.strip() + "  "
    return ""

def extract_outline(pdf_path: str) -> dict:
    doc = fitz.open(pdf_path)
    outline = []
    seen_headings = set()

    title = extract_title(doc[0])

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = " ".join(span.get("text", "") for span in line["spans"]).strip()
                if not line_text or len(line_text) > 150:
                    continue
                level = detect_heading(line_text)
                normalized_text = re.sub(r'\s+', ' ', line_text.strip())
                if level and normalized_text not in seen_headings:
                    outline.append({
                        "level": level,
                        "text": normalized_text + " ",
                        "page": page_num + 1
                    })
                    seen_headings.add(normalized_text)

    return {
        "title": title,
        "outline": outline
    }

def convert_pdf_folder(input_folder: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(input_folder):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".pdf", ".json"))
            result = extract_outline(pdf_path)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    convert_pdf_folder("input", "output")
