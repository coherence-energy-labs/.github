# The Admission Spec

**How the Coherent Adversary becomes a product a stranger can use.**

Status: proposal. Written 2026-08-22 against `coherent_adversary@050acde` and `capability_atlas@3b73dd6`.
Every gate flag quoted below is read from `harness/gates.py` at that commit, not from a card.

---

## 0. The finding

The adversarial machinery is built. The attacks are real — Frozen Heart across
Bulletproofs/PlonK/Girault, Bleichenbacher e=3, length-extension MAC forgery, Merkle
leaf/internal type confusion, the DarkForest range-proof family, MACI wraparound synthesis,
comparator operand safety on real BN254 `.r1cs` bytes. The measured efficacy is real: **recall
1.0, precision 1.0** on a disclosed 10-target corpus where blind fuzzing hits **0/50,000**.

None of it is reachable by a stranger, and the reason is stated plainly in the repository:

```
external_admission = false
analysis_status    = NOT_RUN
execution_ready    = false
G0                 = NO
```

> *"Arbitrary external-target admission remains intentionally BLOCKED."*

**The product is not blocked on capability. It is blocked on a door.**

And the door already has a specification. `harness/gates.py` carries **40 boolean production
requirements** across G0–G7. Every one is `False`. That dict is the build plan — nobody has to
invent it, only execute it.

### The reframe

G0 is not a gate. It is a **conjunction of eleven flags written for the hardest case in the
system**: running an untrusted *native toolchain* over an *external artifact* on a *shared-user
Windows host*. G0 stays NO because `all(production_requirements.values())` is `False`, and it is
correct that it does.

But almost every flag in that conjunction is about **compiling someone else's Circom**. A product
that never compiles anyone's Circom is being blocked by a threat model it does not have.

> **Do not open G0. Split it.**

---

## 1. Admission classes

The lattice conflates four analyses with four different threat models. Separate them and the
build plan collapses from "40 flags" to "which flags does *this* analysis actually need."

| Class | What runs | Threat surface | Example |
|---|---|---|---|
| **A — INSPECT** | Nothing of the target's. Parse only. | Parser hardening. Resource limits on parsing. | Static vacuity audit; claim extraction; receipt structure checks |
| **B — REPLAY** | The receipt's own IR, in a machine with no floats, no clock, no syscalls, no allocation, and a step budget. | The IR itself — and it is total by construction. | `obsign-verify` replay; re-deriving a published number |
| **C — BUILD** | The *target's* toolchain. Native. Arbitrary. | Everything G0 enumerates. | Circom → R1CS → soundness analysis |
| **D — EXERCISE** | The *target's own test suite*, repeatedly, under mutation. | Arbitrary target code, plus secrets and network. | Sabotage: "your gate cannot detect the failure it claims to prevent" |

### Where the 40 flags actually land

**Class A needs approximately none of them.** Parsing untrusted text under a resource limit is
ordinary engineering. The one flag that genuinely applies is
`authority_revalidated_before_every_effect` — a general authorization property, not a containment
one. Class A is, today, *unblocked*.

**Class B needs one: `external_target_cold_replay_admission`.** And the hard half is already
discharged by the IR's own design. From the `obsign_verifier` card:

> Determinism is **structural, not promised**. There are no floats anywhere — not in the ops, not
> in the operands, not in the constant pool — and no clock, randomness, environment, I/O,
> allocation or host call. Not sandboxed: **absent from the instruction set**. […] Every operation
> is TOTAL. Division by zero, an out-of-range shift, a bad address and an exhausted step budget
> are traps — refusals with reasons, never exceptions that escape. **The step budget is a security
> property**: a receipt handed to you by an adversary must not be able to hang your verifier.

That is an admission argument, already written, already tested, already shipped to PyPI and npm
as `obsign-verify` 0.2.0 under Apache-2.0. What remains for cold-replay admission is *governance*
of the accepted program — which `--expect-program <sha256>` already provides — not containment.

**Class C needs nine of G0's eleven**, plus all five of G2. This is the ZK-audit business. It is
months of real work and it is the highest-value lane.

**Class D needs containment for running untrusted test suites** — which, unlike Class C, is a
solved industry problem (this is what every CI provider does) — plus secret hygiene and cost
control.

### The flags, mapped

