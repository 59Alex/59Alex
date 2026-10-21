"""Deterministic SVG artwork for the GitHub profile. No scripts inside the SVGs."""
from pathlib import Path
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / 'assets'


def motion_css():
    rules = ['.block{opacity:0}.rig,.sling{opacity:0}']
    for i, (start, dy, anchor) in enumerate([(0, -230, 304), (18, -160, 234), (36, -93, 167), (54, -26, 84)]):
        begin = max(0, start)
        small = (anchor + dy - 42) / (anchor - 42)
        rules.append(f'''
.block-{i}{{animation:block{i} 24s ease-in-out infinite}}
.rig-{i}{{animation:rig{i} 24s ease-in-out infinite}}
.wire-{i}{{transform-origin:350px 42px;animation:wire{i} 24s ease-in-out infinite}}
.sling-{i}{{animation:sling{i} 24s ease-in-out infinite}}
@keyframes block{i}{{0%,{begin}%{{opacity:0;transform:translate(140px,{dy}px)}}{start+1}%{{opacity:1;transform:translate(140px,{dy}px)}}{start+5}%{{opacity:1;transform:translate(0,{dy}px)}}{start+13}%,92%{{opacity:1;transform:translate(0,0)}}97%,100%{{opacity:0;transform:translate(0,0)}}}}
@keyframes rig{i}{{0%,{begin}%{{opacity:0;transform:translateX(140px)}}{start+1}%{{opacity:1;transform:translateX(140px)}}{start+5}%,{start+13}%{{opacity:1;transform:translateX(0)}}{start+14}%,100%{{opacity:0;transform:translateX(0)}}}}
@keyframes wire{i}{{0%,{start+5}%{{transform:scaleY({small:.4f})}}{start+13}%,100%{{transform:scaleY(1)}}}}
@keyframes sling{i}{{0%,{begin}%{{opacity:0}}{start+1}%,{start+12}%{{opacity:1}}{start+14}%,100%{{opacity:0}}}}
''')
    rules.append('@media(prefers-reduced-motion:reduce){.block{animation:none;opacity:1;transform:none}.rig,.sling{animation:none;opacity:0}.wire{animation:none}}')
    return '\n'.join(rules)


def scene(c):
    ink, muted, line, fill, accent = c
    result = f'''<g fill="none" stroke="{line}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M16 380h544 M40 376V35h22v341 M22 376h58 M22 35h530v14H22z M40 35L54 8l9 27 M54 8l-32 27 M54 8l476 27"/>
<path d="M40 75l22-26M40 49l22 26M40 115l22-40M40 75l22 40M40 155l22-40M40 115l22 40M40 195l22-40M40 155l22 40M40 235l22-40M40 195l22 40M40 275l22-40M40 235l22 40M40 315l22-40M40 275l22 40M40 355l22-40M40 315l22 40"/>
<path d="M80 35l20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14 20-14 20 14"/>
<rect x="10" y="52" width="25" height="20" rx="2" fill="{fill}"/>
</g>'''
    for i, anchor in enumerate([304, 234, 167, 84]):
        result += f'''<g class="rig rig-{i}" fill="none" stroke="{accent}" stroke-width="1.4"><rect x="343" y="32" width="14" height="18" rx="2" fill="{fill}"/><path class="wire wire-{i}" d="M350 42V{anchor}"/></g>'''
    floors = [
        (0, 178, 320, 354, 52, 'ИНФРАСТРУКТУРА', ['Docker · Kubernetes · CI/CD']),
        (1, 190, 250, 330, 64, 'ДАННЫЕ И КОММУНИКАЦИИ', ['Kafka · Redis · PostgreSQL', 'WebRTC · SSE']),
        (2, 190, 183, 330, 61, 'СЕРВЕР', ['Java · Spring · Debezium']),
    ]
    for i, x, y, width, height, label, tech in floors:
        result += f'''<g class="block block-{i}"><g class="sling sling-{i}" fill="none" stroke="{accent}" stroke-width="1.2"><path d="M{x+70} {y}L350 {y-16}L{x+width-70} {y}"/></g><rect x="{x}" y="{y}" width="{width}" height="{height}" rx="4" fill="{fill}" stroke="{line}"/><path d="M{x} {y+height-5}h{width}" stroke="{accent}" opacity=".3"/>
<text x="350" y="{y+16}" text-anchor="middle" fill="{muted}" font-family="Arial, sans-serif" font-size="10" letter-spacing="1.6">{label}</text>'''
        for j, line_text in enumerate(tech):
            result += f'<text x="350" y="{y+37+j*18}" text-anchor="middle" fill="{ink}" font-family="Arial, sans-serif" font-size="18">{escape(line_text)}</text>'
        result += '</g>'
    result += f'''<g class="block block-3"><g class="sling sling-3" fill="none" stroke="{accent}" stroke-width="1.2"><path d="M300 123L350 84L400 123"/></g>
<path d="M178 175L350 100L532 175Z" fill="{fill}" stroke="{line}" stroke-linejoin="round"/>
<path d="M190 175h330" stroke="{accent}" stroke-width="2"/>
<text x="350" y="143" text-anchor="middle" fill="{ink}" font-family="Arial, sans-serif" font-size="18">TS · React · Vite</text>
<text x="350" y="164" text-anchor="middle" fill="{ink}" font-family="Arial, sans-serif" font-size="17">Next.js · Node.js</text>
</g>'''
    return result


