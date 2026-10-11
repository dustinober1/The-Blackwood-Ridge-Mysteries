// Quote card — 1080x1080. Spec fields: quote, attribution, book_line,
// quote_size (pt, optional, default 24).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let qsize = spec.at("quote_size", default: 24)

#set page(width: 540pt, height: 540pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#dark-frame
#place(center + horizon, dy: -6pt)[
  #block(width: 82%)[
    #align(center)[
      #set par(leading: 0.5em)
      #fleuron()
      #v(16pt)
      #text(font: (F.display, "Georgia"), size: qsize * 1pt, style: "italic", fill: ivory, hyphenate: false, top-edge: "cap-height", bottom-edge: "baseline")[#spec.quote]
      #v(20pt)
      #line(length: 24%, stroke: (paint: gold, thickness: 0.8pt))
      #v(14pt)
      #text(font: F.label, size: 10pt, fill: gold_light, tracking: 2.6pt)[#spec.attribution]
      #if spec.at("book_line", default: none) != none [
        #v(5pt)
        #text(font: F.label, size: 7.5pt, fill: ivory_muted.lighten(12%), tracking: 1.8pt)[#spec.book_line]
      ]
    ]
  ]
]
#place(top + center, dy: 36pt, fleuron(size: 9pt, col: gold.lighten(15%)))
#wordmark-footer()
