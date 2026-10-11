// Case file — typewritten records card on ivory paper, 1080x1080.
// Spec fields: stamp, fields (label/value list; __R__ in a value becomes a
// redaction bar), note (optional), options (optional list of
// {stamp, note} engagement verdicts).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)

#let redact-bars = (3.4em, 5.2em, 2.6em, 4.6em, 3.8em, 6em)
#let field-value(v) = {
  let segs = v.split("__R__")
  let out = ()
  for (i, s) in segs.enumerate() {
    if i > 0 {
      out.push(box(width: redact-bars.at(calc.rem(i - 1, redact-bars.len())), height: 0.62em, fill: ink, outset: (top: 0.1em), radius: 0.5pt))
    }
    out.push(s)
  }
  out.join()
}

#let option-stamp(o, tilt) = rotate(tilt, origin: center)[
  #box(stroke: (paint: ink.darken(5%), thickness: 1.8pt), inset: (x: 16pt, y: 9pt))[
    #align(center)[
      #text(font: F.label, weight: "bold", size: 12.5pt, fill: ink, tracking: 2.2pt)[#o.stamp]
      #v(3pt)
      #text(font: F.label, size: 7pt, fill: gold_shadow.darken(10%), tracking: 1.5pt)[#o.note]
    ]
  ]
]

#set page(width: 540pt, height: 540pt, margin: 0pt, fill: ivory)
#set text(lang: "en", fill: ink)

// Paper warmth and edge shading.
#place(rect(width: 100%, height: 100%, fill: gradient.radial(rgb(245, 226, 176, 20%), rgb(247, 242, 228, 0%))))
#place(rect(width: 100%, height: 100%, fill: gradient.radial(rgb(14, 6, 15, 0%), rgb(14, 6, 15, 9%))))
// Paper edge and coffee ring.
#place(center, rect(width: 100% - 30pt, height: 100% - 30pt, stroke: (paint: ink.darken(15%), thickness: 1pt)))
#place(top + right, dx: -54pt, dy: 48pt, circle(radius: 30pt, stroke: (paint: gold_shadow.lighten(42%), thickness: 2.4pt)))
#place(top + right, dx: -47pt, dy: 55pt, circle(radius: 23pt, stroke: (paint: gold_shadow.lighten(52%), thickness: 1pt)))

#place(top + center, dy: 46pt)[
  #text(font: F.label, size: 9pt, fill: ink.darken(5%), tracking: 3.2pt)[BLACKWOOD RIDGE COUNTY RECORDS]
]
#place(top + center, dy: 78pt)[
  #rotate(-3.5deg, origin: center)[
    #box(stroke: (paint: gold_shadow, thickness: 1.6pt), inset: (x: 13pt, y: 6.5pt))[
      #text(font: F.label, weight: "bold", size: 13pt, fill: gold_shadow.darken(8%), tracking: 2.2pt)[#spec.stamp]
    ]
  ]
]

#place(center + horizon, dy: 14pt)[
  #block(width: 78%)[
    #set par(leading: 1.5em)
    #grid(
      columns: (88pt, 1fr),
      column-gutter: 12pt,
      row-gutter: 11pt,
      align: (right + top, left + top),
      ..spec.fields.map(f => (
        text(font: F.label, size: 7.8pt, fill: gold_shadow.darken(15%), tracking: 1.2pt)[#f.label],
        text(font: (F.typewriter, "Courier New"), size: 11pt)[#field-value(f.value)],
      )).flatten()
    )
    #if spec.at("note", default: none) != none [
      #v(15pt)
      #block(width: 100%, inset: (x: 11pt, y: 9pt), stroke: (left: (paint: gold, thickness: 2pt)))[
        #set par(leading: 0.7em)
        #text(font: (F.typewriter, "Courier New"), size: 10.5pt, style: "italic", top-edge: "cap-height", bottom-edge: "baseline")[#spec.note]
      ]
    ]
  ]
]

#if spec.at("options", default: none) != none [
  #place(bottom + center, dy: -62pt)[
    #grid(
      columns: (auto, auto),
      column-gutter: 46pt,
      align: center + horizon,
      option-stamp(spec.options.at(0), -3deg),
      option-stamp(spec.options.at(1), 3deg),
    )
  ]
]

#place(bottom + center, dy: -34pt)[
  #align(center)[
    #fleuron(size: 8pt, col: gold_shadow.lighten(25%))
    #v(2pt)
    #text(font: F.label, size: 7pt, fill: gold_shadow.darken(10%), tracking: 2.2pt)[FROM THE MARGINS OF THE BLACKWOOD RIDGE MYSTERIES]
  ]
]
