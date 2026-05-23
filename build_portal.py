#!/usr/bin/env python3
from __future__ import annotations

import html
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MEMO = Path("/Users/ntemis/Ntemis' Custody Files Against Efthimia Bakolouka/ΑΠΑΝΤΗΣΕΙΣ-PAKLEX-ΤΕΛΙΚΟ-2026-04-03.md")
OUT = ROOT / "index.html"

EVIDENCE = [
    ("Slack ΚΕΔΑΣΥ", "evidence/screenshots/slack-kedasy-initiative.png", "Πρωτοβουλία πατέρα για ΚΕΔΑΣΥ"),
    ("SMS Οικονόμου", "evidence/screenshots/SMS-Anna-Oikonomou-Fofi-Tzanni-19-20-Nov-2023.jpg", "Σύσταση Φώφης Τζάνη στον πατέρα"),
    ("Viber Τσεκούρα 1", "evidence/screenshots/viber-1.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 2", "evidence/screenshots/viber-2.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 3", "evidence/screenshots/viber-3.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 4", "evidence/screenshots/viber-4.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 5", "evidence/screenshots/viber-5.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 6", "evidence/screenshots/viber-6.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 7", "evidence/screenshots/viber-7.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 8", "evidence/screenshots/viber-8.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 9", "evidence/screenshots/viber-9.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 10", "evidence/screenshots/viber-10.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 11", "evidence/screenshots/viber-11.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 12", "evidence/screenshots/viber-12.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 13", "evidence/screenshots/viber-13.jpg", "Συνομιλία 2/1/2025"),
    ("Viber Τσεκούρα 14", "evidence/screenshots/viber-14.jpg", "Συνομιλία 2/1/2025"),
    ("Ψευδής τίτλος Τσεκούρα", "evidence/screenshots/Tsekoura-NOT-eidikos-paidagogos.png", "Screenshot Χατζηδάκη"),
    ("Screenshot 19/3/2026", "evidence/screenshots/Screenshot_2026-03-19_at_9.51.08_PM.png", "Συμπληρωματικό screenshot"),
    ("Γνωμάτευση Σταματοπούλου", "evidence/pdfs/stamatopoulou-gnomateysi.pdf", "F90.0 και εναντιωματικές συμπεριφορές"),
    ("Πόρισμα ΚΕΔΑΣΥ", "evidence/pdfs/kedasy-porisma.pdf", "Επίσημη κρατική αξιολόγηση"),
    ("Έκθεση Χατζηδάκη", "evidence/pdfs/chatzidakis-ekthesi.pdf", "Καθημερινή παρακολούθηση Αίαντα"),
    ("Email ΕΡΩΤΗΜΑΤΟΛΟΓΙΑ", "evidence/pdfs/email-erotimatologia.pdf", "Thread 28/11-9/12/2023"),
    ("Ένορκη Τσεκούρα", "evidence/pdfs/affidavit-tsekoura.pdf", "Πηγή ψευδών χωρίων"),
    ("Email Λέλα 5/12/2023", "evidence/pdfs/email-lela-ektimisi-5-12-2023.pdf", "Απόκρυψη εναντιωματικότητας"),
    ("Email Έφης 27/12/2024", "evidence/pdfs/email-effie-klironomiko-26-27-12-2024.pdf", "Άρνηση κληρονομικότητας"),
    ("Απάντηση Ντέμη 27/12/2024", "evidence/pdfs/email-ntemis-reply-klironomiko-27-12-2024.pdf", "Απάντηση στο κληρονομικό ιστορικό"),
    ("Σημείωμα Ίωνα", "evidence/photos/20230102_121921.jpg", "Πρωτοχρονιά 2022"),
    ("Έλεγχος προόδου Αίαντα", "evidence/photos/elegxos-proodou-ajax.jpg", "Μαθησιακή πρόοδος"),
]


def run_pandoc() -> str:
    return subprocess.check_output(
        [
            "pandoc",
            str(MEMO),
            "--from=gfm",
            "--to=html5",
            "--wrap=none",
            "--section-divs",
        ],
        text=True,
    )


def is_image(path: str) -> bool:
    return Path(path).suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def evidence_cards() -> str:
    cards = []
    for title, path, note in EVIDENCE:
        title_h = html.escape(title)
        note_h = html.escape(note)
        path_h = html.escape(path)
        if is_image(path):
            media = f'<button class="thumb image-thumb" data-src="{path_h}" title="Άνοιγμα εικόνας"><img src="{path_h}" alt="{title_h}" loading="lazy"></button>'
        else:
            media = f'<a class="thumb pdf-thumb" href="{path_h}" target="_blank" rel="noopener"><iframe src="{path_h}#page=1&toolbar=0&navpanes=0" loading="lazy" title="{title_h}"></iframe></a>'
        cards.append(
            f"""
            <article class="evidence-card">
              {media}
              <div class="evidence-meta">
                <h3>{title_h}</h3>
                <p>{note_h}</p>
                <a class="download" href="{path_h}" target="_blank" rel="noopener" download>Download</a>
              </div>
            </article>
            """
        )
    return "\n".join(cards)


