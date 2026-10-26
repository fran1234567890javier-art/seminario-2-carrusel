from pathlib import Path
from html import escape

OUT = Path('/projects/sandbox/seminario-2')
W, H = 1080, 1350

COLORS = {
    'paper': '#F5ECDD', 'ink': '#2F2923', 'sepia': '#865C3A',
    'gold': '#C5A15B', 'sage': '#87917D', 'rust': '#A85F46',
    'dark': '#242526', 'cream': '#F7F0E4', 'muted': '#6E6257'
}

slides = [
    {
        'kind': 'cover', 'file': 'diapositiva-1-portada.svg',
        'title': ['De escribas a', 'gestores digitales'],
        'subtitle': 'Huellas de una profesión en Murcia',
        'body': ['Seis trayectorias que muestran cómo la gestión',
                 'de la información ha evolucionado: del',
                 'saber humanista al dato digital.']
    },
    {
        'kind': 'person', 'file': 'diapositiva-2-francisco-cascales.svg', 'number': '01',
        'period': 'SIGLO XVII', 'name': ['Francisco', 'Cascales'], 'dates': 'c. 1559–1642',
        'accent': '#B5844E', 'portrait': 'scholar', 'icon': 'book',
        'trajectory': ['Humanista, filólogo e historiador', 'murciano. Fue catedrático y enseñó', 'gramática y latín.'],
        'contribution': ['Recopiló y difundió conocimiento', 'sobre la historia, la lengua y la', 'literatura de su época.'],
        'legacy': ['Sus obras ayudaron a conservar la', 'memoria cultural de Murcia y anticipan', 'la tarea de organizar y transmitir', 'información fiable.'],
        'source': 'Fuente: Real Academia de la Historia'
    },
    {
        'kind': 'person', 'file': 'diapositiva-3-aurea-javierre.svg', 'number': '02',
        'period': '1898 — 1980', 'name': ['Áurea Lucinda', 'Javierre Mur'], 'dates': '1898–1980',
        'accent': '#9B6D64', 'portrait': 'woman', 'icon': 'archive',
        'trajectory': ['Archivera e investigadora. Ingresó en', 'el Cuerpo Facultativo de Archiveros', 'en 1921.'],
        'contribution': ['Fue la primera archivera del Archivo', 'de la Corona de Aragón y trabajó con', 'fondos históricos de gran valor.'],
        'legacy': ['Abrió camino a las mujeres en los', 'archivos y contribuyó a preservar el', 'patrimonio documental.'],
        'source': 'Fuente: Ministerio de Cultura'
    },
    {
        'kind': 'person', 'file': 'diapositiva-4-jose-antonio-gomez.svg', 'number': '03',
        'period': 'BIBLIOTECAS', 'name': ['José Antonio', 'Gómez Hernández'], 'dates': 'Universidad de Murcia',
        'accent': '#79876F', 'portrait': 'professor', 'icon': 'library',
        'trajectory': ['Catedrático de Biblioteconomía y', 'Documentación. Comenzó como', 'bibliotecario universitario en 1984.'],
        'contribution': ['Referente en alfabetización', 'informacional, gestión y marketing', 'de bibliotecas.'],
        'legacy': ['Ha formado a profesionales y defiende', 'las bibliotecas como espacios de', 'inclusión, educación y participación.'],
        'source': 'Fuente: Portal de Investigación · Universidad de Murcia'
    },
    {
        'kind': 'person', 'file': 'diapositiva-5-juan-antonio-pastor.svg', 'number': '04',
        'period': 'WEB SEMÁNTICA', 'name': ['Juan Antonio', 'Pastor Sánchez'], 'dates': 'Universidad de Murcia',
        'accent': '#657E83', 'portrait': 'professor2', 'icon': 'nodes',
        'trajectory': ['Profesor titular del Departamento de', 'Información y Documentación.'],
        'contribution': ['Investiga la organización del', 'conocimiento y los tesauros digitales', 'basados en SKOS.'],
        'legacy': ['Su trabajo facilita encontrar, describir', 'y conectar la información en la web.'],
        'source': 'Fuente: Portal de Investigación · Universidad de Murcia'
    },
    {
        'kind': 'person', 'file': 'diapositiva-6-celia-chain.svg', 'number': '05',
        'period': 'PATRIMONIO', 'name': ['Celia María', 'Chaín Navarro'], 'dates': 'Universidad de Murcia',
        'accent': '#A2634B', 'portrait': 'woman2', 'icon': 'map',
        'trajectory': ['Catedrática de Documentación, con', 'formación en Biblioteconomía,', 'Documentación e Historia.'],
        'contribution': ['Ha investigado gestión de información,', 'humanidades digitales, recuperación', 'de información y patrimonio marítimo.'],
        'legacy': ['Conecta la documentación con la', 'investigación histórica y la protección', 'del patrimonio.'],
        'source': 'Fuente: Portal de Investigación · Universidad de Murcia'
    },
    {
        'kind': 'person', 'file': 'diapositiva-7-francisco-javier-martinez.svg', 'number': '06',
        'period': 'CIENCIA ABIERTA', 'name': ['Francisco Javier', 'Martínez Méndez'], 'dates': 'Universidad de Murcia',
        'accent': '#6E738E', 'portrait': 'professor3', 'icon': 'screen',
        'trajectory': ['Catedrático de Biblioteconomía y', 'Documentación. Imparte docencia en', 'la Universidad de Murcia desde 1990.'],
        'contribution': ['Especialista en recuperación de', 'información, gestión documental,', 'tesauros, ontologías y ciencia abierta.'],
        'legacy': ['Impulsa sistemas de información y', 'gestión de contenidos para organizar', 'mejor el conocimiento digital.'],
        'source': 'Fuente: web académica · Universidad de Murcia'
    },
    {'kind': 'sources', 'file': 'diapositiva-8-fuentes.svg'}
]

