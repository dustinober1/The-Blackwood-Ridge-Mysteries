// Case file — typewritten records laid over a period document photograph
// (survey map, botanical plate, handwritten letter).
// Spec fields: photo, veil (optional %, default 70), stamp, fields
// (label/value; __R__ becomes a redaction bar), note (optional),
// options (optional {stamp, note} list for engagement verdicts).
#import "lib.typ": *

#let spec = yaml(sys.inputs.spec)

#let redact-bars = (3.4em, 5.2em, 2.6em, 4.6em, 3.8em, 6em)
#let field-value(v) = {
  let segs = v.split("__R__")
  let out = ()
  for (i, s) in segs.enumerate() {
    if i > 0 {
      out.push(box(width: redact-bars.at(calc.rem(i - 1, redact-bars.len())), height: 0.62em, fill: ink-a(92%), outset: (top: 0.1em), radius: 0.5pt))
    }
    out.push(s)
  }
  out.join()
}

#let option-stamp(o, tilt) = rotate(tilt, origin: center)[
  #box(stroke: (paint: stamp_red, thickness: 2pt), inset: (x: 16pt, y: 9pt))[
    #align(center)[
      #text(font: F.label, weight: "bold", size: 12.5pt, fill: stamp_red, tracking: 2.2pt)[#o.stamp]
      #v(3pt)
      #text(font: (F.kicker, "Avenir Next"), weight: 500, size: 7pt, fill: ink-a(70%), tracking: 2pt)[#o.note]
    ]
  ]
]

#set page(width: 540pt, height: 540pt, margin: 0pt, fill: ivory)
#set text(lang: "en", fill: ink)

#place(image(spec.photo, width: 100%, height: 100%, fit: "cover"))
#ivory-veil(spec.at("veil", default: 70) * 1%)
#place(rect(width: 100%, height: 100%, fill: gradient.radial(ink-a(0%), ink-a(16%))))

#place(top + center, dy: 42pt)[
  #text(font: F.label, size: 9.5pt, fill: ink-a(82%), tracking: 3.5pt)[BLACKWOOD RIDGE COUNTY RECORDS]
]
#place(top + center, dy: 78pt)[
  #rotate(-3.5deg, origin: center)[
    #box(stroke: (paint: stamp_red, thickness: 1.8pt), inset: (x: 13pt, y: 6.5pt))[
      #text(font: F.label, weight: "bold", size: 13.5pt, fill: stamp_red, tracking: 2.5pt)[#spec.stamp]
    ]
  ]
]

#place(center + horizon, dy: 14pt)[
  #block(width: 80%)[
    #set par(leading: 1.35em)
    #grid(
      columns: (86pt, 1fr),
      column-gutter: 12pt,
      row-gutter: 11pt,
      align: (right + top, left + top),
      ..spec.fields.map(f => (
        text(font: F.label, size: 8pt, fill: stamp_red.darken(6%), tracking: 1.4pt)[#f.label],
        text(font: (F.typewriter, "Courier New"), size: 11.5pt, fill: ink-a(92%))[#field-value(f.value)],
      )).flatten()
    )
    #if spec.at("note", default: none) != none [
      #v(16pt)
      #block(width: 100%, inset: (x: 11pt, y: 9pt), stroke: (left: (paint: gold, thickness: 2.2pt)))[
        #set par(leading: 0.75em)
        #text(font: (F.typewriter, "Courier New"), size: 11pt, style: "italic", fill: ink-a(88%), top-edge: "cap-height", bottom-edge: "baseline")[#spec.note]
      ]
    ]
  ]
]

#if spec.at("options", default: none) != none [
  #place(bottom + center, dy: -60pt)[
    #grid(
      columns: (auto, auto),
      column-gutter: 46pt,
      align: center + horizon,
      option-stamp(spec.options.at(0), -3deg),
      option-stamp(spec.options.at(1), 3deg),
    )
  ]
]

#place(bottom + center, dy: -28pt)[
  #text(font: (F.kicker, "Avenir Next"), weight: 500, size: 7.5pt, fill: ink-a(62%), tracking: 3pt)[FROM THE MARGINS OF THE BLACKWOOD RIDGE MYSTERIES]
]
