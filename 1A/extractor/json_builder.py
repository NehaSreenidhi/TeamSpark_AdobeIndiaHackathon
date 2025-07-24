# extractor/json_builder.py
import json

def build_json(title, outline):
    return {
        "title": title,
        "outline": outline
    }

def write_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