def t(x, y, text, size, color=None, family='Georgia, serif', weight='400', anchor='start', style='', spacing=0):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color or COLORS["ink"]}" text-anchor="{anchor}" style="{style}" letter-spacing="{spacing}">{escape(text)}</text>'

def multiline(x, y, lines, size, leading, **kwargs):
    return ''.join(t(x, y + i*leading, line, size, **kwargs) for i, line in enumerate(lines))

def paper_defs():
    return '''<defs>
      <radialGradient id="paper" cx="46%" cy="42%" r="78%"><stop offset="0" stop-color="#FBF5EA"/><stop offset=".72" stop-color="#F3E8D6"/><stop offset="1" stop-color="#D8C39E"/></radialGradient>
      <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="3" seed="8"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 .08"/></feComponentTransfer></filter>
      <filter id="shadow"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#382819" flood-opacity=".18"/></filter>
    </defs>'''

def paper_bg():
    return f'''<rect width="{W}" height="{H}" fill="url(#paper)"/>
    <rect width="{W}" height="{H}" filter="url(#grain)" opacity=".45"/>
    <path d="M38 52 Q230 34 420 48 T1042 42 L1036 1308 Q820 1320 614 1304 T42 1312 Z" fill="none" stroke="#805D3A" stroke-opacity=".28" stroke-width="2"/>'''

def icon(kind, x, y, color):
    common = f'stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    if kind == 'book':
        return f'<g transform="translate({x} {y})" {common}><path d="M0 10 Q40 0 70 18 V98 Q38 82 0 92 Z M140 10 Q100 0 70 18 V98 Q102 82 140 92 Z"/><line x1="70" y1="18" x2="70" y2="98"/></g>'
    if kind == 'archive':
        return f'<g transform="translate({x} {y})" {common}><rect x="8" y="12" width="124" height="88" rx="5"/><path d="M0 12h140M48 43h44v28H48z"/><line x1="55" y1="55" x2="85" y2="55"/></g>'
    if kind == 'library':
        return f'<g transform="translate({x} {y})" {common}><path d="M0 35 L70 0 140 35 Z M12 100h116 M25 40v50 M58 40v50 M92 40v50 M125 40v50"/></g>'
    if kind == 'nodes':
        return f'<g transform="translate({x} {y})" {common}><path d="M20 25L70 53 122 20M70 53L28 95M70 53l55 43"/><circle cx="20" cy="25" r="14"/><circle cx="122" cy="20" r="14"/><circle cx="70" cy="53" r="15"/><circle cx="28" cy="95" r="14"/><circle cx="125" cy="96" r="14"/></g>'
    if kind == 'map':
        return f'<g transform="translate({x} {y})" {common}><path d="M0 18L45 2l48 16 47-16v90l-47 16-48-16L0 108z M45 2v90M93 18v90"/><path d="M104 42c0 18-18 35-18 35S68 60 68 42a18 18 0 1 1 36 0z"/><circle cx="86" cy="42" r="5"/></g>'
    return f'<g transform="translate({x} {y})" {common}><rect x="0" y="0" width="140" height="92" rx="8"/><path d="M35 112h70M70 92v20M20 68l25-24 20 14 32-36 25 18"/></g>'

