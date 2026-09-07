with open(r"C:\Users\Sameh Edris\.gemini\antigravity-ide\scratch\UAE-Swimming-Team\index.html", "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        if "background-clip" in line:
            print(f"Line {idx+1}: {line.strip()}")
