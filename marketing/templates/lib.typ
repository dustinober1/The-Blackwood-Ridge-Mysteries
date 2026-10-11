// Shared brand library for the Blackwood Ridge social card templates.
// Single source of truth: /marketing/brand.yaml.

#let brand = yaml("/marketing/brand.yaml")
#let C = brand.colors
#let ink = rgb(C.ink)
#let ink_warm = rgb(C.ink_warm)
#let ivory = rgb(C.ivory)
#let ivory_muted = rgb(C.ivory_muted)
#let gold = rgb(C.gold)
#let gold_light = rgb(C.gold_light)
#let gold_shadow = rgb(C.gold_shadow)
#let stamp_red = rgb(128, 35, 30) // rubber-stamp oxblood for case files

// Alpha helpers — veils and scrims over photography.
#let ink-a(pct) = rgb(14, 6, 15, pct)
#let ivory-a(pct) = rgb(247, 242, 228, pct)
#let gold-a(pct) = rgb(216, 168, 78, pct)

#let ink-veil(pct) = rect(width: 100%, height: 100%, fill: ink-a(pct))
#let ivory-veil(pct) = rect(width: 100%, height: 100%, fill: ivory-a(pct))
// Vertical scrims (verified empirically): 270deg seats the gradient's first
// stop at the rect's bottom edge, 90deg at the top edge.
#let bottom-scrim(height, maxa) = place(bottom, rect(width: 100%, height: height, fill: gradient.linear(ink-a(maxa), ink-a(0%), angle: 270deg)))
#let top-scrim(height, maxa) = place(top, rect(width: 100%, height: height, fill: gradient.linear(ink-a(maxa), ink-a(0%), angle: 90deg)))

#let F = brand.fonts
#let wordmark = "THE BLACKWOOD RIDGE MYSTERIES"

// Modern sans kicker — the "present day" voice against the historic serifs.
#let kicker(txt, size: 9pt, col: ivory-a(90%), tracking: 4.5pt) = text(
  font: (F.kicker, "Avenir Next"), weight: 500, size: size, fill: col, tracking: tracking)[#txt]

// Small-caps label flanked by hairlines (used over photography).
#let eyebrow-block(txt, col: ivory-a(88%), line-col: gold-a(45%)) = grid(
  columns: (1fr, auto, 1fr),
  column-gutter: 14pt,
  align: (right + horizon, center + horizon, left + horizon),
  line(length: 100%, stroke: (paint: line-col, thickness: 0.7pt)),
  text(font: (F.kicker, "Avenir Next"), weight: 500, size: 8.5pt, fill: col, tracking: 3.5pt)[#txt],
  line(length: 100%, stroke: (paint: line-col, thickness: 0.7pt)),
)

#let wordmark-footer(col: gold-a(62%)) = place(bottom + center, dy: -20pt)[
  #text(font: F.label, size: 7.5pt, fill: col, tracking: 2pt)[#wordmark]
]
