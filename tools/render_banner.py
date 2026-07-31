#!/usr/bin/env python3
"""Coherence Energy Labs — org banner as a re-executable figure.

The banner is not a drawing. It is the solution of the estate's field equation

    (D·L + kappa^2·I) tau = s

solved over a jittered lattice graph in EXACT INTEGER arithmetic (no floats
anywhere in the field or the geometry), rendered to SVG. Every byte of the
output is a pure function of the parameters below. CI re-derives both variants
on every push and fails if a single byte drifts.

Usage:
    python tools/render_banner.py           # write assets/banner-{dark,light}.svg + RECEIPT.json
    python tools/render_banner.py --check   # re-derive and byte-compare against committed assets
"""

import hashlib
import json
import os
import sys

# ---------------------------------------------------------------- parameters
W, H = 1600, 400
COLS, ROWS = 40, 10
JITTER = 9            # px, deterministic LCG
D_MILLI = 1000        # diffusion coefficient x1000
K2_MILLI = 50         # kappa^2 x1000  (decay length ~ sqrt(D/kappa^2) cells)
ITERS = 300           # Jacobi iterations
SRC = 1 << 44         # source strength (integer)
SEED = 0x1CEB00DA     # fixed seed
SOURCES = [(0.19, 0.60), (0.50, 0.34), (0.81, 0.60)]  # fractional positions
PULSE_MS = 6000

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")


def lcg(seed):
    s = seed
    while True:
        s = (s * 6364136223846793005 + 1442695040888963407) & ((1 << 64) - 1)
        yield s >> 33


def build_graph():
    rnd = lcg(SEED)
    dx, dy = W // (COLS + 1), H // (ROWS + 1)
    nodes = []
    for r in range(ROWS):
        for c in range(COLS):
            jx = next(rnd) % (2 * JITTER + 1) - JITTER
            jy = next(rnd) % (2 * JITTER + 1) - JITTER
            nodes.append(((c + 1) * dx + jx, (r + 1) * dy + jy))
    idx = lambda r, c: r * COLS + c
    edges = []
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < ROWS and 0 <= cc < COLS:
                    edges.append((idx(r, c), idx(rr, cc)))
    return nodes, edges


