// Cover feature — portrait 1080x1350 book promo over a darkened still life.
// Spec fields: photo, book (key into brand.yaml books), hook (optional
// override), veil (optional %).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let book = brand.books.at(spec.book)

#set page(width: 540pt, height: 675pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(image(spec.photo, width: 100%, height: 100%, fit: "cover"))
#ink-veil(spec.at("veil", default: 72) * 1%)
#bottom-scrim(50%, 84%)

#place(top + center, dy: 36pt, block(width: 86%, eyebrow-block("THE BLACKWOOD RIDGE MYSTERIES · " + upper(book.number))))

#place(center + horizon, dy: -54pt, image(book.cover, width: 318pt, height: 477pt, fit: "cover"))
#place(center + horizon, dy: -54pt, rect(width: 318pt, height: 477pt, stroke: (paint: gold-a(55%), thickness: 1pt)))

#place(bottom + center, dy: -50pt)[
  #block(width: 88%)[
    #align(center)[
      #set par(leading: 1.2em)
      #text(font: (F.display, "Georgia"), weight: "bold", size: 20pt, fill: gold_light, tracking: 1.5pt)[#upper(book.title)]
      #v(7pt)
      #text(font: (F.body, "Georgia"), size: 13pt, style: "italic", fill: ivory-a(92%))[#spec.at("hook", default: book.hook)]
      #v(11pt)
      #text(font: (F.kicker, "Avenir Next"), weight: 500, size: 8.5pt, fill: gold-a(95%), tracking: 3pt)[#book.availability]
    ]
  ]
]
#wordmark-footer()
