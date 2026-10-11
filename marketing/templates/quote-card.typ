// Quote card — verbatim book quote over a darkened photographic texture.
// Spec fields: photo, quote, attribution, book_line, quote_size (pt,
// optional, default 31), veil (optional, %).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let qsize = spec.at("quote_size", default: 31)

#set page(width: 540pt, height: 540pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(image(spec.photo, width: 100%, height: 100%, fit: "cover"))
#ink-veil(spec.at("veil", default: 80) * 1%)
#bottom-scrim(40%, 55%)

#place(center + horizon, dy: -8pt)[
  #block(width: 84%)[
    #align(center)[
      #set par(leading: 0.55em)
      #text(font: (F.display, "Georgia"), size: qsize * 1pt, style: "italic", fill: ivory, hyphenate: false, top-edge: "cap-height", bottom-edge: "baseline")[#spec.quote]
      #v(24pt)
      #line(length: 13%, stroke: (paint: gold, thickness: 1pt))
      #v(15pt)
      #text(font: (F.kicker, "Avenir Next"), weight: 500, size: 9.5pt, fill: gold_light, tracking: 4pt)[#spec.attribution]
      #if spec.at("book_line", default: none) != none [
        #v(6pt)
        #text(font: (F.kicker, "Avenir Next"), weight: 400, size: 7.5pt, fill: ivory-a(58%), tracking: 2.5pt)[#spec.book_line]
      ]
    ]
  ]
]
#wordmark-footer()
