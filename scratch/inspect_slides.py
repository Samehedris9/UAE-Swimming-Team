import re

with open(r"C:\Users\Sameh Edris\.gemini\antigravity-ide\scratch\UAE-Swimming-Team\index.html", "r", encoding="utf-8") as f:
    content = f.read()

sections = re.findall(r'(<section[^>]*id=["\']([^"\']+)["\'][^>]*>.*?)(?=</section>)', content, re.DOTALL)

print(f"Total sections found: {len(sections)}")
for idx, (sec_html, sec_id) in enumerate(sections, 1):
    title_match = re.search(r'<(?:h1|h2|h3|div)[^>]*class=["\'][^"\']*(?:title|heading|name|section-header)[^"\']*["\'][^>]*>(.*?)</', sec_html, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "No title found"
    # clean tags inside title
    title_clean = re.sub(r'<[^>]+>', '', title).strip().replace('\n', ' ')
    print(f"Slide {idx:02d} | ID: {sec_id:<25} | Title: {title_clean[:60]}")
