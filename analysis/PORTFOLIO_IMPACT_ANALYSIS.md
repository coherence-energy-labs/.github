# Coherence Energy Labs — Portfolio Impact Analysis

**Question asked:** Across every repository in the `coherence-energy-labs` org, which single project — if finished — would have the most impact on changing the world *if people knew it existed and understood the possibilities*? Not the closest to done. The highest ceiling, made real.

**Method:** All 47 repositories were cloned and read. Seven independent deep-analysis passes covered the whole estate — core language/compiler, AI systems, provenance/verification, comms/crypto, applied science, the quantum/ONE-Q cluster, and the theory/legacy tail. Two of those passes *independently re-derived the estate's central claims from scratch on foreign hardware* rather than trusting the repos' own reports. The org's own conservation-challenge and re-executable banner were re-run and verified locally.

**Date:** 2026-08-19

---

## TL;DR — the converged ruling

The original ask collapsed three questions; separating them ended the debate, and after three challenge rounds (§5b, §10) two independent analyses converged on the same structure:

- **What to finish first: `Obsign` + `obsign_verifier`.** Across 47 repositories the same invention reappears under thirteen names — a **deterministic, signed, independently re-runnable receipt** — and Obsign is its most generalized, productized, deliberately outsider-facing expression: shipped to public registries, with a public stranger-verifier, its central claim re-derived from scratch during this audit and confirmed byte-for-byte. Finishing it creates the **credibility distribution layer for everything else the estate builds**: ONE-Q results, VMP computations, LumOne answers, Discovery Engine predictions — all become "Obsign it, then let disbelief become irrelevant."
- **The deepest mechanism ceiling: VMP's minimum-sufficient verified computation** — *question → unresolved information → minimum sufficient work → proof*. Measured today (§5b), paradigm-scale if generalized.
- **The largest single deployment of that mechanism: LumOne**, at the committing boundary of AI — every answer PROVED with a warrant, REFUTED with a witness, or UNKNOWN with a signed certificate of ignorance (§10).

One architecture, three altitudes: **Obsign is the doorway, VMP is the engine, LumOne is the flagship deployment.** The unifying systems pattern: *large untrusted intelligence → small truth-bearing computation → minimum-sufficient execution → independent receipt.* The expensive, probabilistic thing stays probabilistic; the committing boundary becomes deterministic and verifiable.

Sections 1–9 are the evidence base, preserved intact; §10 records the challenge rounds, the convergence, and three corrections adopted from the owner's review.

---

## 1. What "impact if they knew" actually demands

The instinct is to rank by ceiling — how big is the problem the project addresses. That is necessary but not sufficient. A claim that would change the world *only if believed* changes nothing when revealed if the world cannot check it; it gets filed next to every other grand claim and discounted. So the real objective function has four multiplicative terms, gated by a fifth:

```
Impact("if they knew")  =  Ceiling  ×  Credibility  ×  Counterfactual-uniqueness  ×  Adoption-reach
                           ────────────────────────────────────────────────────────────────────
                                              gated by  Finishability
```

- **Ceiling** — how large is the problem, and how many domains does solving it touch.
- **Credibility** — can a skeptical expert *verify* it today, without trusting the author. This is the term the estate systematically under-weights in its marketing and over-delivers on in its code.
- **Counterfactual-uniqueness** — does this already exist elsewhere. Novelty the field would actually notice, not novelty of framing.
- **Adoption-reach** — can strangers actually use it, or is it welded to a private workstation.
- **Finishability** — can the remaining gap realistically be closed, and does it depend on things that are themselves unfinished.

The genius move the question is really asking for is to find the project where these terms *multiply* rather than trade off — where finishing it is tractable, the result is checkable, the capability is genuinely new, and the problem is civilizational. Most of the portfolio maxes one term and zeroes another (HazardPulse: highest ceiling, currently-negative credibility; ONE-Q: highest credibility, narrow ceiling; ACE: largest artifact, near-zero uniqueness). Obsign is the one where all four terms are simultaneously positive and finishability is high.

---

## 2. The meta-finding: the estate's real asset is not the physics

