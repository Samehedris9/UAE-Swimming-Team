with open(r"C:\Users\Sameh Edris\.gemini\antigravity-ide\scratch\UAE-Swimming-Team\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "<script>" in line or "const sections =" in line or "document.querySelectorAll('section')" in line or "nav-modal" in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
