// Cross-promo — reading-order card with two covers, 1080x1080.
// Spec fields: covers (two brand.yaml book keys), tagline.
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let b1 = brand.books.at(spec.covers.at(0))
#let b2 = brand.books.at(spec.covers.at(1))

#let promo-col(book, num, label) = grid(
  rows: (auto, auto, auto, auto),
  row-gutter: 9pt,
  align: center + horizon,
  circle(radius: 14pt, stroke: (paint: gold, thickness: 1.1pt))[
    #text(font: F.label, size: 12.5pt, fill: gold_light)[#num]
  ],
  box(stroke: (paint: gold.lighten(25%), thickness: 1pt), image(book.cover, height: 246pt, fit: "cover")),
  text(font: F.label, size: 9pt, fill: gold_light, tracking: 2.4pt)[#label],
  text(font: F.label, size: 7pt, fill: ivory_muted, tracking: 1.6pt)[#upper(book.title)],
)

#set page(width: 540pt, height: 540pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(top + center, dy: 44pt, block(width: 86%, eyebrow-block("THE BLACKWOOD RIDGE MYSTERIES · READING ORDER")))
#place(center + horizon, dy: -18pt)[
  #grid(
    columns: (auto, auto, auto),
    column-gutter: 24pt,
    align: (horizon, horizon, horizon),
    promo-col(b1, "1", "START HERE"),
    grid(
      rows: (auto, auto, auto),
      row-gutter: 7pt,
      align: center + horizon,
      line(angle: 90deg, length: 52pt, stroke: (paint: gold.lighten(30%), thickness: 0.8pt)),
      fleuron(size: 11pt),
      line(angle: 90deg, length: 52pt, stroke: (paint: gold.lighten(30%), thickness: 0.8pt)),
    ),
    promo-col(b2, "2", "THEN THIS"),
  )
]
#place(bottom + center, dy: -74pt)[
  #align(center)[
    #line(length: 26%, stroke: (paint: gold, thickness: 0.8pt))
    #v(10pt)
    #text(font: (F.display, "Georgia"), size: 15pt, style: "italic", fill: gold_light)[#spec.tagline]
  ]
]
#wordmark-footer()
