# extractor/heading_detector.py

from collections import Counter

def detect_headings(blocks):
    """
    Improved: detect title, assign heading levels.
    """
    if not blocks:
        return "", []

    # Count most common font sizes (after rounding)
    sizes = [round(b["font_size"]) for b in blocks if b["font_size"] > 0]
    common = Counter(sizes).most_common()

    # Assign levels: largest freq size → normal text, larger ones → headings
    sorted_sizes = sorted({s for s, _ in common}, reverse=True)
    if len(sorted_sizes) < 1:
        return "", []

    # Title = largest size text on first page
    title = ""
    for b in blocks:
        if round(b["font_size"]) == sorted_sizes[0] and b["page"] == 1:
            title = b["text"].strip()
            break

    outline = []
    for b in blocks:
        text = b["text"].strip()
        if len(text) <= 1 or text.isdigit() or text in {"-", "."}:
            continue  # skip junk

        size = round(b["font_size"])
        page = b["page"]

        if size == sorted_sizes[0] and text != title:
            level = "H1"
        elif len(sorted_sizes) > 1 and size == sorted_sizes[1]:
            level = "H2"
        elif len(sorted_sizes) > 2 and size == sorted_sizes[2]:
            level = "H3"
        else:
            continue

        outline.append({"level": level, "text": text, "page": page})

    return title, outline

