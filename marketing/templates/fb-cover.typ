// Facebook Page cover banner — 851x315pt display size, rendered at 2x
// (1702x630). Keep all text inside the central band: mobile crops the
// cover top/bottom. Not a feed post — excluded from calendar.md.
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)

#set page(width: 851pt, height: 315pt, margin: 0pt, fill: ink)
#set text(lang: "en")

#place(image(spec.photo, width: 100%, height: 100%, fit: "cover"))
#ink-veil(spec.at("veil", default: 42) * 1%)
#bottom-scrim(62%, 90%)
#top-scrim(38%, 72%)

#place(center + horizon)[
  #block(width: 88%)[
    #align(center)[
      #set par(leading: 1em)
      #kicker("A COZY MYSTERY SERIES BY VESPER BLYTHE", size: 10.5pt, tracking: 5pt, col: ivory-a(85%))
      #v(14pt)
      #text(font: (F.display, "Georgia"), weight: "bold", size: 44pt, fill: gold_light, tracking: 1.5pt)[The Blackwood Mysteries]
      #v(14pt)
      #line(length: 16%, stroke: (paint: gold, thickness: 1pt))
      #v(12pt)
      #text(font: (F.display, "Georgia"), size: 15.5pt, style: "italic", fill: ivory-a(94%), top-edge: "cap-height", bottom-edge: "descender")[Cozy mysteries from a small Virginia town where old money is built on old lies.]
      #v(12pt)
      #text(font: (F.kicker, "Avenir Next"), weight: 500, size: 10.5pt, fill: gold-a(95%), tracking: 4pt)[NOW ON KINDLE AND AUDIBLE]
    ]
  ]
]
