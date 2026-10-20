# Pathfinder Nomenclature Trainer

Interactive study tool for U.S. Army Pathfinder School nomenclature: sling load equipment, A-22 cargo bag, 5K/10K cargo nets, M1101 trailer, M1151 HMMWV, triple blivets and the M1301 ISV. Every numbered callout from the source slides is a tappable hotspot on the photo, with rated capacities, lifting provisions and sizes.

Modes: Study (photos with hotspots, hide-names self-test), Flashcards (spaced repetition, photo on front / answer / off), Quiz (name it, find it on the photo, rated capacity, sizes and tables), Tables, Progress.

## Run it

Open `index.html` in a browser. No build step and no server needed; progress is saved in the browser's local storage.

## Files

- `index.html` – the whole app (page, styles, script and data)
- `img/` – photos extracted from the source decks
- `template.html`, `build_data.py`, `data.json` – source used to generate `index.html`

Rebuild after editing data: `python3 build_data.py` then merge `data.json` into `template.html` at the `__DATA__` placeholder (see `build.py`).
