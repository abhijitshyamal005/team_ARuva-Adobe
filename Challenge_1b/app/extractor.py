import pdfplumber

def extract_sections(pdf_path, doc_name):
    sections = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            # Simple rule: split sections by headers (e.g. lines in ALL CAPS or Title Case)
            lines = text.split('\n')
            for line in lines:
                if 8 < len(line) < 100 and (line.istitle() or line.isupper()):
                    section_text = text  # you could extract more precisely with NLP
                    sections.append({
                        "document": doc_name,
                        "title": line.strip(),
                        "content": section_text,
                        "page": i + 1
                    })
    return sections
