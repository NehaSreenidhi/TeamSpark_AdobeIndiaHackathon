# main.py
import os
import json
from datetime import datetime
from analyzer.semantic_matcher import compute_similarity_scores
from analyzer.ranker import rank_sections
from analyzer.sub_section_analysis import get_subsection_analysis

def process_collection(collection_path):
    # Load 1b_input.json
    with open(os.path.join(collection_path, "1b_input.json"), encoding="utf-8") as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    combined_query = f"{persona}: {job}"

    # Load outlines
    outlines_dir = os.path.join(collection_path, "outlines")
    outlines = {}
    for filename in os.listdir(outlines_dir):
        if filename.endswith(".json"):
            with open(os.path.join(outlines_dir, filename), encoding="utf-8") as f:
                outlines[filename] = json.load(f)

    # Step 1: semantic similarity scores
    scored_sections = compute_similarity_scores(combined_query, outlines)

    # Step 2: rank
    extracted_sections = rank_sections(scored_sections, top_n=5)

    # Step 3: subsection analysis
    pdfs_dir = os.path.join(collection_path, "pdfs")
    subsection_analysis = get_subsection_analysis(pdfs_dir, extracted_sections)

    # Step 4: build final output
    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    # Step 5: write output
    output_path = os.path.join(collection_path, "1b_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"✅ Created {output_path}")

def main():
    # Find all collection folders and process
    for folder in os.listdir("."):
        if folder.startswith("collection") and os.path.isdir(folder):
            print(f"🔍 Processing {folder}")
            process_collection(folder)

if __name__ == "__main__":
    main()
