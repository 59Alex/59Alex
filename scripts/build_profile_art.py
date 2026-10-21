"""Reproducible, self-contained bilingual SVG profile artwork."""
from pathlib import Path
from html import escape
from math import cos, sin, pi

ASSETS = Path(__file__).resolve().parents[1] / 'assets'


def motion_css():
    rules = ['.block,.rig,.sling{opacity:0}']
    for i, (start, dy, anchor) in enumerate([(0, -260, 340), (18, -180, 260), (36, -98, 178), (54, -24, 80)]):
        small = (anchor + dy - 42) / (anchor - 42)
        rules.append(f'''
.block-{i}{{animation:block{i} 28s ease-in-out infinite}}
.rig-{i}{{animation:rig{i} 28s ease-in-out infinite}}
.wire-{i}{{transform-origin:350px 42px;animation:wire{i} 28s ease-in-out infinite}}
.sling-{i}{{animation:sling{i} 28s ease-in-out infinite}}
@keyframes block{i}{{0%,{start}%{{opacity:0;transform:translate(30px,{dy}px)}}{start+1}%{{opacity:1;transform:translate(30px,{dy}px)}}{start+5}%{{opacity:1;transform:translate(0,{dy}px)}}{start+13}%,92%{{opacity:1;transform:translate(0,0)}}97%,100%{{opacity:0;transform:translate(0,0)}}}}
@keyframes rig{i}{{0%,{start}%{{opacity:0;transform:translateX(30px)}}{start+1}%{{opacity:1;transform:translateX(30px)}}{start+5}%,{start+13}%{{opacity:1;transform:translateX(0)}}{start+14}%,100%{{opacity:0;transform:translateX(0)}}}}
@keyframes wire{i}{{0%,{start+5}%{{transform:scaleY({small:.4f})}}{start+13}%,100%{{transform:scaleY(1)}}}}
@keyframes sling{i}{{0%,{start}%{{opacity:0}}{start+1}%,{start+12}%{{opacity:1}}{start+14}%,100%{{opacity:0}}}}
''')
    rules.append('''
.gear{animation:turn var(--period) linear infinite}.reverse{animation-direction:reverse}
.balance{animation:balance 1.4s ease-in-out infinite}
@keyframes turn{to{transform:rotate(360deg)}}
@keyframes balance{0%,100%{transform:rotate(-26deg)}50%{transform:rotate(26deg)}}
@media(prefers-reduced-motion:reduce){.block{animation:none;opacity:1;transform:none}.rig,.sling{animation:none;opacity:0}.wire,.gear,.balance{animation:none}}
''')
    return '\n'.join(rules)


