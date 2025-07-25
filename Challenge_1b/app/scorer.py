from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    query = f"{persona} needs to: {job}"
    query_emb = model.encode(query, convert_to_tensor=True)

    for section in sections:
        section_emb = model.encode(section["content"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(query_emb, section_emb).item()
        section["score"] = score

    return sections
