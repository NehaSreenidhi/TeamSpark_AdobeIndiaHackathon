# analyzer/sub_section_analysis.py
def get_subsection_analysis(pdfs_dir, extracted_sections):
    results = []
    for sec in extracted_sections:
        text = f"Refined text for section: {sec['section_title']}"
        results.append({
            "document": sec["document"],
            "refined_text": text,
            "page_number": sec["page_number"]
        })
    return results