def scene(c, lang):
    ink, muted, line, fill, accent = c
    result = f'''<g fill="none" stroke="{line}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M16 426h552 M40 420V35h22v385 M22 420h58 M22 35h530v14H22z M40 35L54 8l9 27 M54 8l-32 27 M54 8l476 27"/>
<rect x="10" y="52" width="25" height="20" rx="2" fill="{fill}"/>
'''
    for y in range(49, 410, 40):
        result += f'<path d="M40 {y}l22 {min(40, 420-y)}M40 {min(y+40, 420)}l22-{min(40, 420-y)}"/>'
    for x in range(80, 520, 40):
        result += f'<path d="M{x} 35l20 14 20-14"/>'
    result += '</g>'
    for i, anchor in enumerate([340, 260, 178, 80]):
        result += f'<g class="rig rig-{i}" fill="none" stroke="{accent}" stroke-width="1.4"><rect x="343" y="32" width="14" height="18" rx="2" fill="{fill}"/><path class="wire wire-{i}" d="M350 42V{anchor}"/></g>'
    labels = ['ИНФРАСТРУКТУРА', 'ДАННЫЕ И КОММУНИКАЦИИ', 'СЕРВЕР'] if lang == 'ru' else ['INFRASTRUCTURE', 'DATA & COMMUNICATION', 'SERVER']
    floors = [
        (0, 140, 358, 420, 60, labels[0], ['Docker · Kubernetes · CI/CD']),
        (1, 150, 278, 400, 72, labels[1], ['Kafka · Redis · PostgreSQL', 'WebRTC · SSE']),
        (2, 150, 196, 400, 74, labels[2], ['Java · Spring · Debezium', 'Project Reactor']),
    ]
    for i, x, y, width, height, label, tech in floors:
        result += f'''<g class="block block-{i}"><g class="sling sling-{i}" fill="none" stroke="{accent}" stroke-width="1.2"><path d="M{x+70} {y}L350 {y-18}L{x+width-70} {y}"/></g><rect x="{x}" y="{y}" width="{width}" height="{height}" rx="4" fill="{fill}" stroke="{line}"/><path d="M{x} {y+height-5}h{width}" stroke="{accent}" opacity=".3"/>
<text x="350" y="{y+18}" text-anchor="middle" fill="{muted}" font-size="12" letter-spacing="1.4">{escape(label)}</text>'''
        for j, text in enumerate(tech):
            result += f'<text x="350" y="{y+42+j*21}" text-anchor="middle" fill="{ink}" font-size="19">{escape(text)}</text>'
        result += '</g>'
    result += f'''<g class="block block-3"><g class="sling sling-3" fill="none" stroke="{accent}" stroke-width="1.2"><path d="M300 123L350 80L400 123"/></g>
<path d="M140 188L350 96L560 188Z" fill="{fill}" stroke="{line}" stroke-linejoin="round"/>
<path d="M150 188h400" stroke="{accent}" stroke-width="2"/>
<text x="350" y="150" text-anchor="middle" fill="{ink}" font-size="19">TS · React · Vite</text>
<text x="350" y="175" text-anchor="middle" fill="{ink}" font-size="18">Next.js · Node.js</text>
</g>'''
    return result


def gear(x, y, radius, teeth, seconds, reverse, c):
    ink, muted, line, fill, accent = c
    points = []
    for tooth in range(teeth):
        for phase, r in ((0, radius-3), (.18, radius+3), (.55, radius+3), (.73, radius-3)):
            angle = (tooth+phase)*2*pi/teeth
            points.append(f'{r*cos(angle):.2f},{r*sin(angle):.2f}')
    spokes = ''.join(f'<path d="M{12*cos(a):.2f} {12*sin(a):.2f}L{(radius-12)*cos(a):.2f} {(radius-12)*sin(a):.2f}"/>' for a in [i*pi/3 for i in range(6)])
    return f'''<g transform="translate({x} {y})"><g class="gear {'reverse' if reverse else ''}" style="--period:{seconds}s" stroke="{accent}" fill="none" stroke-width="1.4">
<polygon points="{' '.join(points)}" fill="{fill}"/><circle r="{radius-10}"/>{spokes}<circle r="10" fill="{fill}"/></g><circle r="4" fill="{accent}"/><circle r="1.5" fill="{ink}"/></g>'''


