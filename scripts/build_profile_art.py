"""Reproducible, self-contained bilingual SVG profile artwork."""
from pathlib import Path
from html import escape
from math import cos, sin, pi

ASSETS = Path(__file__).resolve().parents[1] / 'assets'

CRANE_END = 560
PICKUP_X = CRANE_END - 8  # Keep the trolley fully inside the end of the boom.
PICKUP_OFFSET = PICKUP_X - 350


def motion_css():
    rules = ['.block,.rig,.sling{opacity:0}']
    for i, (start, dy, anchor) in enumerate([(0, -260, 340), (18, -180, 260), (36, -98, 178), (54, -24, 80)]):
        small = (anchor + dy - 42) / (anchor - 42)
        rules.append(f'''
.block-{i}{{animation:block{i} 28s ease-in-out infinite}}
.rig-{i}{{animation:rig{i} 28s ease-in-out infinite}}
.wire-{i}{{transform-origin:350px 42px;animation:wire{i} 28s ease-in-out infinite}}
.sling-{i}{{animation:sling{i} 28s ease-in-out infinite}}
@keyframes block{i}{{0%,{start}%{{opacity:0;transform:translate({PICKUP_OFFSET}px,{dy}px)}}{start+1}%{{opacity:1;transform:translate({PICKUP_OFFSET}px,{dy}px)}}{start+5}%{{opacity:1;transform:translate(0,{dy}px)}}{start+13}%,92%{{opacity:1;transform:translate(0,0)}}97%,100%{{opacity:0;transform:translate(0,0)}}}}
@keyframes rig{i}{{0%,{start}%{{opacity:0;transform:translateX({PICKUP_OFFSET}px)}}{start+1}%{{opacity:1;transform:translateX({PICKUP_OFFSET}px)}}{start+5}%,{start+13}%{{opacity:1;transform:translateX(0)}}{start+14}%,100%{{opacity:0;transform:translateX(0)}}}}
@keyframes wire{i}{{0%,{start+5}%{{transform:scaleY({small:.4f})}}{start+13}%,100%{{transform:scaleY(1)}}}}
@keyframes sling{i}{{0%,{start}%{{opacity:0}}{start+1}%,{start+12}%{{opacity:1}}{start+14}%,100%{{opacity:0}}}}
''')
    rules.append('''
.gear{animation:turn var(--period) linear infinite}.reverse{animation-direction:reverse}
.balance{animation:balance 1.4s ease-in-out infinite}
.stream{stroke-dasharray:3 21;animation:flow 5s linear infinite}.stream-return{animation-direction:reverse;animation-duration:7s}
@keyframes flow{to{stroke-dashoffset:-144}}
@keyframes turn{to{transform:rotate(360deg)}}
@keyframes balance{0%,100%{transform:rotate(-26deg)}50%{transform:rotate(26deg)}}
@media(prefers-reduced-motion:reduce){.block{animation:none;opacity:1;transform:none}.rig,.sling{animation:none;opacity:0}.wire,.gear,.balance,.stream{animation:none}}
''')
    return '\n'.join(rules)


def scene(c, lang):
    ink, muted, line, fill, accent = c
    result = f'''<g fill="none" stroke="{line}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
<path d="M16 426h552 M40 420V35h22v385 M22 420h58 M22 35H{CRANE_END}v14H22z M40 35L54 8l9 27 M54 8l-32 27 M54 8L{CRANE_END} 35"/>
<rect x="10" y="52" width="25" height="20" rx="2" fill="{fill}"/>
'''
    for y in range(49, 410, 40):
        result += f'<path d="M40 {y}l22 {min(40, 420-y)}M40 {min(y+40, 420)}l22-{min(40, 420-y)}"/>'
    for x in range(80, CRANE_END-39, 40):
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


def fitted_assembly(x, content):
    """Inset complete mechanical parts; preserve their alignment and circular motion."""
    center = 105 if x < 195 else 281 if x < 365 else 456
    return f'<g transform="translate({center} 88) scale(.78) translate({-center} -88)">{content}</g>'