The org's public thesis is "one field equation, `(D·L + κ²I)τ = s`, from bare metal to cosmology." **Every one of the seven analyses independently concluded that this framing is branding, not load-bearing.** Delete the field equation from ONE-Q and every certificate still verifies. In HazardPulse the PDE is a *feature generator* feeding gradient-boosted trees, not the predictor. In Obsign, omega_one, the covenant, glasshouse, and the proof fabric the "coherence" story is explicitly disclaimed in the code as narrative. In `onefield-mesh` the physics is worse than decorative — it is *wrong* (a load-bearing constant is dimensionally `√(m/s)` used as a velocity, and a MOND galactic-acceleration scale is used to set a radio link budget).

What is genuinely, repeatedly, and defensibly present instead is a **research-integrity and verifiable-computation discipline** that is more mature than any of the science it governs. It shows up, independently reinvented, in at least fourteen repos:

- machine-readable **claim ledgers** where a public number without a backing artifact fails the build (`cel/claims-ledger.json`, `loo/evidence/claims.json`, `vmp/claim_registry`, `cpf/spec/PROVEN_VS_RESEARCH.md`);
- **CI that gates the gates** — mutation-testing the checkers themselves, so "a gate that cannot fail is not a gate" (`loo/scripts/metagate.py`, `glasshouse` mutation gate, `cpf` hermetic-gate-with-forced-REJECT);
- **published self-refutations** — retraction indices and falsification libraries kept dated and preserved (`vmp/artifacts/RETRACTED.json`, ACE's from-code ledger correcting the author in both directions, omega_one walking back its own single-seed result);
- and one primitive above all: the **0-ULP deterministic, signed, independently re-runnable receipt** — *re-derivation, not certificate trust*.

omega_one states the lesson outright in its own self-teardown: **"Do not sell the theory; sell the receipt."** The estate has, unknowingly, already converged on its own answer. Obsign is that answer, extracted and made public.

One refinement, adopted after review (§10): "not load-bearing" is a statement about *evidence*, not about *worth*. That the verified results survive with the physics deleted proves the verification architecture is independently valuable — it does not prove the physics is valueless. The physics is an open research program, and the correct path for it is the one the doctrine itself prescribes: don't ask anyone to believe the framework first; hand them something the framework produced that they can independently prove is real, and let them come asking what's underneath.

---

## 3. The decision: Obsign

**What it is.** Obsign builds and verifies *re-executable computation receipts*. A receipt is a small signed JSON object naming a kernel, its inputs, and the SHA-256 of its output. The guarantee is not "a trusted party attests this happened" — it is "re-run this yourself and you get the identical bytes." Determinism is achieved by doing the computation in integer fixed-point (`int64`), so it is bit-identical on every CPU, GPU, WASM runtime, and browser. The public half, `obsign_verifier`, ships a tiny deterministic integer VM whose program travels *inside* the receipt, small enough to re-implement from its docstring in about twenty minutes, and in which nondeterminism is not restricted but *inexpressible* — no clock, no RNG, no I/O, no float, anywhere.

**Why it wins on each term of the model:**

- **Credibility — the highest in the estate.** An independent analysis pass reimplemented Obsign's kernel from the spec, with no producer code, on a different OS / CPU / Python than the producer, and re-derived both a PDE receipt *and* a 27-instruction IFRS-9/CECL credit-loss receipt bit-for-bit. All sixteen forgery bundles were correctly refused. Critically, the `resealed_tampered_claim` case — signature-clean, internally consistent, but false — is caught by re-derivation and *only* by re-derivation. That single bundle is a complete, working demonstration of why attestation ≠ truth. **Precision matters here (corrected in §10): Obsign is not the *only* outsider-checkable claim — ONE-Q's distance closures were also independently re-verified during this audit, and several public repos carry stranger-verifiable artifacts. The defensible statement is stronger for being exact: Obsign is the most generalized, productized, deliberately outsider-facing expression of the re-derivation doctrine** — while the flagship AI and compiler claims (ACE, LumOne, idem, glasshouse) still require the private, unshipped Coherence Language toolchain. Obsign is already on PyPI (`obsign-verify`) and npm, with the best cross-platform CI in the org (3 OS × 4 Python, including ARM64, printing output hashes per-runner so a divergence is visible).

- **Counterfactual-uniqueness — genuinely unoccupied ground.** The provenance landscape is entirely attestation-based (C2PA, in-toto, SLSA, SCITT) — all of them record *what was done* and sign it; none can re-execute the operation and confirm the result. The heavy alternative (ZK proofs) needs provers, trusted setups, and cryptographic novelty. Obsign occupies the empty middle: *re-derivation* — cheap, boring, no trusted hardware, no prover, auditable by hand. The decisive design insight is that **SLSA explicitly removed reproducible builds in v1.0 because reproducibility is intractable at build scale — and Obsign sidesteps that by narrowing to a single computed number.** That narrowing is what makes it work, and it is measured (27 instructions for a regulated credit-loss figure), not asserted. The replay-VM-carried-inside-a-signed-receipt is, as far as the analyses could find, not shipping anywhere.

- **Ceiling — civilizational, and rising on an external clock.** "How do you trust a computation you didn't run, especially an AI one" is a facet of nearly every live tech-policy fight: EU AI Act Article 50 transparency and high-risk model validation, NIST provenance work, the proposed U.S. Federal Rule of Evidence 707 (reliability of machine-generated evidence), Daubert reproducibility, SR 11-7 model-risk management in banking, FDA Software-as-a-Medical-Device, the scientific reproducibility crisis, and the entire zkML / verifiable-inference push. The regulatory clock is not controlled by the org and it is ticking toward exactly the primitive Obsign provides.

- **Adoption-reach — already installable, with a sharper wedge available.** The current README aims Obsign at AI-image provenance, which is both the more fashionable market *and* the weaker product: the public verifier cannot re-execute a single AI image edit today (`SUPPORTED_KERNELS = ("tau_field_fixed",)`; the replay VM caps at 2²⁰ cells). The stronger, already-verified wedge is **regulated computation** — the IFRS-9/CECL example, where the models don't move and only the disputed *combining arithmetic* needs to cross over to the verifier. That is the whole adoption story: you don't reproduce the bank's proprietary model, you reproduce the one number a regulator disputes.

- **Finishability — high, and independent of the estate's bottleneck.** The gaps are finite and enumerated (Section 8). None of them require the unshipped Coherence Language — Obsign's `tau_field_fixed` and replay paths are pure-Python / standard-library. This matters enormously: every *other* top candidate is blocked behind `loo`, which is itself only ~55–65% complete and proprietary.

**The portfolio-leverage argument.** Finishing Obsign does not just finish one product — it makes the estate's *shared thesis* externally legible. LumOne's receipts, ONE-Q's certificates, omega_one's signed decisions, glasshouse's proofs, and the covenant lattice all rest on the same re-runnable-receipt idea. Obsign is the public, checkable proof-of-concept for all of them. It is the one domino whose fall is visible from outside the building.

---

## 4. The scoreboard

Every serious candidate, scored on the model (H/M/L). "Ceiling" is problem size; "Cred." is *can an outsider verify it today*; "Uniq." is novelty the field would notice; "Reach" is can strangers use it; "Finish" is tractability of the remaining gap.

| Project | Ceiling | Cred. | Uniq. | Reach | Finish | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|---|
| **Obsign** (+verifier) | **H** | **H** | **H** | **M-H** | **H** | **The pick.** Only externally-verified claim; novel primitive; shipped; no blocking dependency. |
| **LumOne** (+platform) | **H+** | M | M-H | M | M | Runner-up. Highest ceiling; publishable result; but unreproducible by outsiders and the novel part (PIC) isn't wired in. |
| ONE-Q | M (deep) | **H** | H | M | **H** | Most shovel-ready. Independently re-verified. Tiny audience (QEC). Two papers written, unsubmitted. |
| VMP | **H** | **H*** | M-H | L-M | M | Best-engineered repo; question-native computation is measured (see §5b) but on constructed programs, not yet in its own CLAIM.md, and stranger-unverifiable today. CUDA/Windows-locked. |
| HazardPulse | **H+** | **Negative today** | M | M | L-M | Highest raw ceiling (lives) but currently loses to a trivial baseline in 432/432 forecasts. Fixable, but a science bet. |
| Coherence Covenant | M | H | M-H | L | **H** | ~500 LOC standards-track receipt lattice. Highest impact-per-line, but infrastructure — value ∝ adoption of the whole thesis. |
| Ariadne | M | H | M | **H** | **H** | Public, packaged, 1050 tests. Highest odds of a *real external user*. One honest baseline from a solid paper. Modest ceiling. |
| loo `certified_compile` | **H** | M | **H** | L | L | Highest-ceiling *idea* (proof-gated per-function backend routing), lowest readiness. Integer-fragment, proprietary, no paper. |
| One Link | M | M | L | M | L | Undifferentiated vs Signal/Briar/SimpleX; build broken at HEAD; classical ratchet is behind Signal. |
| ACE | M | L | L | L | L | 2M lines, largely generated; marquee self-modification has zero write calls; not instantiable from its own repo. |

---

## 5. The runner-up, and the honest tension: LumOne

LumOne deserves a real hearing because on **ceiling alone it beats Obsign.** "An LLM that answers only when it can back the answer with a machine-checkable warrant, and signs a certificate of what it cannot know instead of bluffing" targets *the* defining failure of applied AI — hallucination / unknown-unknowns — and gates every regulated LLM deployment on earth. It has a genuinely publishable measured result: on held-out, decontaminated, unanswerable questions the false-answer rate drops from 87% to 3.7%, with a bootstrap confidence interval that excludes zero (the cost is coverage roughly halving). Its 21 solver lanes (exact arithmetic, Z3 over `int64`, SymPy CAS, exhaustive logic) are real and run *before* the model. And its **Provable Ignorance Certificate** — a signed, bounded, third-party-re-runnable certificate that a complete search found neither proof nor refutation, pinned to a hash of the belief state and composable across independent agents — is the single most novel primitive in the entire AI cluster. It has essentially no prior art.

So why does Obsign rank above it for *this* question?

1. **Credibility is the gating term, and LumOne cannot be checked by an outsider today.** It needs a 14B model, a CUDA GPU, the private Coherence Language compiler, and a self-hosted Windows runner; its full gate is off by default. For "if the world knew," the world must be able to verify — and only Obsign clears that. An unverifiable claim, however important, does not move experts when revealed.
2. **The novel part isn't wired in.** The certificate-of-ignorance lives in `pic.py` and is exercised only by tests; the shipping product emits a hardcoded English "I don't know" string. The org's flagship marketing sentence is, as of today, literally not what the product does.
3. **Dependency risk.** LumOne is blocked behind `loo` (unshipped, proprietary, ~60% done). Obsign's core is not.
4. **Obsign is the substrate LumOne needs anyway.** LumOne's whole value proposition is the re-runnable receipt attached to each answer. Finishing Obsign first makes LumOne's receipts credible — the two share a spine.

**The synthesis:** these are not really competitors. Obsign is the *provable-computation receipt*; LumOne is *that receipt applied to LLM answers*. The correct sequencing is Obsign → LumOne, and the correct near-term move on LumOne specifically is small and high-leverage: **wire `pic.py` into `turn.py` and the platform's chat envelope so "I don't know" becomes a downloadable, verifiable artifact** (days of work), and **publish a Linux/CPU path so a stranger can reproduce the 87%→3.7% number** (the single highest-value credibility action available to that project). Do those two things and LumOne graduates from "highest ceiling, can't check it" to a genuine co-headline.

---

## 5b. Challenge round — the case for VMP first, and why the pick survives it

A serious counter-analysis was raised after the first version of this report: finish **VMP** first, not as a fast-math library but as the first public expression of *proof-directed, minimum-sufficient computation* — "a computer should compute only the information still necessary to prove the answer to the question being asked." That framing deserved verification against the repo rather than argument, so its load-bearing claims were checked directly.

**What the counter-case gets right (and this report now adopts):**

- Question-native computation in VMP is **measured, not merely envisioned**. `artifacts/observable_pullback__20260814T220445Z.json` records answering a query about a matrix product instead of materializing it — 11.45 ms vs 1210.36 ms (**105.7×**) with 1000/1000 exact identity trials, capacity certification (K18 covers; K16 correctly REFUSED), both arms agreeing exactly before any clock, and an honest information-floor note. BOARD row C2 records a proof planner that allocates channels per region — a settled region gets **zero** — 6.866 ms vs 9.3 ms uniform with every observable proven and a negative control. VISION §3.2 (marked BUILT): for a sign observable, 99.95% of the matrix settles at zero channels; every argmax/top-3 row settles at the cheapest rung.
- The "five questions" benchmark it proposes — exact value → interval → sign → threshold → argmax, with work collapsing as the question weakens — is the single best experiment design available to the estate, and this report adopts it as the flagship research act.
- Its "one escalating argument" portfolio framing (deterministic compute → proof/trust → verified decisions → discovery → matter) is crisper than this report's original portfolio-leverage section, and is adopted.

**Accordingly, VMP's ceiling in the scoreboard is raised from M-H to H.**

**Why the pick nevertheless stands — three arguments, each backed by VMP's own artifacts:**

1. **The counter-case grades VMP on its vision and Obsign on its present.** Its own stated criterion — *demonstrated without asking anyone to accept CEL's broader framework; survives hostile external verification* — selects Obsign today. VMP, by its own BOARD at this revision: `DONE 7 · BUILT 4 · OWED 7 · BLOCKED 13 · UNVERIFIED 13`. The pullback/planner results are on **constructed programs** (the board's own residual: "met in arithmetic, not in provenance"), have **not passed into VMP's own CLAIM.md**, and a stranger can neither install nor verify VMP today (Windows + CUDA + Python 3.14-pinned, checked-in DLLs, README linking three gitignored files). Graded consistently — both on vision, or both on present — the orderings converge or favor Obsign.
2. **The counter-case's own finish gates encode this report's sequencing.** Its gate 2 for VMP is verbatim Obsign-shaped: "a stranger verifies it — ship a small public verifier that imports no producer implementation, *following the Obsign/Covenant doctrine*." VMP's own moonshot gate for "verified compute as a market" is "a stranger pays for a result and verifies it without trusting us." Obsign is not rank #9 beneath VMP; **Obsign is VMP's gate 2**, already shipped. Proof-directed computing cannot reach the world without the stranger-verifiable receipt; the receipt is already in the world.
3. **"Finish VMP" is a research bet in a finishing costume.** Its own theorem ("exactness transfers, performance never does") predicts the headline shrinks on datacenter silicon; the structure-route timing experiment carried `INDICATIVE ONLY` and missed its preregistered target (1.704 vs ≥1.85); the five-questions experiment on real application traces is unrun. And the paradigm lands in dense prior art — lazy evaluation, database query optimization, branch-and-bound / best-arm racing (the `L_A > max U_j` early-stop), early-exit inference, self-adjusting computation and differential dataflow ("work ∝ change" is its tagline). The defensible novelty in CEL's hands is the **certificate welded on** — the receipt thesis again, which argues for shipping the receipt first.

