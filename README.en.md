# Constitution as code — Russian Federation

Experimental, source-linked reconstruction of post-1993 constitutional text changes. Russian legal text; English research metadata. **Not a certified legal edition or a verified complete original-author history.**

## Explore

The HTML viewer has been removed. Explore the repository directly with Git.

```sh
git log --graph --oneline --all
git show amendment/16-2020-07-04
git diff amendment/16-2020-07-04^ amendment/16-2020-07-04 -- chapters/
git checkout v1.0.0-1993
```

20 amendment branches, 20 no-fast-forward merge commits, edition tags, and Markdown PR descriptions. These are **local reconstructed PRs**, not GitHub-hosted pull requests. No remote repository has been created.

## Scope and status

The replay covers the 20 instruments represented here: five renaming decrees, five regional mergers, five Article 136 amendment laws (including the entire 2020 package), and five territorial-insertion instruments (one in 2014 and four in 2022). The final represented legal changes date to 2022. **No comprehensive search for changes through 21 October 2026 has been completed.** Unsuccessful bills and intermediate bill drafts are not represented.

The 2020 package is one PR with article-level diffs, not a fictional sequence of separately enacted changes. Four 2022 instruments are ordered by law number for inspection; that ordering is analytical, not proof of four successive published constitutional editions.

## Attribution and integrity

All Git authors/committers are the research reconstruction identity. Real politicians did not make these commits. Metadata distinguishes signatory/issuing president from bill initiative; unknown initiators are explicitly marked. Attribution of every individual clause to its original human drafter is **unfinished**. A signatory is not necessarily the author. Individual 2020 contributions require legislative dossier research, including amendments introduced after the presidential bill.

Dates encode text-change/formation/publication dates where identified. Early decrees sometimes use instrument dates and are marked pending effective-date verification in each PR. Git dates are synthetic noon timestamps, not archival timestamps. Initial baseline adopted 12 December 1993, effective 25 December.

## Text and provenance

`CONSTITUTION.md` is a generated combined text; `chapters/` contains the same text split by chapter. Count only chapter files when measuring legal changes to avoid double counting. Five inserted article numbers use decimal plain-text notation (67.1 etc.); superscript paragraph/letter labels are also normalized to decimal notation. Typography, blank lines, footnotes, and link markup have been normalized.

Transcriptions were retrieved from Russian Wikisource on 21 October 2026. Files under `sources/` preserve raw wikitext used in the experiment; they are secondary transcriptions, not primary promulgation records. The 1993 baseline is reconstructed by reversing later changes, not taken from a certified scan. The original snapshot `rev_1478` has known typographical problems and is retained for provenance, not treated as authoritative. Article 46 and punctuation normalization follow the later consolidated transcription. Source transcriptions can themselves contain errors.

See `SOURCES.md` for URLs and `METHODOLOGY.md` for review limits. Primary-source and legislative-dossier verification is needed before using this as a legal database.

## Territorial status

Article 65 insertions describe the Russian domestic text only. They do not endorse Russia's territorial claims. Crimea, Sevastopol, and the four Ukrainian regions claimed in 2022 are internationally recognized as parts of Ukraine. Consult UN General Assembly resolutions 68/262 and ES-11/4, linked in SOURCES.md.

## Verification

Run `python3 tools/verify.py`. This checks branch/merge counts and that stored article diffs match actual Git chapter changes. These are engineering consistency checks, **not legal certification**.
