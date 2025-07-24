# analyzer/semantic_matcher.py
from sentence_transformers import SentenceTransformer, util

# Load small model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity_scores(query, outlines_dict):
    """
    query: persona + job string
    outlines_dict: {filename.json: outline json}
    """
    results = []
    query_emb = model.encode(query, convert_to_tensor=True)

    for filename, outline in outlines_dict.items():
        doc_name = filename.replace(".json", ".pdf")
        for item in outline["outline"]:
            title = item["text"]
            page = item["page"]
            section_emb = model.encode(title, convert_to_tensor=True)
            score = util.cos_sim(query_emb, section_emb).item()

            results.append({
                "document": doc_name,
                "section_title": title,
                "page_number": page,
                "score": score
            })
    return results