def clockwork(c):
    ink, muted, line, fill, accent = c
    result = f'''<g fill="none" stroke="{line}" stroke-width="1.2">
<path d="M24 34Q24 12 50 12H160Q187 12 187 42V140Q187 164 162 164H52Q24 164 24 136Z"/>
<path d="M209 35Q209 10 236 10H326Q354 10 354 36V140Q354 165 329 165H234Q209 165 209 139Z"/>
<path d="M375 34Q375 9 402 9H510Q537 9 537 36V139Q537 165 510 165H403Q375 165 375 140Z"/>
<path d="M35 35Q35 23 51 23H154M220 34Q220 21 237 21H322M386 33Q386 20 403 20H505" opacity=".5"/>
<path d="M168 43C199 43 190 61 229 61M330 66C361 66 364 65 395 65M120 151C155 182 224 183 267 152M283 152C325 182 409 182 446 152"/>
<path d="M168 48C199 48 190 66 229 66M330 71C361 71 364 70 395 70M119 156C157 188 224 188 267 157M283 157C325 188 409 188 446 157" opacity=".4"/>
</g>
<g fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round">
<path class="stream" d="M168 43C199 43 190 61 229 61M330 66C361 66 364 65 395 65"/>
<path class="stream stream-return" d="M120 151C155 182 224 183 267 152M283 152C325 182 409 182 446 152"/>
</g>'''
    # Three local gear trains; the links represent exchanged signals between assemblies.
    trains = [
        [(80,110,42,21,42,False), (132,84,16,8,16,True), (116,46,25,12,24,False), (162,35,22,11,22,True)],
        [(275,100,38,19,38,False), (229,62,22,11,22,True), (263,32,23,11,22,False), (330,67,26,13,26,True)],
        [(447,98,40,20,40,False), (395,67,20,10,20,True), (417,28,25,12,24,False), (494,52,26,13,26,True)],
    ]
    for train in trains:
        for args in train:
            result += fitted_assembly(args[0], gear(*args, c))
    # Barrels, etched scales, bridges and jewel bearings keep the watch metaphor legible.
    for x,y,r in [(80,110,42),(275,100,38),(447,98,40)]:
        result += fitted_assembly(x, f'''<g transform="translate({x} {y})" fill="none" stroke="{muted}" stroke-width=".7">
<circle r="{r-16}"/><circle r="{r-20}" stroke-dasharray="1 3"/><path d="M-14 0C-14-19 17-20 20 0S-19 27-25 4"/>
</g>''')
    for x, path in [(80, 'M48 135L80 110L116 46L148 26'), (275, 'M235 136L275 100L330 67'), (447, 'M402 137L447 98L494 52L516 30')]:
        result += fitted_assembly(x, f'<path d="{path}" fill="none" stroke="{line}" stroke-width="8" stroke-linecap="round"/><path d="{path}" fill="none" stroke="{muted}" stroke-width=".7"/>')
    for i,(x,y) in enumerate([(80,110),(275,100),(447,98)]):
        result += fitted_assembly(x, f'<circle cx="{x}" cy="{y}" r="6" fill="{fill}" stroke="{accent}"/><circle cx="{x}" cy="{y}" r="2" fill="{ink}"/>')
        result += f'<text x="{[40,220,387][i]}" y="153" fill="{muted}" font-size="9" letter-spacing="2">0{i+1}</text>'
    for x,y in [(116,46),(132,84),(162,35),(229,62),(263,32),(330,67),(395,67),(417,28),(494,52),(48,135),(235,136),(402,137)]:
        result += fitted_assembly(x, f'<circle cx="{x}" cy="{y}" r="3" fill="{fill}" stroke="{accent}"/><path d="M{x-1.5} {y+1.5}l3-3" stroke="{muted}" stroke-width=".7"/>')
    for x,y in [(162,126),(324,127),(510,126)]:
        result += fitted_assembly(x, f'''<g transform="translate({x} {y})" stroke="{accent}" fill="none"><circle r="17" stroke="{line}"/><g class="balance"><circle r="12"/><path d="M-12 0h24M0-12v24"/><circle r="7" stroke-dasharray="1 2"/></g><circle r="2" fill="{accent}"/></g>''')
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
    description = ('Кран собирает дом из технологий: инфраструктура, данные и коммуникации, сервер, фронтенд. Три связанных часовых механизма передают импульсы по основным и обратным каналам.' if lang == 'ru' else 'A crane assembles a house of technologies: infrastructure, data and communication, server, frontend. Three connected clockwork assemblies exchange pulses along forward and return paths.')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc" lang="{lang}">
<title id="title">{escape(identity)}</title><desc id="desc">{' '.join(lines)}. {description}</desc>
<defs><clipPath id="frame"><rect width="{width}" height="{height}" rx="12"/></clipPath></defs>
<style>{'.block{opacity:1}.rig,.sling{display:none}' if static else motion_css()}</style>
<g clip-path="url(#frame)" font-family="Arial, Helvetica, sans-serif">
<rect width="{width}" height="{height}" fill="{bg}"/>
<path d="M32 {91 if mobile else 68}H{width-32}" stroke="{line}" opacity=".35"/>
<text x="32" y="43" fill="{ink}" font-size="{20 if mobile else 21}">{identity_svg}</text>
<text fill="{ink}" font-size="{size}" font-weight="600" letter-spacing="-1.4">{text}</text>
<g transform="translate(16 390)">{clockwork(colors)}</g>
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

    for dark in (True, False):
        theme = 'dark' if dark else 'light'
        bg, ink, line = ('#1A1423', '#C6B7D8', '#463553') if dark else ('#F6F3FA', '#63516F', '#D3C7DF')
        for lang in ('ru', 'en'):
            (ASSETS / f'lang-{lang}-{theme}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="42" height="26" viewBox="0 0 42 26"><rect x=".5" y=".5" width="41" height="25" rx="5" fill="{bg}" stroke="{line}"/><text x="21" y="17" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="{ink}">{lang.upper()}</text></svg>\n')
