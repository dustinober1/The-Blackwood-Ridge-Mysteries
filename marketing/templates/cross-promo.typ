// Cross-promo — reading-order card, two covers over a darkened photograph.
// Spec fields: photo, covers (two brand.yaml book keys), tagline,
// veil (optional %).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let b1 = brand.books.at(spec.covers.at(0))
#let b2 = brand.books.at(spec.covers.at(1))

#let promo-col(book, num, label) = grid(
  rows: (auto, auto, auto, auto),
  row-gutter: 10pt,
  align: center + horizon,
  circle(radius: 14.5pt, fill: ink-a(65%), stroke: (paint: gold, thickness: 1.2pt))[
    #text(font: F.label, size: 12.5pt, fill: gold_light)[#num]
  ],
  box(stroke: (paint: gold-a(60%), thickness: 1.2pt), image(book.cover, height: 272pt, fit: "cover")),
  text(font: (F.kicker, "Avenir Next"), weight: 500, size: 9pt, fill: gold_light, tracking: 3.5pt)[#label],
  text(font: F.label, size: 7.5pt, fill: ivory-a(78%), tracking: 1.8pt)[#upper(book.title)],
)

#set page(width: 540pt, height: 540pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(image(spec.photo, width: 100%, height: 100%, fit: "cover"))
#ink-veil(spec.at("veil", default: 78) * 1%)
#bottom-scrim(44%, 62%)

#place(top + center, dy: 38pt, block(width: 86%, eyebrow-block("THE BLACKWOOD RIDGE MYSTERIES · READING ORDER")))

#place(center + horizon, dy: -14pt)[
  #grid(
    columns: (auto, auto, auto),
    column-gutter: 26pt,
    align: (horizon, horizon, horizon),
    promo-col(b1, "1", "START HERE"),
    grid(
      rows: (auto, auto, auto),
      row-gutter: 7pt,
      align: center + horizon,
      line(angle: 90deg, length: 46pt, stroke: (paint: gold-a(50%), thickness: 0.8pt)),
      rotate(45deg, origin: center, square(size: 5pt, fill: gold-a(80%), stroke: none)),
      line(angle: 90deg, length: 46pt, stroke: (paint: gold-a(50%), thickness: 0.8pt)),
    ),
    promo-col(b2, "2", "THEN THIS"),
  )
]

#place(bottom + center, dy: -64pt)[
  #align(center)[
    #line(length: 22%, stroke: (paint: gold, thickness: 1pt))
    #v(10pt)
    #text(font: (F.display, "Georgia"), size: 16pt, style: "italic", fill: gold_light)[#spec.tagline]
  ]
]
#wordmark-footer()
