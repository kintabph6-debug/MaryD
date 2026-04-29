from pathlib import Path
p = Path(r"c:\Users\This\3D Objects\MaryPortfolio\index.html")
s = p.read_text(encoding="utf-8")

# Insert Sublimation category detection after the Graphics detection line
old_line = "else if (/\/Graphics\//i.test(normalized)) category = 'Graphics';"
if old_line in s:
    new_line = old_line + "\n        else if (/\/Jersey_Sublimation-projects(\/|$)/i.test(normalized)) category = 'Sublimation';"
    s = s.replace(old_line, new_line)

# Insert Sublimation section before the contact section
contact_marker = "\n    <section id=\"contact\" class=\"contact\">"
if contact_marker in s:
    sub_section = "\n\n    <section class=\"sublimation\" id=\"sublimation\">\n      <div class=\"container\">\n        <h2>Jersey Sublimation</h2>\n        <p>Explore jersey sublimation mockups and project files.</p>\n        <p><a href=\"Mary_D%20Reels%20%26%20Graphics/Jersey_Sublimation-projects/\">Open Jersey Sublimation Projects</a></p>\n      </div>\n    </section>\n\n    <section id=\"contact\" class=\"contact\">"
    s = s.replace(contact_marker, sub_section)

p.write_text(s, encoding="utf-8")
print('patched')
