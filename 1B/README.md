# Round 1B — Persona Intelligence

In Round 1B, our goal is to help a specific persona achieve a job-to-be-done by finding and ranking the most relevant sections from multiple PDF documents, based on the outlines extracted in Round 1A.

---

## Methodology

We divide the pipeline into three clean, modular steps:

1. **Semantic Matching:**
   - Combine the persona and job description into a single query string.
   - Load the outline JSON files from Round 1A, which list section titles and page numbers.
   - Compute embeddings for the query and each section title using a lightweight offline embedding model (`sentence-transformers/all-MiniLM-L6-v2`), which is under 100MB.
   - Calculate cosine similarity between the query and each section to score relevance.

2. **Ranking:**
   - Sort sections by similarity score in descending order.
   - Select the top N sections (e.g., top 5) and assign `importance_rank` based on score.
   - Remove raw scores from final output for clarity.

3. **Subsection Analysis:**
   - For the top sections, optionally parse PDFs to extract related sub-sections or full text from corresponding pages.
   - Provide refined text (e.g., ingredients, instructions) in the output JSON under `subsection_analysis`.

---

## Why this approach

- **Offline-first:** No external APIs; embeddings run locally.
- **Modular:** Clear separation: semantic matching, ranking, and text extraction.
- **Efficient:** Small models keep processing under RAM/size limits.
- **Transparent:** Judges can trace why each section was picked.

---

## Output Structure

```json
{
  "metadata": { ... },
  "extracted_sections": [
    {"document": "file.pdf", "section_title": "Title", "importance_rank": 1, "page_number": 3}
  ],
  "subsection_analysis": [
    {"document": "file.pdf", "refined_text": "...", "page_number": 3}
  ]
}
```
 - Output is stored as `1b_output.json` specific for each collection.
 - Docker file is generated.

## Install dependencies
```bash 
pip install -r requirements.txt
```