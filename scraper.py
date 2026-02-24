import requests, pdfplumber, json, re, os, time

BASE = "https://science.osti.gov/-/media/wdts/nsb/pdf"

PDF_LIST = []

# ── MS Sets ────────────────────────────────────────────────────────────────────

# MS Set 1 — m_round01.pdf (18 rounds)
for r in range(1, 19):
    PDF_LIST.append(("MS", 1, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-1/m_round{r:02d}.pdf"))

# MS Set 2 — sample_questions_r{n}.pdf (10 rounds)
for r in range(1, 11):
    PDF_LIST.append(("MS", 2, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-2/sample_questions_r{r}.pdf"))

# MS Set 3 — Round-{n}C-MS.pdf (15 rounds)
for r in range(1, 16):
    PDF_LIST.append(("MS", 3, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-3/Round-{r}C-MS.pdf"))

# MS Set 4 — Round{n}.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 4, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-4/Round{r}.pdf"))

# MS Set 5 — Round{n}.pdf (16 rounds)
for r in range(1, 17):
    PDF_LIST.append(("MS", 5, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-5/Round{r}.pdf"))

# MS Set 6 — Round{n}.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 6, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-6/Round{r}.pdf"))

# MS Set 7 — MS_Round-{n}.pdf (15 rounds)
for r in range(1, 16):
    PDF_LIST.append(("MS", 7, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-7/MS_Round-{r}.pdf"))

# MS Set 8 — Round-{n}-A.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 8, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-8/Round-{r}-A.pdf"))

# MS Set 9 — RegionalMS_{n}.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 9, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-9/RegionalMS_{r}.pdf"))

# MS Set 10 — {n}A_MS_Reg_2016.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 10, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-10/{r}A_MS_Reg_2016.pdf"))

# MS Set 11 — MS_{n}.pdf (17 rounds) — note lowercase 'set' in URL
for r in range(1, 18):
    PDF_LIST.append(("MS", 11, r,
        f"{BASE}/MS-Sample-Questions/Sample-set-11/MS_{r}.pdf"))

# MS Set 12 — MSRound-{n}.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 12, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-12/MSRound-{r}.pdf"))

# MS Set 13 (2019) — 2019-NSB-MSR-Round-{n}A.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 13, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-13/2019-NSB-MSR-Round-{r}A.pdf"))

# MS Sample Rounds — Round Robin (rounds 2, 5)
for r in [2, 5]:
    PDF_LIST.append(("MS", "RR", r,
        f"{BASE}/MS-Sample-Questions/Sample-Rounds/rr{r}_for_web.pdf"))

# MS Sample Rounds — Double Elimination (rounds 1, 3)
for r in [1, 3]:
    PDF_LIST.append(("MS", "DE", r,
        f"{BASE}/MS-Sample-Questions/Sample-Rounds/de{r}_for_web.pdf"))

# MS Set 14 (2020) — 2020-MS-Rd{n}.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("MS", 14, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-14/2020-MS-Rd{r}.pdf"))

# MS Set 15 (2021) — Set-{n}-MS-2021.pdf (10 rounds)
for r in range(1, 11):
    PDF_LIST.append(("MS", 15, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-15/Set-{r}-MS-2021.pdf"))

# MS Set 16 (2022) — 2022-MS-{n}.pdf (9 rounds)
for r in range(1, 10):
    PDF_LIST.append(("MS", 16, r,
        f"{BASE}/MS-Sample-Questions/Sample-Set-16/2022-MS-{r}.pdf"))

# ── HS Sets ────────────────────────────────────────────────────────────────────

# HS Sets 1–12 — round{n}.pdf
for r in range(1, 18):
    PDF_LIST.append(("HS", 1, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-1/round{r}.pdf"))

for r in range(1, 16):
    PDF_LIST.append(("HS", 2, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-2/round{r}.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 3, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-3/Round-{r}C.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 4, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-4/round{r}.pdf"))

for r in range(1, 16):
    PDF_LIST.append(("HS", 5, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-5/round{r}.pdf"))

for r in range(1, 16):
    PDF_LIST.append(("HS", 6, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-6/Sample6_ROUND{r}.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 7, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-7/ROUND-{r}.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 8, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-8/Round-{r}-A.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 9, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-9/RegionalHS_{r}.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 10, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-10/{r}A_HS_Reg_2016.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 11, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-11/HS_{r}.pdf"))

for r in range(1, 18):
    PDF_LIST.append(("HS", 12, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-12/2018-HSRound-{r}.pdf"))

# HS Set 13 (2019) — rounds 1-6, 15-17
for r in [1, 2, 3, 4, 5, 6, 15, 16, 17]:
    PDF_LIST.append(("HS", 13, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-13/2019-NSB-HSR-Round-{r}A.pdf"))

# HS Set 14 — rounds 7-14
for r in range(7, 15):
    PDF_LIST.append(("HS", 14, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-14/2019-NSB-HSR-Round-{r}A.pdf"))

# HS Set 15 (2020) — 2020-HS-Rd{n}.pdf (17 rounds)
for r in range(1, 18):
    PDF_LIST.append(("HS", 15, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-15/2020-HS-Rd{r}.pdf"))

# HS Set 16 (2021) — Set-{n}-HS-2021.pdf (10 rounds)
for r in range(1, 11):
    PDF_LIST.append(("HS", 16, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-16/Set-{r}-HS-2021.pdf"))

# HS Set 17 (2022) — 2022-HS-{n}.pdf (15 rounds)
for r in range(1, 16):
    PDF_LIST.append(("HS", 17, r,
        f"{BASE}/HS-Sample-Questions/Sample-Set-17/2022-HS-{r}.pdf"))

SUBJECTS = ["Life Science","Physical Science","Earth and Space","Energy",
            "Mathematics","Math","General Science","Biology","Chemistry","Physics"]

JUNK = re.compile(
    r'^(MIDDLE SCHOOL|HIGH SCHOOL)'
    r'|[~]{3,}'
    r'|^\d+$'
    r'|^\d+\)\s*$'
    r'|Regional Science Bowl'
    r'|National Science Bowl'
    r'|Round\s+\d+\s*(Page\s+\d+)?'
    r'|Page\s+\d+\s+of\s+\d+'
    r'|^\s*Page\s+\d+'
    r'|Science\s+Bowl\s+Sample'
    r'|^\s*.{1,3}\s*$',
    re.IGNORECASE
)

MARKER = re.compile(r'^(TOSS-UP|BONUS)\s*$', re.IGNORECASE | re.MULTILINE)

def extract_text(pdf_path):
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                pages.append(t)
    return "\n".join(pages)

def clean_text(raw):
    lines = []
    for line in raw.split("\n"):
        line = line.strip()
        if line and not JUNK.search(line):
            lines.append(line)
    return "\n".join(lines)

def split_blocks(text):
    blocks = []
    matches = list(MARKER.finditer(text))
    for i, m in enumerate(matches):
        label = "TOSSUP" if "TOSS" in m.group(1).upper() else "BONUS"
        start = m.end()
        end   = matches[i+1].start() if i+1 < len(matches) else len(text)
        blocks.append((label, text[start:end].strip()))
    return blocks

def parse_block(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if len(lines) < 2:
        return None

    # Find ANSWER: from the bottom
    answer_idx = None
    for j in range(len(lines)-1, -1, -1):
        if re.match(r'^ANSWER\s*:', lines[j], re.IGNORECASE):
            answer_idx = j
            break
    if answer_idx is None:
        return None

    # ── Header line: "1) Subject – Type [question start...]" ──────────────
    header = lines[0]
    pdf_q_num = None
    nm = re.match(r'^(\d+)\)\s*', header)
    if nm:
        pdf_q_num = int(nm.group(1))
        header = header[nm.end():].strip()

    subject = "General Science"
    for s in SUBJECTS:
        if s.lower() in header.lower():
            subject = s
            break

    q_type = "Multiple Choice" if re.search(r'multiple[\s\-]?choice', header, re.IGNORECASE) else "Short Answer"

    # Strip "Subject – Type" prefix, keep anything after as start of question
    # e.g. "Life Science – Short Answer What is the term..." → "What is the term..."
    leftover = re.sub(
        r'^.*?(short\s+answer|multiple[\s\-]?choice)\s*',
        '', header, flags=re.IGNORECASE
    ).strip()

    # ── Body: leftover from header + remaining lines up to ANSWER ─────────
    body_lines = ([leftover] if leftover else []) + lines[1:answer_idx]

    # Join continuation lines — a line is a new item only if it starts with
    # W) X) Y) Z) (MC choice) — everything else continues the previous line
    joined = []
    for line in body_lines:
        if re.match(r'^[WXYZ]\)', line):
            joined.append(line)   # new choice line
        elif joined:
            joined[-1] = joined[-1] + " " + line  # continuation
        else:
            joined.append(line)   # first line of question

    choices = {}
    question_parts = []
    for line in joined:
        # Match W) X) Y) Z) with optional space before content
        mc = re.match(r'^([WXYZ])\)\s*(.+)$', line)
        if mc:
            choice_text = mc.group(2).strip()
            # Strip any trailing answer leak like "ANSWER: X"
            choice_text = re.sub(r'\s*ANSWER\s*:.*$', '', choice_text, flags=re.IGNORECASE).strip()
            choices[mc.group(1)] = choice_text
        else:
            if line:
                question_parts.append(line)

    question = " ".join(question_parts).strip()
    if len(question) < 10:
        return None

    # ── Answer ────────────────────────────────────────────────────────────
    answer_raw = re.sub(r'^ANSWER\s*:\s*', '', lines[answer_idx], flags=re.IGNORECASE).strip()
    for line in lines[answer_idx+1:]:
        answer_raw += " " + line.strip()
    answer_raw = answer_raw.strip()

    accepted = []
    am = re.search(r'\(ACCEPT[S]?:?\s*([^)]+)\)', answer_raw, re.IGNORECASE)
    if am:
        for part in re.split(r'\s+OR\s+|[,;]', am.group(1)):
            p = part.strip()
            if p:
                accepted.append(p)
        answer_raw = re.sub(r'\s*\(ACCEPT[S]?:?[^)]+\)', '', answer_raw).strip()
    answer_raw = re.sub(r'\s*\(DO NOT ACCEPT[^)]+\)', '', answer_raw).strip()
    answer_raw = re.sub(r'\s*\[[^\]]+\]', '', answer_raw).strip()

    q = {"subject": subject, "type": q_type, "question": question, "answer": answer_raw.upper()}
    if pdf_q_num is not None:
        q["pdfQuestionNum"] = pdf_q_num
    if accepted:
        q["acceptedAnswers"] = list(dict.fromkeys([answer_raw.upper()] + [a.upper() for a in accepted]))
    if choices:
        q["choices"] = choices
        lm = re.match(r'^([WXYZ])\b', answer_raw)
        if lm:
            q["answer"] = lm.group(1)
            q["answerText"] = answer_raw[1:].strip().lstrip(')').strip().upper()
        else:
            for letter, ct in choices.items():
                if ct.upper() in answer_raw.upper() or answer_raw.upper() in ct.upper():
                    q["answer"] = letter
                    q["answerText"] = ct.upper()
                    break
    return q

def process_pdf(pdf_path, level, set_num, round_label):
    raw     = extract_text(pdf_path)
    cleaned = clean_text(raw)
    blocks  = split_blocks(cleaned)
    questions, q_num, i = [], 0, 0
    while i < len(blocks):
        label, block_text = blocks[i]
        if label == "TOSSUP":
            tossup = parse_block(block_text)
            bonus  = None
            if i+1 < len(blocks) and blocks[i+1][0] == "BONUS":
                bonus = parse_block(blocks[i+1][1])
                i += 1
            if tossup:
                q_num += 1
                dn = tossup.pop("pdfQuestionNum", q_num)
                questions.append({
                    "id": q_num,
                    "meta": {"level": level, "set": set_num, "round": round_label, "questionNum": dn},
                    "tossup": tossup,
                    "bonus":  bonus if bonus else {}
                })
        i += 1
    return questions

def download_pdf(url, path):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        if r.status_code == 200 and r.content[:4] == b"%PDF":
            open(path, "wb").write(r.content)
            return True
        print(f"  HTTP {r.status_code}")
    except Exception as e:
        print(f"  Error: {e}")
    return False

JS_HELPERS = """
function getAllQuestions(level) {
  // level: "MS", "HS", or undefined for all
  const pool = level ? questions.filter(q => q.meta.level === level) : questions;
  return [...pool].sort(() => Math.random() - 0.5);
}
function getQuestionsBySubject(subject, level) {
  let pool = level ? questions.filter(q => q.meta.level === level) : questions;
  return pool.filter(q => q.tossup.subject === subject);
}
function checkAnswer(userAnswer, question) {
  const normalize = str => str
    .trim().toUpperCase()
    .replace(/[^A-Z0-9\\s]/g, '')
    .replace(/\\b(THE|A|AN)\\b/g, '')
    .replace(/\\s+/g, ' ').trim();

  const ua = normalize(userAnswer);

  if (question.type === "Multiple Choice") {
    const rawUa = userAnswer.trim().toUpperCase();
    return rawUa === question.answer || rawUa === (question.answerText || '');
  }

  const accepted = question.acceptedAnswers
    ? question.acceptedAnswers.map(a => normalize(a))
    : [normalize(question.answer)];

  if (accepted.includes(ua)) return true;

  const singular = ua.endsWith('S') ? ua.slice(0, -1) : ua;
  const plural   = ua.endsWith('S') ? ua : ua + 'S';
  if (accepted.includes(singular) || accepted.includes(plural)) return true;

  if (accepted.some(a => a.includes(ua) || ua.includes(a))) return true;

  return false;
}
const SUBJECTS = ["Life Science","Physical Science","Earth and Space",
                  "Energy","Math","Mathematics","General Science",
                  "Biology","Chemistry","Physics"];
"""

def main():
    os.makedirs("pdf_cache", exist_ok=True)
    all_questions, global_id = [], 1
    skipped = 0
    print(f"Processing up to {len(PDF_LIST)} PDFs (skipping 404s)...\n")
    for (level, set_num, round_label, url) in PDF_LIST:
        path = f"pdf_cache/{level.lower()}_set{set_num}_round{round_label}.pdf"
        tag  = f"{level} Set {set_num} Round {round_label}"
        if not os.path.exists(path):
            print(f"  Downloading {tag}...", end=" ", flush=True)
            if not download_pdf(url, path):
                skipped += 1
                continue
            print("OK")
            time.sleep(0.3)
        else:
            print(f"  {tag} (cached)", end=" ")
        try:
            parsed = process_pdf(path, level, set_num, round_label)
            for q in parsed:
                q["id"] = global_id
                global_id += 1
            all_questions.extend(parsed)
            print(f"-> {len(parsed)} questions")
        except Exception as e:
            print(f"-> ERROR: {e}")
    print(f"\nTotal: {len(all_questions)} questions ({skipped} PDFs skipped/not found)")
    # Split into MS and HS counts
    ms_count = sum(1 for q in all_questions if q["meta"]["level"] == "MS")
    hs_count = sum(1 for q in all_questions if q["meta"]["level"] == "HS")
    print(f"  MS: {ms_count}  |  HS: {hs_count}")
    with open("questions.js", "w", encoding="utf-8") as f:
        f.write("// questions.js\n")
        f.write(f"// {len(all_questions)} questions from NSB official PDFs ({ms_count} MS, {hs_count} HS)\n\n")
        f.write("const questions = ")
        f.write(json.dumps(all_questions, indent=2, ensure_ascii=False))
        f.write(";\n")
        f.write(JS_HELPERS)
    print("Done! questions.js is ready.")
    with open("questions.js", "w", encoding="utf-8") as f:
        f.write("// questions.js\n")
        f.write(f"// {len(all_questions)} questions from NSB official PDFs\n\n")
        f.write("const questions = ")
        f.write(json.dumps(all_questions, indent=2, ensure_ascii=False))
        f.write(";\n")
        f.write(JS_HELPERS)
    print("Done! questions.js is ready.")

if __name__ == "__main__":
    main()
