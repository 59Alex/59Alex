"""Build standalone SVG marquees from the attributed local Devicon assets."""
from pathlib import Path
import copy
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
ICONS = [('java', 'Java'), ('spring', 'Spring'), ('typescript', 'TypeScript'),
         ('react', 'React'), ('apachekafka', 'Kafka'), ('postgresql', 'PostgreSQL'),
         ('redis', 'Redis'), ('docker', 'Docker'), ('kubernetes', 'Kubernetes')]

for dark in (False, True):
    ink, panel, border = ('#D5E8F0', '#142431', '#304653') if dark else ('#173B4B', '#F0F5F6', '#CCDBDF')
    symbols = []
    for name, label in ICONS:
        icon = ET.parse(ROOT / 'assets' / 'icons' / (name + '.svg')).getroot()
        # Isolate IDs before composing separate upstream SVG documents.
        mapping = {n.attrib['id']: name + '-' + n.attrib['id'] for n in icon.iter() if 'id' in n.attrib}
        for n in icon.iter():
            for key, value in list(n.attrib.items()):
                if key == 'id': n.set(key, mapping[value])
                else:
                    for old, new in mapping.items():
                        value = value.replace('url(#' + old + ')', 'url(#' + new + ')')
                        if value == '#' + old: value = '#' + new
                    n.set(key, value)
            if name == 'apachekafka' and n.get('fill'): n.set('fill', ink)
        symbol = ET.Element('{' + NS + '}symbol', {'id': 'icon-' + name, 'viewBox': icon.get('viewBox', '0 0 128 128')})
        for child in icon: symbol.append(copy.deepcopy(child))
        symbols.append(ET.tostring(symbol, encoding='unicode'))
    for mobile in (False, True):
        width, cell = (480, 120) if mobile else (960, 144)
        period = cell * len(ICONS)
        cards = []
        for repeat in range(2):
            for index, (name, label) in enumerate(ICONS):
                x = (repeat * len(ICONS) + index) * cell
                cards.append(f'<g transform="translate({x} 0)"><rect x="4" y="6" width="{cell-12}" height="84" rx="10" fill="{panel}" stroke="{border}"/><use href="#icon-{name}" x="{cell/2-25}" y="15" width="42" height="42"/><text x="{cell/2-2}" y="77" text-anchor="middle" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="600">{label}</text></g>')
        svg = f'''<svg xmlns="{NS}" width="{width}" height="96" viewBox="0 0 {width} 96" role="img" aria-labelledby="title desc">
<title id="title">Java full stack technology strip</title>
<desc id="desc">Java, Spring, TypeScript, React, Kafka, PostgreSQL, Redis, Docker and Kubernetes. Motion is disabled when reduced motion is requested.</desc>
<style>.track{{animation:travel 40s linear infinite}}@keyframes travel{{from{{transform:translateX(0)}}to{{transform:translateX(-{period}px)}}}}@media(prefers-reduced-motion:reduce){{.track{{animation:none}}}}</style>
<defs>{''.join(symbols)}</defs>
<g class="track">{''.join(cards)}</g>
</svg>'''
        ET.fromstring(svg)
        name = 'tech-strip-' + ('mobile-' if mobile else '') + ('dark' if dark else 'light') + '.svg'
        (ROOT / 'assets' / name).write_text(svg + '\n')
print('Built four theme/viewport variants with reduced-motion support.')
