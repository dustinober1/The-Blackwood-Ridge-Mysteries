# Launch-Month Content Calendar — The Blackwood Ridge Mysteries

Twelve posts, three per week (Mon / Wed / Fri), four weeks. Dates assume the
page launches the week of **2026-10-19**; if account setup slips, shift the
whole grid rather than dropping posts. Suggested time: **10:00 AM Eastern**
(cozy readers scroll late morning and late evening; Insights will refine
this after two weeks).

Every post ships to **both** Instagram and Facebook the same day. The PNG in
`generated/` is the image; the caption, hashtags, and alt text live in the
post's YAML under `social:`. On Facebook, post the caption as-is and drop
the store link in the first comment (links in the caption itself suppress
reach). On Instagram, paste the alt text into the alt-text field when
publishing — Business Suite supports this natively.

| # | Date (2026) | Slug | Card | Hook |
|---|---|---|---|---|
| 001 | Mon Oct 19 | `001-welcome-to-the-ridge` | Town post (Blue Ridge) | Page launch; pin this post |
| 002 | Wed Oct 21 | `002-quote-eleanor` | Quote card | Eleanor's lesson; "who taught you to look closely?" |
| 003 | Fri Oct 23 | `005-case-file-wren` | Case file | Founding discrepancy; "wrong answers only" |
| 004 | Mon Oct 26 | `004-cover-b1` | Cover feature (4:5) | Book One pitch + availability |
| 005 | Wed Oct 28 | `003-town-square` | Town post (Grimshaw) | The square; "where would you sit?" |
| 006 | Fri Oct 30 | `008-readers-verdict` | Case file + verdict stamps | Publish or bury? A/B engagement post |
| 007 | Mon Nov 2 | `007-the-foxed-page` | Town post (bookshop) | The bookshop; "the shop that raised you" |
| 008 | Wed Nov 4 | `006-quote-wren` | Quote card | The Wren cipher; callback to the case file |
| 009 | Fri Nov 6 | `011-case-file-pike` | Case file | The appraiser at the auction house |
| 010 | Mon Nov 9 | `010-ralston-hall` | Town post (mansion) | Ralston Hall; the conspiracy centerpiece |
| 011 | Wed Nov 11 | `009-quote-rain` | Quote card | Chapter-one atmosphere; "weather you want to live in" |
| 012 | Fri Nov 13 | `012-start-the-series` | Cover feature (4:5) | Month close; start-here CTA for Book One |

## Held: Book Two assets

Book Two is **not** advertised in month one — the pages hold until its
audiobook is live. The finished specs are parked in `posts/hold/`
(excluded from `generate.py all`):

- `hold/010-cover-b2.yaml` — Book Two cover feature (update its
  availability line from "coming soon to Audible" to "Now on Audible"
  before releasing)
- `hold/011-case-file-dabney.yaml` — Marguerite Dabney case file
- `hold/012-start-here.yaml` — two-book reading-order card
- `hold/006-quote-town.yaml` — the "They did not hate her…" quote card

When the audiobook drops: move the files back into `posts/`, regenerate,
and slot them into month two's calendar (the violet-plate and cover
backgrounds are already in `assets/photos/`).

## Rhythm notes

- **Grid balance**: dark art cards and light case files alternate so the
  profile grid never shows more than two same-background cards in a row.
- **Engagement posts** (003, 006, plus the question CTAs on most captions)
  are the growth engine — reply to every comment in the first hour. That
  task is human; do not automate replies.
- **Week 4** funnels: Ralston Hall (the conspiracy centerpiece) → the rain
  quote → the start-here close, so a reader who arrived mid-month gets the
  full on-ramp to Book One.
- **Pin** 001 on Instagram and Facebook for the whole month.
- After week 2, check Insights: if case files outperform town posts, rebalance
  month two toward case files and quotes.

## The automation boundary

Scheduling through **Meta Business Suite** (official) is fine. Do **not**
GUI-automate posting, following, liking, or commenting on a new Meta account
— that is the fastest way to get a brand-new page restricted. The intended
loop: generate cards here, review them, batch-schedule a month in Business
Suite in one sitting, then use computer use only for setup, research, and QA
sweeps.
