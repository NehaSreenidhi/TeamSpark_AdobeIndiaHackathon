# main.py
import os
from extractor.extract_text import extract_text_blocks
from extractor.heading_detector import detect_headings
from extractor.json_builder import build_json, write_json

# INPUT_DIR = "/app/input" if os.path.exists("/app/input") else "input"
# OUTPUT_DIR = "/app/output" if os.path.exists("/app/output") else "output"
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def process_pdf(pdf_filename):
    pdf_path = os.path.join(INPUT_DIR, pdf_filename)
    print(f"Processing: {pdf_filename}")
    blocks = extract_text_blocks(pdf_path)
    title, outline = detect_headings(blocks)
    data = build_json(title, outline)
    json_filename = os.path.splitext(pdf_filename)[0] + ".json"
    output_path = os.path.join(OUTPUT_DIR, json_filename)
    write_json(data, output_path)
    print(f"Output written: {json_filename}")

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
    for pdf in pdf_files:
        process_pdf(pdf)

if __name__ == "__main__":
    main()
