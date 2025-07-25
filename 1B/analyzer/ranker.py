# analyzer/ranker.py
def rank_sections(scored_sections, top_n=5):
    sorted_sections = sorted(scored_sections, key=lambda x: x["score"], reverse=True)
    top_sections = sorted_sections[:top_n]
    for i, sec in enumerate(top_sections, start=1):
        sec["importance_rank"] = i
        del sec["score"]  # remove raw score from final JSON
    return top_sections
