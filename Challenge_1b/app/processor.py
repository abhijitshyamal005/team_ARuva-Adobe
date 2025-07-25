import os
from app.extractor import extract_sections
from app.scorer import rank_sections

def process_documents(input_data):
    documents = input_data["documents"]
    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    files_path = "inputs/documents"

    all_sections = []

    for doc in documents:
        filename = doc["filename"]
        path = os.path.join(files_path, filename)
        extracted = extract_sections(path, filename)
        all_sections.extend(extracted)

    # Rank by relevance
    ranked = rank_sections(all_sections, persona, job)

    # Select top 5
    top_sections = sorted(ranked, key=lambda x: x["score"], reverse=True)[:5]

    extracted_sections = []
    subsection_analysis = []

    for rank, item in enumerate(top_sections, 1):
        extracted_sections.append({
            "document": item["document"],
            "section_title": item["title"],
            "importance_rank": rank,
            "page_number": item["page"]
        })
        subsection_analysis.append({
            "document": item["document"],
            "refined_text": item["content"],
            "page_number": item["page"]
        })

    return {
        "metadata": {
            "input_documents": [d["filename"] for d in documents],
            "persona": persona,
            "job_to_be_done": job
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