def header(dark, mobile):
    bg, ink, muted, line, panel, accent = (
        ('#0D0918', '#F3EDFF', '#ADA0C6', '#594074', '#21132F', '#BB8DF2') if dark else
        ('#F4F0FA', '#29143E', '#716180', '#B7A0CB', '#E8DEF1', '#8050AC')
    )
    width, height = (600, 780) if mobile else (1280, 490)
    position = 'translate(4 376)' if mobile else 'translate(656 73)'
    size = 43 if mobile else 49
    top = 105 if mobile else 156
    lines = ['Надёжные', 'распределённые', 'высоконагруженные', 'системы']
    text = ''.join(f'<tspan x="32" y="{top+i*(size+10)}">{line_text}</tspan>' for i,line_text in enumerate(lines))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Aleksandr Kashevarov - Java Full Stack Engineer</title>
<desc id="desc">Надёжные распределённые высоконагруженные системы. Кран собирает дом: инфраструктура; Kafka, Redis, PostgreSQL и WebRTC; Java, Spring и Debezium; TypeScript, React, Vite, Next.js и Node.js.</desc>
<defs><clipPath id="frame"><rect width="{width}" height="{height}" rx="12"/></clipPath></defs>
<style>{motion_css()}</style>
<g clip-path="url(#frame)">
<rect width="{width}" height="{height}" fill="{bg}"/>
<path d="M32 60H{width-32}" stroke="{line}" opacity=".35"/>
<text x="32" y="37" fill="{muted}" font-family="Arial, Helvetica, sans-serif" font-size="15">Aleksandr Kashevarov - Java Full Stack Engineer</text>
<text fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="600" letter-spacing="-1.4">{text}</text>
<path d="M32 {top+3*(size+10)+28}h42" stroke="{accent}" stroke-width="2"/>
<g transform="{position}">{scene((ink, muted, line, panel, accent))}</g>
</g></svg>\n'''


for dark in (False, True):
    theme = 'dark' if dark else 'light'
    for mobile in (False, True):
        (ASSETS / f'header-{"mobile-" if mobile else ""}{theme}.svg').write_text(header(dark, mobile))
    for lang in ('ru', 'en'):
        bg, ink, line = ('#1A1423','#C6B7D8','#463553') if dark else ('#F6F3FA','#63516F','#D3C7DF')
        # Adjacent halves form one quiet horizontal control; state belongs to native details.
        d = 'M8 .5H42V25.5H8Q.5 25.5 .5 18V8Q.5 .5 8 .5Z' if lang == 'ru' else 'M0 .5H34Q41.5 .5 41.5 8V18Q41.5 25.5 34 25.5H0Z'
        (ASSETS / f'lang-{lang}-{theme}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="42" height="26" viewBox="0 0 42 26" role="img" aria-label="{lang.upper()}"><path d="{d}" fill="{bg}" stroke="{line}"/><text x="21" y="17" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="500" fill="{ink}">{lang.upper()}</text></svg>\n''')
