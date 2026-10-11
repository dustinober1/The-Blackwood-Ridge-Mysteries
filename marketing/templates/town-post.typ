// Town post — "A Visitor's Guide to Blackwood Ridge" location card.
// Full-bleed photograph, lower-third type block.
// Spec fields: photo, size (square|portrait), eyebrow, plate, headline,
// sub, headline_size (optional, pt).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let portrait = spec.at("size", default: "square") == "portrait"
#let ph = if portrait { 675pt } else { 540pt }
#let hsize = spec.at("headline_size", default: 34)

#set page(width: 540pt, height: ph, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(image(spec.photo, width: 100%, height: 100%, fit: "cover"))
#ink-veil(spec.at("veil", default: 30) * 1%)
#bottom-scrim(74%, 94%)
#top-scrim(28%, 58%)

#place(top + center, dy: 32pt, kicker(spec.eyebrow))

#place(bottom + center, dy: -44pt)[
  #block(width: 88%)[
    #align(center)[
      #set par(leading: 0.9em)
      #text(font: (F.kicker, "Avenir Next"), weight: 500, size: 8.5pt, fill: gold-a(90%), tracking: 5pt)[#spec.plate]
      #v(10pt)
      #text(font: (F.display, "Georgia"), weight: 900, size: hsize * 1pt, fill: gold_light, tracking: 1.2pt)[#spec.headline]
      #v(13pt)
      #line(length: 20%, stroke: (paint: gold, thickness: 1pt))
      #v(13pt)
      #text(font: (F.display, "Georgia"), size: 15pt, style: "italic", fill: ivory-a(95%), top-edge: "cap-height", bottom-edge: "descender")[#spec.sub]
    ]
  ]
]
#wordmark-footer()
