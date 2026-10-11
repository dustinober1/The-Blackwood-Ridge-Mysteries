// Shared brand library for the Blackwood Ridge social card templates.
// Single source of truth: /marketing/brand.yaml.

#let brand = yaml("/marketing/brand.yaml")
#let C = brand.colors
#let ink = rgb(C.ink)
#let ink_warm = rgb(C.ink_warm)
#let walnut = rgb(C.walnut)
#let ivory = rgb(C.ivory)
#let ivory_muted = rgb(C.ivory_muted)
#let gold = rgb(C.gold)
#let gold_light = rgb(C.gold_light)
#let gold_shadow = rgb(C.gold_shadow)

#let F = brand.fonts
#let wordmark = "THE BLACKWOOD RIDGE MYSTERIES"

// Alpha variants of the brand ink for scrims and vignettes (ink = #0E060F).
#let ink_0 = rgb(14, 6, 15, 0%)
#let ink_90 = rgb(14, 6, 15, 90%)

// Diamond ornament (vector — the ❦ glyph is missing from Hoefler Text Ornaments).
#let fleuron(size: 15pt, col: gold) = rotate(45deg, origin: center, square(size: size * 0.32, fill: col, stroke: none))

// Double hairline frame used on dark cards.
#let dark-frame = {
  place(center, rect(width: 100% - 46pt, height: 100% - 46pt, stroke: (paint: gold, thickness: 1.3pt)))
  place(center, rect(width: 100% - 58pt, height: 100% - 58pt, stroke: (paint: gold.lighten(30%), thickness: 0.6pt)))
}

// Small-caps label flanked by hairlines.
#let eyebrow-block(txt, col: ivory_muted, line-col: gold) = grid(
  columns: (1fr, auto, 1fr),
  column-gutter: 14pt,
  align: (right + horizon, center + horizon, left + horizon),
  line(length: 100%, stroke: (paint: line-col.lighten(20%), thickness: 0.7pt)),
  text(font: F.label, size: 8.5pt, fill: col, tracking: 2.8pt)[#txt],
  line(length: 100%, stroke: (paint: line-col.lighten(20%), thickness: 0.7pt)),
)

#let wordmark-footer(col: gold) = place(bottom + center, dy: -30pt)[
  #text(font: F.label, size: 8pt, fill: col, tracking: 1.5pt)[#wordmark]
]
