# AfriLegalBench

Evaluating LLM legal reasoning across African jurisdictions.

## The gap

Existing legal benchmarks (LegalBench, NeurIPS 2023; Harvey's LAB, 2026) are built on US and UK law. Neither covers Africa's 54 jurisdictions, pluralistic legal systems, or multilingual proceedings. LegalBench explicitly notes it "skews towards US Federal law" and includes "no multilingual or non-English tasks."

AfriLegalBench addresses this gap — a structured evaluation suite for legal reasoning in African legal contexts.

## Scope (Phase 1)

| Jurisdiction | Legal system | Languages | Status |
|---|---|---|---|
| Nigeria | Common law, Customary, Sharia | English + 400+ | Live — 20 tasks, 62 examples |
| South Africa | Roman-Dutch, English, Customary | 11 official | Live — 7 tasks, 20 examples |
| Kenya | Common law, Customary, Islamic | English, Swahili | Live — 6 tasks, 17 examples |

## Reasoning categories

Following LegalBench's taxonomy (6 categories) plus four additions for African legal contexts:

- **Statute interpretation & retrieval** — given a fact pattern, identify and apply the relevant statute
- **Case citation verification** — does a cited case stand for the proposition attributed to it?
- **Customary law reasoning** — how would this dispute be resolved under applicable customary law?
- **Multilingual statute retrieval** — given a query in one language, find the relevant statute in another
- **Long document understanding** — clause detection in full judgments (50+ pages)
- **Multi-jurisdictional citation analysis** — when does a court cite foreign precedent?
- **Legal system identification** — does this fact pattern fall under common law, customary law, or Sharia?
- **Analogical reasoning** — is case A analogous to case B within or across jurisdictions?

## Task format

Each task is a JSON file conforming to the [task schema](tasks/task_schema.json) and compatible with LegalBench evaluation pipelines:

```json
{
  "task_name": "nigeria-customary-inheritance",
  "jurisdiction": "nigeria",
  "legal_system": ["common_law", "customary_law"],
  "reasoning_type": "rule_application",
  "dataset": [
    {
      "id": "ng-custom-001",
      "input": "...",
      "target": "...",
      "source": "Supreme Court of Nigeria, ..."
    }
  ]
}
```

## Data sources

- SAFLII (Southern African Legal Information Institute) — open access case law
- NigeriaLII — open access case law and legislation
- KenyaLII — open access case law and legislation
- National statute repositories (public domain)

## Repository structure

```
tasks/          — task definitions (JSON, LegalBench-compatible)
data/           — raw and processed datasets
scripts/        — data collection and annotation pipelines
docs/           — methodology, jurisdiction notes
notebooks/      — exploratory analysis
```

## License

Apache 2.0
