import re

with open(r"C:\Users\Sameh Edris\.gemini\antigravity-ide\scratch\UAE-Swimming-Team\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

style_start = -1
style_end = -1
for idx, line in enumerate(lines):
    if "<style>" in line:
        style_start = idx
    if "</style>" in line:
        style_end = idx

print(f"Style tag lines: {style_start + 1} to {style_end + 1}")

# Check brace balance line by line inside style tag
depth = 0
for idx in range(style_start, style_end):
    line = lines[idx]
    # strip comments
    line_clean = re.sub(r'/\*.*?\*/', '', line)
    for char_idx, char in enumerate(line_clean):
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth < 0:
                print(f"Extra closing brace at line {idx + 1}: {line.strip()}")
                depth = 0

print(f"Final brace depth: {depth}")