| G0 flag | A | B | C | D |
|---|:-:|:-:|:-:|:-:|
| `analysis_route_enforcement_measured_by_gate` | – | – | ● | ● |
| `compilation_resource_contained` | – | – | ● | – |
| `compilation_egress_contained` | – | – | ● | – |
| `source_to_captured_r1cs_attribution` | – | – | ● | – |
| `strict_native_boundary_wired_to_external_compilation` | – | – | ● | – |
| `strict_native_live_drill_measured_by_gate` | – | – | ● | ● |
| `dos_device_lookup_atomically_excluded_during_every_appcontainer_launch` | – | – | ● | ● |
| `analysis_process_executable_attributed` | – | – | ● | ● |
| `admin_or_hypervisor_isolation` | – | – | ● | ● |
| `external_target_cold_replay_admission` | – | ● | ● | ● |
| `authority_revalidated_before_every_effect` | ● | ● | ● | ● |
| `independent_containment_red_team` | – | – | ● | ● |

Two flags gate the entire near-term product. Nine gate the ZK lane.

---

## 2. The free/paid boundary is an epistemic fact, not a pricing decision

This is the part worth getting right, because it makes the free tier honest instead of crippled.

Static analysis **cannot** resolve vacuity. To know whether a `parametrize` list is empty at
import time, you must import — and importing is execution. The `gate_vacuity_audit.py` detector
class *"parametrize over an import-time list that may be `[]`"* says **may** because that is the
strongest true statement a parser can make.

So the boundary writes itself:

| | Class | Verdict it can honestly issue |
|---|---|---|
| **Free, forever, no account** | A | *"17 gates **may** be vacuous. Here is where to look, and why."* |
| **Paid** | D | *"9 gates **are** vacuous. Here is the run in which the assertion never executed."* |

Free finds. Paid proves. That is not a funnel trick — it is the actual limit of what each analysis
can know, and stating it that way is the most on-brand thing this product could possibly do.

It also solves the surface problem: the free tier ships a **finding**, not an ontology. Nobody has
to learn what L3 means to understand *"this test has reported green 340 times and has never
executed its assertion."*

---

## 3. Build order

### Phase 1 — Class A. The free surface.
**Gates required: none. G4 recommended** (human spec review, so the claims on the page match what
the tool can know).

- Port `gate_vacuity_audit.py` off the workstation. **⚠ See §7 — it is not backed up.**
- Harden the parser against hostile input: refuse rather than raise. The `obsign_verifier` law
  applies verbatim — *"a verifier that raises on a hostile receipt has failed open in the eyes of
  whoever handed it the file. An exception is not a refusal."*
- Ship the five-verdict vocabulary (§5) with scope inside the verdict string.
- Ship the **MAY/IS** distinction on the face of every finding.

### Phase 2 — Class B. The certificate half.
**Gates required: `external_target_cold_replay_admission` + `authority_revalidated_before_every_effect`.**

- Formalize the admission argument the replay IR already satisfies, as a document a stranger can
  check: totality of every op, absence of syscall/clock/alloc from the instruction set, step
  budget as a security property, trap-not-throw.
- Wire `--expect-program` into the product surface as the primary question. *"Did this re-derive?"*
  is the demo. *"Did this re-derive from the program my validator approved?"* is the sale.

### Phase 3 — Class D. Sabotage. The money shot.
**Gates required: containment for untrusted test execution; G5's absence-proof discipline for the
WITHSTOOD side; G3 before any published metric.**

- Mutation harness that plants a known failure and asserts the target's own gate goes red.
- **DARK GATE** verdict (§5) — the highest-value output in the product.
- Run it on well-known open-source projects **yourselves** and publish. Do not offer it free to
  strangers on day one; you cannot contain that safely yet, and pretending otherwise designs a
  product you can't ship.

### Phase 4 — Class C. The ZK lane.
**Gates required: nine G0 flags + all five G2 flags.**

The highest-value lane and the only one where "absurdly better" is a *measurable* claim rather
than a marketing hope — because `harness/soundness.py` already positions against named
incumbents:

> *"Picus/Ecne pass a determined circuit that computes the WRONG function; this catches both."*

That is a testable superiority claim against a real competitor in a market that pays for audits.
Measure it, publish it with the corpus, and it is worth more than any amount of positioning prose.