def portrait(kind, accent):
    hair = '#3A302A'
    extra = ''
    if kind in ('woman', 'woman2'):
        extra = f'<path d="M170 210 Q180 75 300 72 Q420 80 430 220 L400 330 Q375 190 300 185 Q220 190 196 330Z" fill="{hair}"/>'
        face = '<ellipse cx="300" cy="210" rx="82" ry="104" fill="#D8B08C"/>'
        if kind == 'woman2': extra += f'<path d="M203 146 Q300 70 402 148" fill="none" stroke="{accent}" stroke-width="16"/>'
    else:
        face = '<ellipse cx="300" cy="210" rx="82" ry="104" fill="#D5A984"/>'
        extra = f'<path d="M219 184 Q224 94 300 91 Q382 94 387 183 Q330 140 219 184Z" fill="{hair}"/>'
        if kind == 'scholar': extra += '<path d="M228 230h55m34 0h55m-89 0h34" stroke="#3A302A" stroke-width="7" fill="none"/><circle cx="255" cy="230" r="28" fill="none" stroke="#3A302A" stroke-width="6"/><circle cx="345" cy="230" r="28" fill="none" stroke="#3A302A" stroke-width="6"/>'
        elif kind == 'professor2': extra += '<path d="M247 278 Q300 315 353 278" fill="none" stroke="#6C4437" stroke-width="10"/>'
        elif kind == 'professor3': extra += '<path d="M230 222h52m36 0h52m-88 0h36" stroke="#3A302A" stroke-width="6"/><rect x="230" y="199" width="52" height="39" rx="9" fill="none" stroke="#3A302A" stroke-width="5"/><rect x="318" y="199" width="52" height="39" rx="9" fill="none" stroke="#3A302A" stroke-width="5"/>'
    return f'''<g transform="translate(0 20)">
      <path d="M82 357 A218 218 0 0 1 518 357 Z" fill="{accent}" opacity=".9"/>
      <path d="M176 565 Q188 365 300 344 Q412 365 424 565Z" fill="#373B3C"/>
      {face}{extra}
      <path d="M260 292 Q300 315 340 292" fill="none" stroke="#9A6654" stroke-width="4" stroke-linecap="round"/>
      <path d="M230 180 Q250 160 274 177 M326 177 Q350 160 371 180" fill="none" stroke="#59443A" stroke-width="5"/>
      <circle cx="255" cy="203" r="5" fill="#3A302A"/><circle cx="345" cy="203" r="5" fill="#3A302A"/>
      <path d="M274 370L300 420l26-50" fill="#F0E4D0"/>
    </g>'''

def cover_svg(s):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', paper_defs()]
    parts += [f'<rect width="{W}" height="{H}" fill="{COLORS["dark"]}"/>',
              '<circle cx="904" cy="145" r="230" fill="#C5A15B" opacity=".09"/>',
              '<circle cx="92" cy="1195" r="300" fill="#C5A15B" opacity=".06"/>',
              t(90, 130, 'SEMINARIO 2  ·  INFORMACIÓN Y DOCUMENTACIÓN', 22, '#C5A15B', 'Arial, sans-serif', '700', spacing=3),
              multiline(90, 342, s['title'], 100, 112, color='#F7F0E4', weight='700'),
              t(92, 625, s['subtitle'], 40, '#C5A15B', style='font-style:italic'),
              multiline(92, 735, s['body'][:2], 34, 50, color='#E8DED0'),
              t(92, 835, s['body'][2], 34, '#F7F0E4', weight='700'),
              '<line x1="92" y1="1060" x2="988" y2="1060" stroke="#C5A15B" stroke-width="4"/>']
    for x, label in [(92,'Siglo XVII'),(390,'1920'),(690,'1980'),(988,'Hoy')]:
        parts += [f'<circle cx="{x}" cy="1060" r="11" fill="#C5A15B"/>', t(x, 1120, label, 27, '#F7F0E4', anchor='middle' if x not in (92,988) else ('start' if x==92 else 'end'))]
    parts += [t(92, 1268, 'DEL SABER HUMANISTA AL DATO DIGITAL', 20, '#9E927F', 'Arial, sans-serif', '700', spacing=4), '</svg>']
    return ''.join(parts)

