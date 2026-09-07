import re

with open(r"C:\Users\Sameh Edris\.gemini\antigravity-ide\scratch\UAE-Swimming-Team\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for sidebar HTML or JS slide generation
print("--- Navigation / Drawer HTML search ---")
nav_matches = re.findall(r'<div[^>]*class=["\'][^"\']*(?:nav|drawer|sidebar|dots|slide-count)[^"\']*["\'][^>]*>.*?</div>', content, re.DOTALL)
for m in nav_matches[:5]:
    print(m[:200])
    print("="*40)

# Search for JavaScript section/slide handling
print("--- JS Section handling search ---")
js_matches = re.findall(r'const sections =.*?;|function update.*?\n\}', content, re.DOTALL)
for m in js_matches[:5]:
    print(m[:300])
    print("="*40)
