"""Build self-contained profile artwork; no remote fonts or image services."""
from pathlib import Path
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / 'assets'


def header(dark, mobile):
    bg, ink, muted, line, panel, accent = (
        ('#0B141A', '#F2F6F4', '#A8BDB7', '#2C4340', '#122421', '#67E8BD')
        if dark else ('#F0F4EF', '#142B27', '#4B6660', '#C4D5CC', '#E4ECE4', '#087C5B')
    )
    w, h = (480, 356) if mobile else (1200, 420)
    left, top, java_y, full_y = (28, 40, 143, 211) if mobile else (42, 46, 188, 280)
    java_size, full_size = (88, 58) if mobile else (130, 90)
    art = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">59Alex · Java Full Stack</title>
<desc id="desc">Java and Spring services, React and TypeScript interfaces, Kafka event streams. From interaction to transaction.</desc>
<defs>
 <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{line}"/></pattern>
 <linearGradient id="wash" x1="0" x2="1" y1="1" y2="0"><stop stop-color="{bg}"/><stop offset="1" stop-color="{panel}"/></linearGradient>
 <clipPath id="frame"><rect width="{w}" height="{h}" rx="20"/></clipPath>
</defs>
<g clip-path="url(#frame)">
 <rect width="{w}" height="{h}" fill="url(#wash)"/>
 <rect x="{w * .53}" width="{w * .47}" height="{h}" fill="url(#dots)" opacity=".55"/>
 <path d="M{left} {top-8}h18" stroke="{accent}" stroke-width="4"/>
 <text x="{left+30}" y="{top-3}" fill="{muted}" font-family="monospace" font-size="14" letter-spacing="2">59ALEX / ENGINEERING</text>
 <text x="{left-3}" y="{java_y}" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-weight="800" font-size="{java_size}" letter-spacing="-5">JAVA<tspan fill="{accent}">.</tspan></text>
 <text x="{left-2}" y="{full_y}" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-weight="800" font-size="{full_size}" letter-spacing="-3">FULL STACK</text>
'''
    if mobile:
        art += f'''<path d="M28 246h424" stroke="{line}"/>
<g font-family="monospace" font-size="13" fill="{muted}">
 <text x="28" y="276">JAVA + SPRING</text><text x="256" y="276">REACT + TYPESCRIPT</text>
</g>
<path d="M28 312h24m-5-5 5 5-5 5" fill="none" stroke="{accent}" stroke-width="2"/>
<text x="66" y="317" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="18">From interaction to transaction.</text>
'''
    else:
        art += f'''<text x="1158" y="43" text-anchor="end" fill="{muted}" font-family="monospace" font-size="12" letter-spacing="2">SOFTWARE / SYSTEMS / OPEN SOURCE</text>
<path d="M720 122v170h40" fill="none" stroke="{accent}" stroke-width="2"/>
<circle cx="720" cy="122" r="4" fill="{accent}"/>
'''
        for x, y, num, label, stack in [
            (794, 79, '01', 'INTERFACE', 'React / TypeScript'),
            (756, 162, '02', 'SERVICES', 'Java / Spring'),
            (794, 245, '03', 'EVENT STREAMS', 'Kafka / Streaming'),
        ]:
            art += f'''<rect x="{x+4}" y="{y+5}" width="328" height="72" rx="12" fill="{bg}" opacity=".4"/>
<rect x="{x}" y="{y}" width="328" height="72" rx="12" fill="{panel}" stroke="{line}"/>
<text x="{x+18}" y="{y+27}" fill="{accent}" font-family="monospace" font-size="13">{num}</text>
<text x="{x+56}" y="{y+25}" fill="{muted}" font-family="monospace" font-size="11" letter-spacing="1.6">{label}</text>
<text x="{x+56}" y="{y+51}" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="600">{stack}</text>
<path d="M{x+300} {y+30}l6 6-6 6" fill="none" stroke="{accent}" stroke-width="2"/>
'''
        art += f'''<path d="M42 341h1116" stroke="{line}"/>
<path d="M42 378h26m-6-6 6 6-6 6" fill="none" stroke="{accent}" stroke-width="2"/>
<text x="84" y="384" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="23">From interaction to transaction.</text>
<text x="1158" y="382" text-anchor="end" fill="{muted}" font-family="monospace" font-size="13" letter-spacing="1">STREAMING / REAL-TIME SYSTEMS</text>
'''
    return art + '</g></svg>\n'


for dark in (False, True):
    theme = 'dark' if dark else 'light'
    for mobile in (False, True):
        (ASSETS / f'header-{"mobile-" if mobile else ""}{theme}.svg').write_text(header(dark, mobile))
    for lang, caption in [('en', 'English'), ('ru', 'Русский')]:
        ink, bg, stroke, accent = ('#F2F6F4', '#122421', '#3D665A', '#67E8BD') if dark else ('#142B27', '#EAF3EC', '#98B9AA', '#087C5B')
        (ASSETS / f'lang-{lang}-{theme}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="108" height="44" viewBox="0 0 108 44" role="img" aria-label="{escape(caption)}">
<rect x=".5" y=".5" width="107" height="43" rx="10" fill="{bg}" stroke="{stroke}"/>
<circle cx="20" cy="22" r="3" fill="{accent}"/>
<text x="59" y="28" text-anchor="middle" fill="{ink}" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="700" letter-spacing="1.5">{lang.upper()}</text>
<path d="m87 19 3 3-3 3" stroke="{accent}" stroke-width="1.5" fill="none"/>
</svg>\n''')
