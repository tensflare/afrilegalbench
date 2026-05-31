# Methodology

## Overview

malawi-bench follows the same methodology as LegalBench (NeurIPS 2023) to ensure compatibility and comparability. Each task is a curated set of input-output pairs designed to test a specific legal reasoning capability.

## Task construction

1. **Source identification** — identify authoritative legal documents (statutes, case law, legal textbooks) for the target jurisdiction.
2. **Passage extraction** — extract relevant passages from source documents.
3. **Annotator task creation** — legal professionals (law students, junior lawyers) write natural language questions and expected answers.
4. **Quality review** — second annotator validates a 20% sample. Inter-annotator agreement (Fleiss' kappa) must exceed 0.8.

## Reasoning categories

See LegalBench taxonomy (6 categories) plus 4 additional categories for African legal contexts.

## Data sources

- SAFLII (Southern African Legal Information Institute) — free, open access
- NigeriaLII — free, open access
- KenyaLII — free, open access
- LawPavilion — commercial Nigerian legal research platform
- National statute repositories (public domain)

## Evaluation metrics

Following LegalBench: accuracy per task, macro-average across tasks, and breakdown by reasoning category and jurisdiction.
