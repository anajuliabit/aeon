*HN Digest — 2026-07-28*

_open-weights day. 3 of 7 orbit anthropic's position, kimi-k3's 3T drop, and anthropic's book-shredding fallout. bun-in-rust postmortem, google's dmca loss, and a fire-cloud in france close it._

1. **[AI & agents]** [Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models) — 782 pts · 1107 comments
   Why it matters: anthropic backs open weights in principle, pushes compute/export limits on frontier training. bio and cyber flagged as red lines.
   HN take: "leveling the playing field empowers ordinary people more than governments already at the frontier. general intelligence is dual-use" — _txrx0000_
   [Discussion](https://news.ycombinator.com/item?id=49076057)

2. **[AI & agents]** [Kimi-K3 on HuggingFace](https://huggingface.co/moonshotai/Kimi-K3) — 1334 pts · 526 comments
   Why it matters: moonshot ships 3T-param mxfp4-native open weights plus tech report. largest open drop to date, sized to force a real $/MTok anchor.
   HN take: "~1.5TB of VRAM, at the limit of 8xb200s. realistically 16x for context/throughput. finally a real $/MTok anchor for a 3T model" — _NitpickLawyer_
   [Discussion](https://news.ycombinator.com/item?id=49065752)

3. **[AI & culture]** [AI companies are shredding rare books](https://twitter.com/HedgieMarkets/status/2081534588485296565) — 763 pts · 479 comments
   Why it matters: anthropic destroyed physical rare books to digitize for training, backed by a june fair-use ruling. some titles were last-copies.
   HN take: "you can reprint a bestseller. you can't replace the last three copies of an 18th-century botanical text once someone shreds them for training data" — _est31_
   [Discussion](https://news.ycombinator.com/item?id=49068738)

4. **[Infra & devtools]** [PGSimCity — How PostgreSQL Works](https://nikolays.github.io/PGSimCity/) — 901 pts · 88 comments
   Why it matters: interactive simcity-style viz of postgres internals. wal, autovacuum, buffer cache, workers. teaching aid, not a debugger.
   HN take: "why is a new process a square through a tube to a building where a pinball switch glows red? it gets lost in the sauce" — _graypegg_
   [Discussion](https://news.ycombinator.com/item?id=49063754)

5. **[Infra & devtools]** [How is the Bun rewrite in Rust going?](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) — 464 pts · 367 comments
   Why it matters: 4 months post-rewrite, commits flatlined and no user-facing release shipped. postmortem questions the token spend.
   HN take: "someone fixed the zig original with sub-second builds by modernizing the codebase. the issues that justified the rewrite were self-inflicted" — _bendmorris_
   [Discussion](https://news.ycombinator.com/item?id=49067854)

6. **[Security & policy]** [Judge rejects Google's DMCA claim against scrapers](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) — 295 pts · 118 comments
   Why it matters: court dismisses google v serpapi. search-index data isn't copyrightable, dmca doesn't reach scraping. wide read for ai training pipelines.
   HN take: "suit was filed because openai was using serpapi. alphabet is an anthropic investor. amended complaint due aug 10" — _1vuio0pswjnm7_
   [Discussion](https://news.ycombinator.com/item?id=49073513)

7. **[Science & culture]** [French firefighters face 'pyrocumulonimbus' for first time](https://www.france24.com/en/live-news/20260726-french-firefighters-face-pyrocumulonimbus-for-first-time) — 451 pts · 358 comments
   Why it matters: gironde wildfire made its own thunderstorm with self-igniting downwind lightning. 8-10 fire-storm episodes this season vs 2 in 2017's pedrogão.
   HN take: "biggest wildfire in spain: 2026. norway: 2026. germany: 2025. uk: 2025. almost every european country broke records in the same window" — _pvaldes_
   [Discussion](https://news.ycombinator.com/item?id=49060495)
