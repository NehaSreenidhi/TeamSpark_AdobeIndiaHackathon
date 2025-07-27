# Adobe India Hackathon 2025 — Round 2

We are `Team Spark`
This repository contains solutions for both Round 1A and Round 1B of the Adobe India Hackathon 2025.

---

## Round 1A — Outline Extractor
- Extracts structured outlines (title, H1, H2, H3, page numbers) from PDFs.
- Uses lightweight offline libraries (PyMuPDF).
- Outputs JSON outlines for use in Round 1B.

---

## Round 1B — Persona Intelligence
- Takes the outlines + persona + job description.
- Computes semantic similarity between persona/job and each section.
- Ranks the most relevant sections.
- Outputs:
  - metadata
  - extracted sections (with importance rank)
  - refined sub-section text.

---

## Project Structure of 1A
```plaintext
1A/
├── extractor
    ├── extract_text.py
    ├── heading_detector.py
    ├── json_builder.py
├── input/ (input pdf files)
├── output/ (json outputs)
├── main.py
├── requirements.txt
├── DockerFile
├── README.md


```
## Project Structure of 1A
```plain text
1B/
├── analyzer
    ├── semantic_matcher.py
    ├── ranker.py
    ├── sub_section_analysis.py
├── collections/ 
    ├── pdfs/ 
    ├── outlines/
    ├── 1b_input.json
    ├── 1b_output.json
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```