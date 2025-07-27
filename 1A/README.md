# Round 1A — PDF Outline Extractor

This module extracts structured outlines (title, headings with page numbers) from PDF documents, without internet access.

---

## Approach

- Parse PDFs using `PyMuPDF (fitz)` to get text blocks, font sizes, styles, and positions.
- Use font size clustering and heuristic rules to detect heading hierarchy (H1, H2, H3).
- Extract document title as the largest top-centered text on the first page.
- Build a JSON outline containing:
  - title
  - outline list: section titles, levels, and page numbers.

- Output.json is produced as instructed.
- Docker file also generated

---

## Models & Libraries Used

- Python
- PyMuPDF (`fitz`) — PDF parsing and text block extraction.

---

## Install dependencies
```bash 
pip install -r requirements.txt
```
