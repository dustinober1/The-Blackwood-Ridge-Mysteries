// Town post — "A Visitor's Guide to Blackwood Ridge" location card.
// Requires sys.inputs.art (ridge_art SVG). Spec fields: size (square|
// portrait), eyebrow, plate, headline, sub, headline_size (optional).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)
#let portrait = spec.at("size", default: "square") == "portrait"
#let ph = if portrait { 675pt } else { 540pt }
#let hsize = spec.at("headline_size", default: 30)

#set page(width: 540pt, height: ph, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(image(sys.inputs.art, width: 100%, height: 100%, fit: "cover"))
// Legibility scrim over the lower half for the headline block.
#place(bottom, rect(width: 100%, height: 72%, fill: gradient.linear(ink_0, ink_90, angle: 180deg)))
#place(top + center, dy: 46pt)[
  #text(font: F.label, size: 8.5pt, fill: ivory_muted, tracking: 3.2pt)[#spec.eyebrow]
]
#place(center + horizon, dy: if portrait { 96pt } else { 54pt })[
  #block(width: 86%)[
    #align(center)[
      #set par(leading: 0.5em)
      #text(font: F.label, size: 8pt, fill: gold.lighten(20%), tracking: 3pt)[#spec.plate]
      #v(10pt)
      #text(font: F.label, weight: "bold", size: hsize * 1pt, fill: gold_light, tracking: 3pt)[#spec.headline]
      #v(13pt)
      #line(length: 30%, stroke: (paint: gold, thickness: 0.9pt))
      #v(13pt)
      #text(font: (F.display, "Georgia"), size: 14.5pt, style: "italic", fill: ivory, top-edge: "cap-height", bottom-edge: "descender")[#spec.sub]
    ]
  ]
]
#place(top + center, dy: 64pt, fleuron(size: 8pt, col: gold.lighten(10%)))
#wordmark-footer()
