// Cover feature — portrait 1080x1350 book promo card.
// Spec fields: book (key into brand.yaml books), hook (optional override).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let book = brand.books.at(spec.book)

#set page(width: 540pt, height: 675pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(top + center, dy: 44pt, block(width: 86%, eyebrow-block("THE BLACKWOOD RIDGE MYSTERIES · " + upper(book.number))))
// Cover art with a drop slab and hairline frame.
#place(center + horizon, dy: -38pt, dx: 7pt, rect(width: 296pt, height: 444pt, fill: ink_warm))
#place(center + horizon, dy: -40pt, image(book.cover, width: 296pt, height: 444pt, fit: "cover"))
#place(center + horizon, dy: -40pt, rect(width: 296pt, height: 444pt, stroke: (paint: gold.lighten(25%), thickness: 1pt)))

#place(bottom + center, dy: -58pt)[
  #block(width: 88%)[
    #align(center)[
      #set par(leading: 1.4em)
      #text(font: (F.display, "Georgia"), weight: "bold", size: 24pt, fill: gold_light, tracking: 1pt)[#upper(book.title)]
      #v(8pt)
      #text(font: (F.body, "Georgia"), size: 12pt, style: "italic", fill: ivory_muted)[#spec.at("hook", default: book.hook)]
      #v(12pt)
      #text(font: F.label, size: 8.5pt, fill: gold, tracking: 2.4pt)[#book.availability]
    ]
  ]
]
#wordmark-footer()
