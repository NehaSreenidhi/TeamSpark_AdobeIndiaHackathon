# extractor/extract_text.py
import fitz  # PyMuPDF

def extract_text_blocks(pdf_path):
    """
    Extract text blocks from PDF with text, font size, font name, page number.
    Returns: list of dicts
    """
    doc = fitz.open(pdf_path)
    blocks = []

    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("dict")["blocks"]:
            # Blocks can have multiple lines/spans
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    if text:  # skip empty
                        blocks.append({
                            "text": text,
                            "font_size": span.get("size", 0),
                            "font_name": span.get("font", ""),
                            "flags": span.get("flags", 0),
                            "page": page_num
                        })
    return blocks