def person_svg(s):
    accent = s['accent']
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', paper_defs(), paper_bg()]
    parts += [t(76, 102, s['number'], 24, accent, 'Arial, sans-serif', '700'),
              t(120, 102, s['period'], 20, COLORS['muted'], 'Arial, sans-serif', '700', spacing=3),
              f'<line x1="76" y1="130" x2="1004" y2="130" stroke="{accent}" stroke-width="2" opacity=".65"/>',
              multiline(76, 245, s['name'], 70, 74, weight='700'),
              t(80, 400, s['dates'], 28, accent, 'Arial, sans-serif', '700'),
              f'<g transform="translate(24 370) scale(.68)">{portrait(s["portrait"], accent)}</g>',
              icon(s['icon'], 178, 950, accent),
              t(248, 1100, 'ILUSTRACIÓN VECTORIAL ORIGINAL', 14, COLORS['muted'], 'Arial, sans-serif', '700', anchor='middle', spacing=2)]
    sections = [('TRAYECTORIA', s['trajectory']), ('APORTACIÓN', s['contribution']), ('LEGADO', s['legacy'])]
    y = 485
    for title, lines in sections:
        parts += [f'<rect x="455" y="{y-38}" width="12" height="34" rx="6" fill="{accent}"/>',
                  t(486, y-12, title, 20, accent, 'Arial, sans-serif', '700', spacing=3),
                  multiline(486, y+35, lines, 28, 39, color=COLORS['ink'])]
        y += 225 if title != 'LEGADO' else 0
    parts += [f'<line x1="76" y1="1210" x2="1004" y2="1210" stroke="{accent}" stroke-width="2" opacity=".4"/>',
              t(76, 1252, s['source'], 17, COLORS['muted'], 'Arial, sans-serif'),
              t(1004, 1252, f'{s["number"]} / 06', 17, accent, 'Arial, sans-serif', '700', anchor='end'),
              '</svg>']
    return ''.join(parts)

def sources_svg():
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', paper_defs(), paper_bg(),
             t(76, 105, '08  ·  REFERENCIAS', 22, COLORS['sepia'], 'Arial, sans-serif', '700', spacing=4),
             t(76, 240, 'Fuentes', 82, weight='700'), t(76, 324, 'consultadas', 82, weight='700'),
             t(80, 380, 'Información contrastada en fuentes institucionales', 27, COLORS['sepia'], style='font-style:italic')]
    entries = [
        ('01', 'Real Academia de la Historia', 'Francisco Cascales.'),
        ('02', 'Ministerio de Cultura', 'Áurea Javierre, primera archivera del Archivo de la Corona de Aragón.'),
        ('03', 'Universidad de Murcia', 'Portal de Investigación de José Antonio Gómez Hernández.'),
        ('04', 'Universidad de Murcia', 'Portal de Investigación de Juan Antonio Pastor Sánchez.'),
        ('05', 'Universidad de Murcia', 'Portal de Investigación de Celia María Chaín Navarro.'),
        ('06', 'Universidad de Murcia', 'Web académica de Francisco Javier Martínez Méndez.')]
    y = 470
    for num, org, desc in entries:
        parts += [f'<circle cx="99" cy="{y-8}" r="23" fill="#865C3A"/>', t(99, y, num, 14, '#F7F0E4', 'Arial, sans-serif', '700', anchor='middle'),
                  t(145, y-10, org, 25, COLORS['ink'], 'Arial, sans-serif', '700'),
                  t(145, y+27, desc, 21, COLORS['muted'], 'Arial, sans-serif')]
        y += 105
    parts += [f'<rect x="76" y="1110" width="928" height="130" rx="8" fill="{COLORS["dark"]}"/>',
              t(540, 1160, 'DE ESCRIBAS A GESTORES DIGITALES', 18, COLORS['gold'], 'Arial, sans-serif', '700', anchor='middle', spacing=3),
              t(540, 1202, 'De conservar documentos a gestionar datos:', 24, COLORS['cream'], anchor='middle'),
              t(540, 1232, 'la información sigue siendo la base del conocimiento.', 24, COLORS['cream'], anchor='middle'),
              t(76, 1300, 'EQUIPO: _________________________________________________', 18, COLORS['muted'], 'Arial, sans-serif', '700', spacing=2),
              '</svg>']
    return ''.join(parts)

def index_html():
    cards = '\n'.join(f'<figure><img src="{s["file"]}" alt="Diapositiva {i}"><figcaption>Diapositiva {i}</figcaption></figure>' for i,s in enumerate(slides, 1))
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Seminario 2 · Carrusel</title><style>body{{margin:0;background:#202020;color:#eee;font-family:Arial,sans-serif}}header{{padding:28px;text-align:center}}main{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:28px;padding:0 28px 50px;max-width:1500px;margin:auto}}figure{{margin:0}}img{{display:block;width:100%;height:auto;box-shadow:0 12px 30px #0008}}figcaption{{padding:10px;text-align:center;color:#bbb}}</style></head><body><header><h1>De escribas a gestores digitales</h1><p>Carrusel vertical · 1080 × 1350 px</p></header><main>{cards}</main></body></html>'''

for s in slides:
    svg = cover_svg(s) if s['kind']=='cover' else person_svg(s) if s['kind']=='person' else sources_svg()
    (OUT / s['file']).write_text(svg, encoding='utf-8')

(OUT / 'vista-carrusel.html').write_text(index_html(), encoding='utf-8')
(OUT / 'carrusel.html').write_text(index_html(), encoding='utf-8')
print(f'Generadas {len(slides)} diapositivas SVG y dos vistas HTML')