**The synthesis this report now carries:** sequence by risk class, not ceiling. **Act One (months, low variance): finish Obsign** — the credibility spear and the substrate. **Act Two (the elevated research flagship): VMP's five-questions experiment, with every point's certificate emitted as an Obsign replay program**, so a stranger verifies the entire curve in the already-shipped verifier — the weld that makes "a new abstraction for computing" survive hostile review. **In parallel (days–weeks): LumOne's two cheap moves** (wire the ignorance certificate into the product path; publish a CPU reproduction of the 87%→3.7% result). The two analyses are the producer half and the verifier half of one architecture; the strategy uses both, in the order credibility compounds.

---

## 6. The full portfolio map (all 47 repos)

Organized by what they *are*, with lineage. The estate is one substrate (`loo`) plus applications, plus a governance layer, plus a large legacy/theory tail.

**The substrate**
- `loo` — **Coherence Language**: the language, compiler (7 backends), self-hosted stage-1/2 compiler, stdlib, IDE, and the genuinely novel `fabric/symbolic.py` + `certified_compile.py` (proof-gated per-function backend routing). Root of everything; ~55–65% complete; proprietary.
- `cel` — the company **website** monorepo (3GB, ~2.9GB abandoned data/git). Live surface is 10K lines of `.cl` + one Worker. Home of `claims-ledger.json`, the best governance artifact in the org.