def clockwork(c):
    ink, muted, line, fill, accent = c
    result = f'''<g fill="none" stroke="{line}" stroke-width="1.2">
<path d="M76 28Q88 4 122 4H353Q389 4 405 37L430 98Q439 128 411 144H122Q79 144 72 110Z"/>
<path d="M84 29Q99 13 126 13H350M416 115Q411 134 387 135H133" opacity=".45"/>
</g>'''
    # Equal tooth pitch and inverse tooth-count speeds give a consistent gear train.
    for args in [(151,74,58,29,29,False), (247,74,38,19,19,True), (299,118,30,15,15,False)]:
        result += gear(*args, c)
    result += f'''<g transform="translate(365 65)" fill="none" stroke="{accent}">
<circle r="43" stroke="{line}"/><g class="balance"><circle r="36" stroke-width="2"/><circle r="30" stroke-width=".7"/>
<path d="M-36 0h72M0-36v72" stroke-width="2"/><path d="M0 0C-5-10 15-15 18 0S-7 25-19 9S-12-27 12-25S43 10 22 25" stroke-width="1"/></g><circle r="4" fill="{accent}"/>
</g><path d="M120 74H268L299 118" fill="none" stroke="{line}" stroke-width="9" stroke-linecap="round"/>
<path d="M120 74H268L299 118" fill="none" stroke="{muted}" stroke-width=".6"/>
'''
    for x,y in [(106,29),(395,116),(151,74),(247,74),(299,118)]:
        result += f'<circle cx="{x}" cy="{y}" r="4" fill="{fill}" stroke="{accent}"/><path d="M{x-2} {y+2}l4-4" stroke="{muted}"/>'
    return result


def header(dark, mobile, static=False, lang='ru'):
    bg, ink, muted, line, panel, accent = (
        ('#0D0918', '#F3EDFF', '#ADA0C6', '#594074', '#21132F', '#BB8DF2') if dark else
        ('#F4F0FA', '#29143E', '#716180', '#B7A0CB', '#E8DEF1', '#8050AC')
    )
    colors = ink, muted, line, panel, accent
    width, height = (600, 1030) if mobile else (1280, 610)
    position = 'translate(0 575) scale(1.02)' if mobile else 'translate(650 132) scale(1.04)'
    size, top = (44, 153) if mobile else (48, 157)
    lines = ['Надежные', 'Распределенные', 'Высоконагруженные', 'Системы'] if lang == 'ru' else ['Reliable', 'Distributed', 'High-load', 'Systems']
    name = 'Александр Кашеваров' if lang == 'ru' else 'Aleksandr Kashevarov'
    identity = name + ' · Java & TS Full Stack Engineer'
    text = ''.join(f'<tspan x="32" y="{top+i*61}">{line_text}</tspan>' for i,line_text in enumerate(lines))
    identity_svg = (f'<tspan x="32" y="38">{name}</tspan><tspan x="32" y="69">Java &amp; TS Full Stack Engineer</tspan>' if mobile else escape(identity))
    description = ('Кран собирает дом из технологий: инфраструктура, данные и коммуникации, сервер, фронтенд. Внизу работает часовой механизм.' if lang == 'ru' else 'A crane assembles a house of technologies: infrastructure, data and communication, server, frontend. A clockwork mechanism runs below.')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc" lang="{lang}">
<title id="title">{escape(identity)}</title><desc id="desc">{' '.join(lines)}. {description}</desc>
<defs><clipPath id="frame"><rect width="{width}" height="{height}" rx="12"/></clipPath></defs>
<style>{'.block{opacity:1}.rig,.sling{display:none}' if static else motion_css()}</style>
<g clip-path="url(#frame)" font-family="Arial, Helvetica, sans-serif">
<rect width="{width}" height="{height}" fill="{bg}"/>
<path d="M32 {91 if mobile else 68}H{width-32}" stroke="{line}" opacity=".35"/>
<text x="32" y="43" fill="{ink}" font-size="{23 if mobile else 24}">{identity_svg}</text>
<text fill="{ink}" font-size="{size}" font-weight="600" letter-spacing="-1.4">{text}</text>
<g transform="translate(12 395) scale(1.12)">{clockwork(colors)}</g>
<g transform="{position}">{scene(colors, lang)}</g>
</g></svg>\n'''


if __name__ == '__main__':
    for lang in ('ru', 'en'):
        for dark in (False, True):
            theme = 'dark' if dark else 'light'
            for mobile in (False, True):
                for static in (False, True):
                    name = f'header-{"en-" if lang == "en" else ""}{"static-" if static else ""}{"mobile-" if mobile else ""}{theme}.svg'
                    (ASSETS / name).write_text(header(dark, mobile, static, lang))