### Phase 5 — Continuous.
**Gates required: G6 (independent red team), G7 (lifecycle recall — all nine flags).**

G7 is what makes the subscription real rather than SaaS theater. A warrant that cannot be revoked
is a warrant that lies as soon as the world moves. `artifact_change_invalidation`,
`spec_change_invalidation`, `toolchain_change_invalidation`, `key_rotation_invalidation`,
`dependency_watch` — each is a reason a previously-issued certificate must expire itself.

Fold Sentinel in here: the previous signed observation commits **in advance** to the deadline for
the next one, so killing the monitor produces observable missing evidence rather than ambiguous
silence.

### What can stay NO forever, for the near-term product
G1's four efficacy flags gate **claims about how good you are**, not admission. You do not need a
sealed multi-project holdout with an independent custodian to ship a free tool that shows a
developer a test which cannot fail. You need it before you publish a number. Keep them NO and
keep the numbers off the page until they're PASS.

---

## 4. The Attack object

The corpus already exists in embryo: the acceptor-differential library is a set of real,
disclosed, deployed soundness breaks, each modeled as `verify_buggy` vs `verify_correct` with a
minted witness and a confirmed post-fix rejection. That is the seed.

What is missing is that each attack must carry **live evidence that it can still attack**.

```
ATTACK  A-004217   Vacuous parameterized test
────────────────────────────────────────────────────────
targets          Python · pytest
failure class    FC-011  gate executes zero cases
applies when     parameters derived at import time
attack           force derived corpus → []
vulnerable       suite remains green
defended         gate refuses, or independently asserts non-empty corpus

ARMING                                    measured 2026-08-22
  kills known-vulnerable specimen         ✓
  leaves known-safe twin alive            ✓
  own detection path mutation-tested      ✓  15/15 guards removed → caught
  required capabilities present           ✓
  oracle independently checkable          ✓
  version + assumptions frozen            ✓  v3.2.1

STATUS           ARMED
measured FP rate 0.7%  (n=1,412)
last falsified   2026-07-31
```

**ARMED is a live state, not a property.** If any arming condition lapses, the attack goes
`UNARMED` and contributes exactly zero assurance to any assessment that includes it.

The arming mechanism already exists and should be generalized rather than invented:
`scripts/audit_independent_checker.py` removes **15 load-bearing guards one at a time** and
**all 15/15 mutations are caught**. That is arming, implemented, today.

### ⚠ The ratchet must count failure classes, not attacks

*"4,731 armed"* is a number about **attacks**. The estate has already paid for this exact mistake
one level down: 31 evidence claims looked like coverage until someone scored them per-capability
and it was **6 of 20**. `AUDIT_2026-08-14.md` names the trap precisely —

> The gate counts evidence claims **per card**. Nothing checks that a card's claim covers the
> card's *headline capability*. […] Scored per-card, both look covered. Scored per-capability,
> both are bare.

So the corpus ratchet must be:

```
FAILURE-CLASS COVERAGE: 34 of 61 classes have ≥1 ARMED attack
```

and it must fail the build when that number goes **down**. Counting attacks instead of classes
rebuilds the identical drift with more steps and a bigger number.

---

## 5. Verdicts

Five, and the scope lives **inside** the verdict string. A parenthetical never survives contact
with a reader.

| Verdict | Meaning |
|---|---|
| **REFUTED** | An independently reproducible counterexample exists. Here it is. Run it. |
| **WITHSTOOD 374/391 · 17 unarmed** | Every armed applicable attack executed within its declared model and produced no counterexample. **Not "safe."** The numerator and denominator are the honesty; the word alone is not. |
| **UNKNOWN under bounds B** | The bounded search terminated with neither proof nor counterexample. Signed certificate of exactly where we looked. |
| **NOT APPLICABLE** | No attack in the corpus honestly applies to this target class. |
| **DARK GATE** | The target's own defense did not detect a planted instance of the failure it claims to prevent. |

`DARK GATE` is the highest-value result the product can produce, and it is the only one that
requires Class D.

Inherit the discipline from `harness/determinacy.py`, which already refuses to collapse
`DETERMINED` / `UNDER-CONSTRAINED` / `UNPROVEN` into a boolean, and issues `DETERMINED` only with
an output-uniqueness proof and `UNDER-CONSTRAINED` only with a concrete two-witness forgery.