**The verifiable-computation core (the estate's real thesis)**
- `obsign` + `obsign_verifier` — **the pick.** Re-executable receipts; the only externally-verified claim; shipped public.
- `coherence_proof_fabric` — canonical claim envelope + dependency-free strict verifiers (py/js/C/Rust/WASM) + a GitHub Action; ~90% shippable but crowded (overlaps in-toto/DSSE/C2PA). Labels its *own* Merkle binding "REFUTED — BROKEN IN PRACTICE."
- `coherence_covenant` — the ~500-LOC receipt soundness lattice (L0–L5, VIOLATION-vs-UNVERIFIED); standards-track; private.
- `evidence` (public) — the org's claims registry, where "we can't show you this" is a first-class labeled status.
- `capability_atlas` — the estate's self-gating map and its own harshest critic (its RANKING doc finds "12 of 19 Tier-1 capabilities have no executable claim reaching them").
- `vmp` — exact certificate-carrying GPU linear algebra + the estate's most portable measurement discipline; best-engineered repo.
- `omega_one` — coherence-native ML; commodity predictor, but the 0-ULP cross-substrate signed *receipt* is the real asset ("sell the receipt, not the theory").
- `idem` — proof-carrying e-graph; headline speedup falsified on real hardware (~1.0× vs `gcc -O3`); external NO-GO kept.

**AI systems**
- `lumone` + `lumone-platform` — **the runner-up.** Neurosymbolic router + Provable Ignorance Certificate; publishable abstention result; not connected end-to-end.
- `ace` / `ace_og` / `ace_console` / `ace-website` — symbolic cognitive organism (2M generated lines; self-modification is proposal-only), its museum-piece ancestor, a read-only monitor with a genuinely good "health = semantic depth" idea, and a marketing site. `ace` supersedes `ace_og`.
- `coherence_ai` — the 2025 root ancestor of the whole tau-field lineage; superseded; contains a live undocumented trading daemon (the estate's largest undocumented liability).
- `council` — multi-LLM deliberation with correlation-aware independence accounting and certificates of ignorance; the only AI repo usable today via `pip`; needs efficacy evidence.
- `coherent_adversary` — a ZK-circuit soundness analyzer (highest *dollar* impact — gates bridge/rollup TVL); self-invalidating assurance is its novel idea; gated behind its own NO gates; depends on `loo`.

**Applied science**
- `hazardpulse` (public) — earthquake/hurricane/tornado forecasting; highest raw ceiling; central claim currently false but with a specific fixable cause (missing background probability floor).
- `one_q` + `oneq-distance-closures` (public) + `qcode-discovery` (fork) — QEC decoder optimality certificates + qLDPC distance certification; independently re-verified; papers written, unsubmitted; IBM PR unanswered since July 30.
- `one_discovery_engine` — materials discovery; most epistemically disciplined repo ("Level 2.5 of 7, nothing has met matter"); no LICENSE file (legally unrunnable by third parties).
- `biomesh` — RF detection of invasive species; real ecological value; project-defining claim unmeasured; idle.
- `Ariadne` (public) — astrodynamics toolkit; packaged, 1050 tests, honest negative controls; the highest odds of a real external user in the whole org.
- `matching_manifold` — certified RF impedance instrument ("an instrument with a conscience"); one ~$300 tuner from closing its loop.

**Competitions (time-boxed)**
- `rsna-knee-2026` — knee-MRI Kaggle ($77K, deadline Oct 22); rank 103/1703, 0.024 below top-10; blocked on GPU quota, not science.
- `arc_prize_2026` — ARC-AGI-3; 0.00 on the hidden set; real target is the Nov 8 Paper Prize, but no paper is written; "certificates of provable ignorance" is the idea worth rescuing.
- `agent_security_kaggle` — **urgent:** entry closes ~Aug 25 (days away); a ready, gated notebook measuring ~40× the starter baseline that *has never been submitted.*

**Communications**
- `one-link` + `one-link-website` — post-quantum serverless messenger; large and impressive but undifferentiated vs Signal/Briar/SimpleX, LAN-only by default, classical ratchet, build broken at HEAD.

**Theory / legacy / hardware / marketing tail**
- `fvcs_book` — a 92,500-word monograph that builds to a 328-page PDF and *already functions as the estate's audit instrument* (8 work orders → landed fixes in 6 repos, 18+ math corrections). Roughly three edits from publishable.
- `one_mind`, `field_organism`, `coherence_cell`, `genesis_engine`, `coherence-glass-plant`, `onefield-mesh`, `living-glyph`, `coherence_program`, `glasshouse`, `Ariadne` are covered above or are paper/simulation designs, governance docs, and hardware Phase-0 work with honest "nothing has touched hardware yet" ledgers.

**Do-not-build-on (flagged for the record):** `onefield-mesh` (dimensionally inconsistent load-bearing constant; beyond-Shannon claims; Apache-licensed and therefore the most exposed) and `coherence_ai` (a live autonomous trading daemon with no committed backtest, P&L, or risk documentation).

---

## 7. What "finish Obsign" concretely means

The finish line is finite and does not touch the estate's bottleneck (`loo`). In priority order:

1. **Ship the replay-program compiler.** Today a customer hand-writes the 27-instruction assembly for their number. A small compiler that emits deterministic replay programs from ordinary Python/SQL aggregations turns Obsign from a demo into a tool. *This is the single highest-leverage piece of engineering.*
2. **Re-aim the wedge at regulated computation.** Lead with the IFRS-9/CECL / SR 11-7 model-validation story (a disputed number a regulator can re-derive without the proprietary model), not AI-image provenance (where the verifier cannot yet re-execute an image edit). The already-verified evidence is on the finance side.
3. **Get the external cryptographic audit** the project's own doctrine demands and has never had (`docs/SECURITY_AUDIT_SCOPE.md` is written and waiting).
4. **Land one third-party attestation** — a single outside party who runs the verifier and publishes the log. The attestation format is specified and the template is empty (`challenge/ATTESTATION.md`). One real one converts "well-built" into "credible."
5. **Submit `c2pa.reproducible.operation`** to the C2PA working group as the standards path — Obsign already contains the proposed vendor-neutral assertion and a real integration with Adobe's `c2pa-rs`.
6. **Fix the trivial credibility leaks** that undercut a project whose entire brand is "no unbacked claims": the README says v1.0.0 while the package is v2.0.0; `challenge/README.md` lists an expected output that doesn't match the shipped bundles; and rotate the leaked credential regardless (`obsign_verifier` is in fact already public — see §10 correction 3 — which makes the rotation more urgent, not less).

Realistic horizon: a focused few months, most of it packaging, audit, and one compiler — not open research.

---

## 8. Three cross-cutting recommendations (independent of the pick)

1. **Close the gap between the careful repos and the overclaiming website — first, before any outreach.** The repos are disciplined; `cel/ssg/build.cl` is not, and the claims-ledger gate only checks numbers already *in* the ledger. The public "29 cryptographic primitives implemented natively across four independent execution surfaces" is contradicted by the estate's *own source* (`loo/.../crypto_reference.py`: they are bare `extern fn`s dispatching to the same Python callables — not native, not independent). One unbacked public number makes an expert discount the twenty that are real, and here most of them are real. Put every public number under the ledger gate.

2. **Take the shovel-ready credibility wins now.** Two are nearly free: **ONE-Q** has two finished papers and an independently-re-verified result sitting behind an "owner must decide" flag and an IBM PR nobody has answered — submit them and get one stranger to run `challenge/verify.sh`. **Ariadne** is one honest baseline experiment from a real algorithms paper and one `twine upload` from being on PyPI. Neither changes the world, but both convert latent work into external legibility at near-zero cost.

3. **The `agent_security_kaggle` deadline is ~August 25.** A ready, gated notebook measuring ~40× the starter baseline has never been submitted because no one has pushed the button (no `kaggle.json`, rules unaccepted). Not world-changing, but it is free money and a scored credential left on the table with days to spare. Submit it.

---

## 9. The through-line

The most striking fact about this portfolio is that it has, forty-seven times over, built the discipline for proving things are true — and then, in its public voice, made claims it cannot yet prove. The scarcest resource here is not rigor; there is more rigor per line in this org than in most funded labs. It is **convergence** — choosing one thing and carrying it through the last 30% into the world's hands.

Obsign is that one thing. It is the estate's own best idea — the re-runnable receipt — already extracted, already shipped, already the claim most deliberately handed to strangers to verify, and it held. Finishing it doesn't just complete a product; it makes the whole portfolio's thesis checkable by people who have never met the author. That is what "impact if they knew" actually looks like: not a louder claim, but a claim anyone can re-run on their own machine and watch come out true.

---

## 10. Challenge rounds and convergence (amended 2026-08-19)

This report was stress-tested in three rounds after its first version; the record is kept, per the estate's own erratum discipline.

**Round 1 — the VMP counter-case.** "Finish VMP first, as proof-directed computing." Verified against VMP's artifacts and answered in §5b: VMP's ceiling raised to H; the pick held because Obsign is VMP's own stranger-verification gate, and "finish VMP" is a research bet whose flagship experiment is unrun.

**Round 2 — the owner's rule: "largest impact, period; proximity excluded."** Under that objective the analysis named **LumOne**: the mechanism is evidenced (the 87%→3.7% selective-prediction result; real solver lanes; the Provable Ignorance Certificate implemented), and the ceiling operates at the layer civilization is delegating cognition to. Four tiebreakers vs VMP-as-paradigm: it attacks the binding constraint of the era (trust in machine cognition, not compute cost); the counterfactual is stark (nobody ships certified ignorance; everybody attacks compute efficiency); VMP's termination law reaches maximum expression at the semantic layer, which *is* LumOne; and its prevented failures are catastrophic-tail-shaped. The honest conditional: LumOne's ceiling equals the growth curve of its verification frontier (42.6% today), with autoformalization and the solver ecosystem as compounding tailwinds.

**Round 3 — the owner's synthesis, and convergence.** The owner's independent review reached the same finish-first conclusion from a different route: *Obsign is the public abstraction for the entire stack* — the doorway through which every other project's results become externally checkable ("ONE-Q result? Obsign it. VMP computation? Obsign it. LumOne answer? Obsign it."). It also supplied the sharpest formulation of the target: not an image-forensics product and not merely "re-executable receipts," but **the universal verification layer for computed claims**, built on the operation of **extracting the truth-bearing kernel** — most committing claims depend on a small deterministic slice of an enormous system; find that slice, freeze it as a replay program, pin its hash, receipt it. The resulting systems pattern unifies the portfolio: *large untrusted intelligence → small truth-bearing computation → minimum-sufficient execution → independent receipt.*

**Resolution of the remaining ceiling dispute (VMP #1 vs LumOne #1):** both statements are true at different altitudes. A pattern's ceiling is the sum over all its deployments — so VMP-as-pattern (minimum-sufficient verified computation) bounds any single consumer from above. The largest *single term* in that sum is the committing boundary of AI, which is LumOne's seat — and LumOne is itself the pattern's reference deployment (untrusted model proposes; deterministic lanes settle; receipt signs). No rival projects; one architecture: **Obsign the doorway, VMP the engine, LumOne the flagship deployment.**

**Three corrections adopted from the owner's review:**
1. **"Only externally-verified claim" was overstated.** ONE-Q's distance closures were also independently re-verified during this audit, and several public repos (oneq-distance-closures, hazardpulse ledgers, the org profile's own challenges) carry stranger-verifiable artifacts. Corrected in §3 to the exact and stronger statement: Obsign is the most generalized, productized, deliberately outsider-facing expression of the re-derivation doctrine.
2. **"The real asset was never the physics" refined** (§2): the audit shows the physics is not load-bearing in any verified result today — which proves the verification architecture is independently valuable, not that the physics is worthless. The physics is an open research program whose credibility should arrive through the receipt layer.
3. **`obsign_verifier` is public**, not private: the session-start repository inventory lists it `visibility: public`. The "private pending key rotation" note in §3/§7 was stale (drawn from an in-repo doc). The credential rotation remains worth doing — more so, now that the repo is exposed.
