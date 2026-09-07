import re

with open(r"C:\Users\Sameh Edris\.gemini\antigravity-ide\scratch\UAE-Swimming-Team\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

content = "".join(lines)

# Find all section start line numbers and end line numbers
matches = list(re.finditer(r'<section\b[^>]*>', content))

for i, m in enumerate(matches):
    start_pos = m.start()
    start_line = content[:start_pos].count('\n') + 1
    end_pos = content.find('</section>', start_pos)
    end_line = content[:end_pos].count('\n') + 1 if end_pos != -1 else -1
    
    sec_tag = m.group(0)
    sec_id_m = re.search(r'id=["\']([^"\']+)["\']', sec_tag)
    sec_id = sec_id_m.group(1) if sec_id_m else "no-id"
    
    # Extract first 150 chars inside section
    sec_inner = content[start_pos:end_pos][:300]
    sec_inner_clean = re.sub(r'\s+', ' ', sec_inner)
    
    print(f"Slide {i+1:02d} | Lines {start_line:4d}-{end_line:4d} | ID: {sec_id:<15} | Snippet: {sec_inner_clean[:100]}")
