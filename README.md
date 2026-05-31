# malawi-bench

**African Legal AI Benchmark** — evaluating LLM legal reasoning across African jurisdictions.

LegalBench (NeurIPS 2023) explicitly acknowledges it "skews towards US Federal law," has "no multilingual or non-English tasks," and excludes other jurisdictions. Harvey's LAB (2026) is also US/UK focused. No benchmark exists for any of Africa's 54 jurisdictions.

malawi-bench fills that gap.

## Scope (Phase 1)

| Jurisdiction | Legal System | Languages | Status |
|---|---|---|---|
| Nigeria | Common law + Customary + Sharia | English + 400+ | Planning |
| South Africa | Roman-Dutch + English + Customary | 11 official | Planning |
| Kenya | Common law + Customary + Islamic | English, Swahili | Planning |

## Task categories

- Statute interpretation & retrieval
- Case citation verification
- Customary law reasoning
- Multilingual statute retrieval
- Long document understanding
- Multi-jurisdictional citation analysis

## Structure

```
tasks/          — Task definitions (JSON, LegalBench-compatible)
data/           — Raw and processed datasets
scripts/        — Data collection and annotation pipelines
docs/           — Methodology and jurisdiction notes
notebooks/      — Exploratory analysis
```

## License

Apache 2.0