def gallery_cards(folder: str, label: str, count: int) -> str:
    cards = []
    for i in range(1, count + 1):
        path = f"evidence/{folder}/{folder[:-1] if folder.endswith('s') else folder}-{i}.jpg"
        if folder == "photos":
            path = f"evidence/photos/svoronou-{i}.jpg"
        cards.append(
            f'<button class="gallery-item image-thumb" data-src="{path}" title="{html.escape(label)} {i}">'
            f'<img src="{path}" alt="{html.escape(label)} {i}" loading="lazy"><span>{html.escape(label)} {i}</span></button>'
        )
    return "\n".join(cards)


def page(body: str) -> str:
    return f"""<!doctype html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<title>ΑΠΑΝΤΗΣΕΙΣ ΣΕ MEMO PAKLEX — Evidence Portal</title>
<style>
:root {{
  color-scheme: dark;
  --bg: #101114;
  --panel: #17191f;
  --panel-2: #20232b;
  --line: #343946;
  --text: #e7e9ee;
  --muted: #a6adbb;
  --red: #f05d5e;
  --gold: #f0c35b;
  --blue: #70b7ff;
  --green: #63d293;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 16px/1.72 Georgia, "Times New Roman", serif;
}}
a {{ color: var(--blue); text-decoration-thickness: 1px; text-underline-offset: 3px; }}
strong {{ color: #fff; }}
em {{ color: var(--gold); }}
table {{ width: 100%; border-collapse: collapse; margin: 1rem 0 1.5rem; font-size: .94rem; }}
th, td {{ border: 1px solid var(--line); padding: .55rem .7rem; vertical-align: top; }}
th {{ color: var(--gold); background: var(--panel-2); text-align: left; }}
tr:nth-child(even) td {{ background: rgba(255,255,255,.025); }}
hr {{ border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }}
#gate {{
  position: fixed; inset: 0; z-index: 50;
  display: grid; place-items: center;
  background: #050506;
}}
#gate.hidden {{ display: none; }}
.gate-box {{
  width: min(92vw, 420px);
  border: 1px solid var(--line);
  background: var(--panel);
  padding: 2.2rem;
  border-radius: 8px;
  text-align: center;
}}
.gate-box h1 {{ margin: 0 0 .4rem; font-size: 1.2rem; letter-spacing: .08em; color: #fff; }}
.gate-box p {{ margin: 0 0 1.2rem; color: var(--muted); font-size: .9rem; }}
.gate-row {{ display: flex; gap: .6rem; }}
#gate-pw {{
  min-width: 0; flex: 1;
  border: 1px solid var(--line);
  background: #101114;
  color: #fff;
  border-radius: 6px;
  padding: .75rem .85rem;
  font: inherit;
}}
.gate-box button, .download, .nav button {{
  border: 1px solid var(--line);
  background: var(--panel-2);
  color: var(--text);
  border-radius: 6px;
  padding: .55rem .8rem;
  cursor: pointer;
  font: inherit;
}}
.gate-box button:hover, .download:hover, .nav button:hover {{ border-color: var(--blue); color: #fff; }}
#gate-error {{ min-height: 1.4rem; margin-top: .7rem; color: var(--red); font-size: .88rem; }}
.layout {{ display: grid; grid-template-columns: minmax(0, 1fr) 280px; gap: 2rem; width: min(1380px, 100%); margin: 0 auto; padding: 2rem; }}
main {{ min-width: 0; max-width: 900px; }}
.hero {{
  border-bottom: 2px solid var(--red);
  padding: 1rem 0 1.4rem;
  margin-bottom: 1.2rem;
}}
.hero h1 {{ margin: 0 0 .8rem; font-size: clamp(1.45rem, 3vw, 2.15rem); line-height: 1.18; color: #fff; }}
.hero p {{ margin: .25rem 0; color: var(--muted); }}
.memo {{
  background: transparent;
}}
.memo h1, .memo h2 {{
  color: #fff;
  border-left: 4px solid var(--red);
  background: var(--panel);
  padding: .7rem .9rem;
  margin: 2.2rem 0 .9rem;
  font-size: 1.3rem;
  line-height: 1.28;
}}
.memo h3 {{
  color: var(--gold);
  margin: 1.7rem 0 .6rem;
  font-size: 1.05rem;
}}
.memo p {{ margin: .75rem 0; }}
.memo li {{ margin: .35rem 0; }}
.memo blockquote {{
  margin: 1rem 0;
  border-left: 3px solid var(--gold);
  background: rgba(240,195,91,.08);
  padding: .8rem 1rem;
  color: #fff;
}}
.nav {{
  position: sticky;
  top: 1rem;
  align-self: start;
  border: 1px solid var(--line);
  background: var(--panel);
  border-radius: 8px;
  padding: 1rem;
  max-height: calc(100vh - 2rem);
  overflow: auto;
}}
.nav h2 {{ margin: 0 0 .75rem; color: #fff; font-size: 1rem; }}
.nav a {{ display: block; color: var(--muted); text-decoration: none; padding: .28rem 0; font-size: .9rem; }}
.nav a:hover {{ color: var(--blue); }}
.nav .actions {{ display: grid; gap: .45rem; margin-top: .9rem; }}
.evidence-section {{
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 2px solid var(--red);
}}
.evidence-section h2 {{ color: #fff; font-size: 1.35rem; }}
.evidence-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: .9rem;
  margin: 1rem 0 1.5rem;
}}
.evidence-card {{
  border: 1px solid var(--line);
  background: var(--panel);
  border-radius: 8px;
  overflow: hidden;
}}
.thumb {{
  display: block;
  width: 100%;
  height: 170px;
  border: 0;
  border-bottom: 1px solid var(--line);
  background: #0b0c0f;
  padding: 0;
  cursor: pointer;
  overflow: hidden;
}}
.thumb img, .gallery-item img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; display: block; }}
.pdf-thumb iframe {{ width: 100%; height: 100%; border: 0; pointer-events: none; background: #fff; }}
.evidence-meta {{ padding: .8rem; }}
.evidence-meta h3 {{ margin: 0 0 .25rem; font-size: .98rem; color: var(--gold); }}
.evidence-meta p {{ margin: 0 0 .7rem; color: var(--muted); font-size: .88rem; line-height: 1.45; }}
.download {{ display: inline-block; text-decoration: none; font-size: .86rem; }}
.gallery {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: .65rem;
  margin: 1rem 0 1.5rem;
}}
.gallery-item {{
  border: 1px solid var(--line);
  background: var(--panel);
  color: var(--muted);
  border-radius: 7px;
  padding: 0;
  overflow: hidden;
  cursor: pointer;
  text-align: left;
}}
.gallery-item img {{ height: 130px; }}
.gallery-item span {{ display: block; padding: .45rem .55rem; font-size: .8rem; }}
#lightbox {{
  display: none;
  position: fixed; inset: 0; z-index: 60;
  background: rgba(0,0,0,.94);
  align-items: center; justify-content: center;
  padding: 2rem;
}}
#lightbox.active {{ display: flex; }}
#lightbox img {{ max-width: 94vw; max-height: 90vh; object-fit: contain; }}
.lb-actions {{ position: fixed; top: 1rem; right: 1rem; display: flex; gap: .6rem; }}
.lb-actions a, .lb-actions button {{
  width: 42px; height: 42px;
  border: 1px solid var(--line);
  background: var(--panel);
  color: #fff;
  border-radius: 50%;
  display: grid; place-items: center;
  text-decoration: none;
  cursor: pointer;
  font-size: 1.1rem;
}}
.top-link {{
  position: fixed; right: 1rem; bottom: 1rem;
  width: 42px; height: 42px;
  display: grid; place-items: center;
  border: 1px solid var(--line);
  border-radius: 50%;
  background: var(--panel);
  color: #fff;
  text-decoration: none;
}}
@media (max-width: 980px) {{
  .layout {{ display: block; padding: 1rem; }}
  .nav {{ position: static; max-height: none; margin-bottom: 1rem; }}
  table {{ display: block; max-width: 100%; overflow-x: auto; }}
  th, td {{ overflow-wrap: anywhere; }}
}}
@media print {{
  #gate, .nav, #lightbox, .top-link {{ display: none !important; }}
  body {{ background: white; color: black; }}
  .layout {{ display: block; padding: 0; }}
  .memo h1, .memo h2 {{ color: black; background: white; }}
  a {{ color: black; }}
}}
</style>
</head>
<body>
<div id="gate">
  <form class="gate-box" id="gate-form">
    <h1>PAKLEX EVIDENCE</h1>
    <p>Λατσούδης κατά Μπακολούκα · εμπιστευτικό</p>
    <div class="gate-row">
      <input id="gate-pw" type="password" placeholder="Κωδικός" autocomplete="off" autofocus>
      <button type="submit">Είσοδος</button>
    </div>
    <div id="gate-error"></div>
  </form>
</div>

<div id="lightbox" aria-hidden="true">
  <div class="lb-actions">
    <a id="lb-download" href="#" download title="Download">↓</a>
    <button id="lb-close" type="button" title="Κλείσιμο">×</button>
  </div>
  <img id="lb-img" src="" alt="">
</div>

<div class="layout" id="page">
  <main>
    <header class="hero">
      <h1>ΑΠΑΝΤΗΣΕΙΣ ΣΕ MEMO PAKLEX — Μήνυση κατά Τσεκούρα</h1>
      <p>Πηγή: τελικό memo 3 Απριλίου 2026. Κωδικός portal: paklex2026.</p>
      <p>Όλα τα εξωτερικά και αποδεικτικά links ανοίγουν σε νέο tab.</p>
    </header>
    <article class="memo">
      {body}
    </article>

    <section class="evidence-section" id="evidence-library">
      <h2>Αποδεικτικά Downloads</h2>
      <p>Πλήρης βιβλιοθήκη αποδεικτικών που υπάρχει στο repository. Τα PDF εμφανίζονται ως ενσωματωμένη πρώτη σελίδα όπου το υποστηρίζει ο browser.</p>
      <div class="evidence-grid">
        {evidence_cards()}
      </div>

      <h2>Φωτογραφίες Πρέβεζας</h2>
      <div class="gallery">
        {gallery_cards("preveza", "Πρέβεζα", 6)}
      </div>

      <h2>Φωτογραφίες Σβορώνου</h2>
      <div class="gallery">
        {gallery_cards("photos", "Σβορώνου", 39)}
      </div>
    </section>
  </main>

  <aside class="nav">
    <h2>Πλοήγηση</h2>
    <a href="#πλαισιο">Πλαίσιο</a>
    <a href="#γιατι-η-τσεκουρα-ειναι-ιδιαιτερα-υπολογη">Γιατί είναι υπόλογη</a>
    <a href="#εισαγωγικεσ-παρατηρησεισ--τρεις-κρίσιμες-επισημάνσεις">Εισαγωγικές παρατηρήσεις</a>
    <a href="#επι-των-ψευδων-χωριων">Επί των ψευδών χωρίων</a>
    <a href="#εκκρεμουν">Εκκρεμούν</a>
    <a href="#αποδεικτικα--13-τεκμηρια-ολα-διαθεσιμα">Αποδεικτικά</a>
    <a href="#evidence-library">Evidence Library</a>
    <div class="actions">
      <button type="button" id="unlock-dev">Unlock</button>
      <button type="button" id="print-page">Print</button>
    </div>
  </aside>
</div>
<a class="top-link" href="#page" title="Επάνω">↑</a>

<script>
const EXPECTED = 'b9cf7ae9f816157d4a15a092d4c5949f0c632828f5330957365b548b3a43c658';
async function sha256(text) {{
  const data = new TextEncoder().encode(text);
  const hash = await crypto.subtle.digest('SHA-256', data);
  return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
}}
function unlock() {{
  document.getElementById('gate').classList.add('hidden');
  sessionStorage.setItem('paklexUnlocked', '1');
}}
document.getElementById('gate-form').addEventListener('submit', async event => {{
  event.preventDefault();
  const input = document.getElementById('gate-pw');
  const ok = await sha256(input.value);
  if (ok === EXPECTED) unlock();
  else document.getElementById('gate-error').textContent = 'Λάθος κωδικός';
}});
if (sessionStorage.getItem('paklexUnlocked') === '1') unlock();
document.getElementById('unlock-dev').addEventListener('click', () => document.getElementById('gate-pw').focus());
document.getElementById('print-page').addEventListener('click', () => window.print());
document.querySelectorAll('a[href]').forEach(a => {{
  const href = a.getAttribute('href') || '';
  if (href.startsWith('#')) return;
  a.target = '_blank';
  a.rel = 'noopener';
}});
const lightbox = document.getElementById('lightbox');
const lbImg = document.getElementById('lb-img');
const lbDownload = document.getElementById('lb-download');
document.querySelectorAll('.image-thumb').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const src = btn.dataset.src || btn.querySelector('img')?.getAttribute('src');
    if (!src) return;
    lbImg.src = src;
    lbDownload.href = src;
    lbDownload.download = src.split('/').pop();
    lightbox.classList.add('active');
    lightbox.setAttribute('aria-hidden', 'false');
  }});
}});
function closeLightbox() {{
  lightbox.classList.remove('active');
  lightbox.setAttribute('aria-hidden', 'true');
  lbImg.src = '';
}}
document.getElementById('lb-close').addEventListener('click', closeLightbox);
lightbox.addEventListener('click', event => {{ if (event.target === lightbox) closeLightbox(); }});
document.addEventListener('keydown', event => {{ if (event.key === 'Escape') closeLightbox(); }});
</script>
</body>
</html>
"""


def main() -> None:
    if not MEMO.exists():
        raise SystemExit(f"Missing memo: {MEMO}")
    body = run_pandoc()
    OUT.write_text(page(body), encoding="utf-8")


if __name__ == "__main__":
    main()