def solve_field(nodes, edges):
    n = len(nodes)
    nbr = [[] for _ in range(n)]
    for a, b in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    s = [0] * n
    for fx, fy in SOURCES:
        tx, ty = int(fx * W), int(fy * H)
        best = min(range(n), key=lambda i: (nodes[i][0] - tx) ** 2 + (nodes[i][1] - ty) ** 2)
        s[best] = SRC
    tau = [0] * n
    for _ in range(ITERS):
        tau = [
            (s[i] + D_MILLI * sum(tau[j] for j in nbr[i])) // (D_MILLI * len(nbr[i]) + K2_MILLI)
            for i in range(n)
        ]
    tmax = max(tau) or 1
    bright = [t * 1000 // tmax for t in tau]  # 0..1000, exact integers
    return tau, bright


PALETTES = {
    "dark": dict(bg="#0A0D12", node="#F5C044", edge="#F5C044", title="#F2EFE6",
                 sub="#B8B2A2", meta="#6E7681", rule="#F5C044"),
    "light": dict(bg="#FBFAF7", node="#A66A1F", edge="#A66A1F", title="#1A1A17",
                  sub="#57534A", meta="#8B8578", rule="#A66A1F"),
}


def render(variant, nodes, edges, bright, field_sha):
    p = PALETTES[variant]
    fonts = "'Inter','Segoe UI',system-ui,-apple-system,sans-serif"
    mono = "'SFMono-Regular','Cascadia Code',Consolas,monospace"
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
               f'width="{W}" height="{H}" role="img" '
               f'aria-label="Coherence Energy Labs: how systems hold together">')
    out.append(f'<!-- RE-EXECUTABLE FIGURE. This image is the solution of '
               f'(D*L + kappa^2*I) tau = s over a {COLS}x{ROWS} lattice, solved in exact '
               f'integer arithmetic. params: D_milli={D_MILLI} k2_milli={K2_MILLI} '
               f'iters={ITERS} seed={SEED:#x} src={SRC:#x}. sha256(field)={field_sha}. '
               f'Re-derive: python tools/render_banner.py (repo coherence-energy-labs/.github) -->')
    out.append(f'<defs><clipPath id="rc"><rect width="{W}" height="{H}" rx="30" ry="30"/></clipPath>'
               f'<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">'
               f'<stop offset="0" stop-color="{p["node"]}" stop-opacity="0"/>'
               f'<stop offset="0.5" stop-color="{p["node"]}" stop-opacity="0.055"/>'
               f'<stop offset="1" stop-color="{p["node"]}" stop-opacity="0"/></linearGradient></defs>')
    out.append('<g clip-path="url(#rc)">')
    out.append(f'<rect width="{W}" height="{H}" fill="{p["bg"]}"/>')
    # --- edges (the web that holds together)
    out.append(f'<g stroke="{p["edge"]}" stroke-width="1">')
    for a, b in edges:
        w = min(bright[a], bright[b])
        if w < 60:
            continue
        op = 40 + w * 240 // 1000  # 0.040 .. 0.280, in thousandths
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-opacity="0.{op:03d}"/>')
    out.append('</g>')
    # --- nodes, phase-locked to the field (begin offset = -tau-proportional)
    out.append(f'<g fill="{p["node"]}">')
    for i, (x, y) in enumerate(nodes):
        b = bright[i]
        r_tenths = 12 + b * 26 // 1000            # radius 1.2 .. 3.8 px
        lo = 80 + b * 250 // 1000                 # opacity floor  .080 .. .330
        hi = 200 + b * 700 // 1000                # opacity peak   .200 .. .900
        begin = b * PULSE_MS // 1000              # phase from tau
        out.append(
            f'<circle cx="{x}" cy="{y}" r="{r_tenths // 10}.{r_tenths % 10}">'
            f'<animate attributeName="opacity" values="0.{lo:03d};0.{hi:03d};0.{lo:03d}" '
            f'dur="{PULSE_MS}ms" begin="-{begin}ms" repeatCount="indefinite"/></circle>')
    out.append('</g>')
    # --- signal pulses traveling the lattice rows (speed follows the field)
    pulses = []
    for r in range(0, ROWS, 1):
        row = nodes[r * COLS:(r + 1) * COLS]
        mb = sum(bright[r * COLS:(r + 1) * COLS]) // COLS
        if mb < 60:
            continue
        d = f"M{row[0][0]} {row[0][1]} " + " ".join(f"L{x} {y}" for x, y in row[1:])
        dur = 30000 - mb * 20000 // 1000
        begin = (r * 3137) % dur
        op = 350 + mb * 550 // 1000
        pulses.append(
            f'<circle r="2.2" fill="{p["node"]}" fill-opacity="0.{op:03d}">'
            f'<animateMotion path="{d}" dur="{dur}ms" begin="-{begin}ms" repeatCount="indefinite"/>'
            f'<animate attributeName="fill-opacity" values="0;0.{op:03d};0.{op:03d};0" '
            f'keyTimes="0;0.06;0.94;1" dur="{dur}ms" begin="-{begin}ms" repeatCount="indefinite"/></circle>')
    out.append('<g>' + "".join(pulses) + '</g>')
    # --- wordmark
    cx = W // 2
    out.append(f'<text x="{cx}" y="176" text-anchor="middle" font-family={fonts!r} '
               f'font-size="54" font-weight="600" letter-spacing="14" fill="{p["title"]}">'
               f'COHERENCE ENERGY LABS</text>')
    out.append(f'<rect x="{cx - 260}" y="204" width="520" height="2" fill="{p["rule"]}" fill-opacity="0.55"/>')
    out.append(f'<text x="{cx}" y="248" text-anchor="middle" font-family={fonts!r} '
               f'font-size="23" font-weight="400" letter-spacing="6" fill="{p["sub"]}">'
               f'HOW SYSTEMS HOLD TOGETHER</text>')
    # --- the receipt, printed on the artifact itself
    out.append(f'<text x="24" y="{H - 18}" font-family={mono!r} font-size="13" '
               f'fill="{p["meta"]}">(D·L + κ²I)τ = s · exact integer arithmetic · '
               f'{ITERS} Jacobi iterations · {COLS}×{ROWS} lattice</text>')
    out.append(f'<text x="{W - 24}" y="{H - 18}" text-anchor="end" font-family={mono!r} '
               f'font-size="13" fill="{p["meta"]}">sha256(field) = {field_sha[:16]}… · '
               f're-derive: tools/render_banner.py</text>')
    out.append(f'<rect x="-460" y="-40" width="360" height="{H + 80}" fill="url(#sheen)" '
               f'transform="skewX(-16)"><animateTransform attributeName="transform" type="translate" '
               f'additive="sum" values="0 0; {W + 960} 0" dur="11000ms" repeatCount="indefinite"/></rect>')
    out.append('</g>')
    out.append('</svg>')
    return "\n".join(out).encode("utf-8")


def main():
    check = "--check" in sys.argv
    nodes, edges = build_graph()
    tau, bright = solve_field(nodes, edges)
    field_sha = hashlib.sha256(",".join(map(str, tau)).encode()).hexdigest()
    svgs = {v: render(v, nodes, edges, bright, field_sha) for v in ("dark", "light")}
    receipt = {
        "artifact": "org profile banner (animated SVG, dark+light)",
        "equation": "(D*L + kappa^2*I) tau = s",
        "arithmetic": "exact integer (python int), no floats in field or geometry",
        "params": {"W": W, "H": H, "COLS": COLS, "ROWS": ROWS, "JITTER": JITTER,
                    "D_milli": D_MILLI, "kappa2_milli": K2_MILLI, "iters": ITERS,
                    "seed": hex(SEED), "source_strength": hex(SRC), "sources": SOURCES,
                    "pulse_ms": PULSE_MS},
        "sha256_field": field_sha,
        "sha256_svg": {v: hashlib.sha256(b).hexdigest() for v, b in svgs.items()},
        "re_derive": "python tools/render_banner.py --check",
    }
    rec_bytes = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode()

    targets = {os.path.join(ASSETS, f"banner-{v}.svg"): b for v, b in svgs.items()}
    targets[os.path.join(ASSETS, "RECEIPT.json")] = rec_bytes

    if check:
        bad = []
        for path, want in targets.items():
            have = open(path, "rb").read() if os.path.exists(path) else b""
            if have != want:
                bad.append(os.path.relpath(path, ROOT))
        if bad:
            print(f"DRIFT: {', '.join(bad)} do not match re-derivation. "
                  f"The banner is a receipted artifact; regenerate with tools/render_banner.py.")
            sys.exit(1)
        print(f"OK: banner re-derives byte-identically. sha256(field)={field_sha[:16]}...")
        return

    os.makedirs(ASSETS, exist_ok=True)
    for path, data in targets.items():
        with open(path, "wb") as f:
            f.write(data)
        print(f"wrote {os.path.relpath(path, ROOT)}  sha256={hashlib.sha256(data).hexdigest()[:16]}...")


if __name__ == "__main__":
    main()