**Render-layer requirement:** gate the badge path the way `idem`'s Proven Surface gates
*"the verified badge only appears for verified peers."* A verdict that can be rendered green by a
mishandled enum is the same defect class this product exists to sell against.

---

## 6. The surface

### The line
> ## Green means nothing until red is possible.

Everything else is a subhead. It is legible to a developer, a CTO, and a regulator without a
glossary, and it is a distillation of what `gate_vacuity_audit.py` learned expensively:
*"A red test gets fixed. A test that cannot go red gets trusted, and that is worse."*

### The first screen
One field. Pre-defined input. **A git URL.** Never a blank box asking what you want to know is
true — that question has no existing behavior attached to it, and users will not invent one.

Button: **Attack it.**

### The first sixty seconds
No tour, no docs, no signup. A finding about *their own repository*:

```
tests/test_gpu_kernel.py::test_matches_cpu

MAY BE VACUOUS  ·  FC-011 gate executes zero cases

  parametrized over CASES, built at import time from a
  glob that resolves to [] when CUDA_HOME is unset.

  This gate has reported green 340 times.
  We cannot tell from source alone whether its assertion
  has ever executed. Running it would tell you.

  [ show the 4 lines ]   [ prove it — run the suite ]
```

The MAY is doing the work. It is the honest limit of Class A, it is more credible than a
confident green, and the *"running it would tell you"* line is the entire upgrade path stated as
a fact rather than a pitch.

### What they receive
Not "a portable object typed L0–L5." That is a thing only you want.

**Something to hand to a person who doubts them, and four words:**

> **Check it yourself. I'll wait.**

Nobody has been able to say that. Every incumbent answer is *trust our brand / our auditor / our
signature.* Design the free tier for the **receiver** — the bank validator, the reinsurer, the
diligence lead, the journal editor. They never buy anything and they create all the demand,
exactly as SOC 2 and HTTPS spread: the recipient started expecting it, so the sender had to have
it.

Attacking a stranger's claim feels like diligence. Attacking your own feels like homework. Sell to
the diligent; the homework gets bought defensively.

---

## 7. Risks, stated as gates

**🔴 The free tier's engine is not backed up.** `gate_vacuity_audit.py` lives in `coherence_lang`,
which does not exist under `coherence-energy-labs` on GitHub. `AUDIT_2026-08-14.md` Open Flag 1
records **68 commits** on local branches no remote has. The single most product-ready asset in the
estate is one disk failure from gone. **Fix this before anything else in this document.**

**An adversarial product's output is an accusation.** A false `DARK GATE` on someone's release
gate is a reputational and possibly legal event. History predicts it: `gate_vacuity_audit.py` was
narrowed **1759 → 515** because breadth generated false positives. Therefore every attack ships
its **measured** false-positive rate, and the corpus keeps its own falsification library — attacks
that were wrong, dated, with what replaced them. On-brand, and non-optional.

**Default private.** Anything the submitter is authorized to submit. Public arena limited to CEL's
own projects, opt-in open source, and explicit public challenges. Do not launch *"paste any
company's repo and we'll tell the world what's broken."*

**Language stays mechanical.** Never *"Company X lied."* Always *"Claim C does not re-derive under
the declared program"* or *"Gate G remained green after mutation M removed condition P."* Facts,
artifacts, scope.

**Do not claim novelty yet.** Property testing, mutation testing, fuzzing platforms, chaos
engineering, formal verification and adversarial ML each hold pieces of this. What is plausibly
unusual is the **composition** — an executable attack library whose individual attacks must prove
their own non-vacuity, producing typed portable survival/refutation evidence, preserving its own
failures. Research that before marketing it, and note that in the ZK lane you have named
competitors (Picus, Ecne) and can measure the claim instead of asserting it.

**The namespace has a clock on it.** PyPI `obsign` 0.0.1 was reserved by a `github.com/obsign` org
created **2026-07-30 16:57Z**, name taken 17 minutes later, self-described as *"cryptographic
proof of AI agent actions."* Someone is claiming this category now.

---

## 8. The one-line summary

The adversary is the engine. The certificate is what survives it. Neither is the product.

**The product is the door** — and the door's specification is already written, as 40 booleans, in
a file you already own.
