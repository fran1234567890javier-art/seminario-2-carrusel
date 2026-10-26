from pathlib import Path
from html import escape

OUT = Path('/projects/sandbox/seminario-2')
W, H = 2480, 3508
INK = '#202427'
CREAM = '#F7F0E3'
PAPER = '#E9DDC8'
GOLD = '#D3A84B'
MUTED = '#6E6A61'

profiles = [
    {
        'n':'01','name':['Francisco','Cascales'],'meta':'c. 1559–1642 · HUMANISMO','accent':'#B87345','icon':'book',
        'lead':'Organizó la memoria cultural de Murcia.',
        'body':['Humanista, filólogo e historiador. Recopiló y difundió',
                'conocimiento sobre historia, lengua y literatura. Sus obras',
                'anticipan la tarea de transmitir información fiable.']
    },
    {
        'n':'02','name':['Áurea Lucinda','Javierre Mur'],'meta':'1898–1980 · ARCHIVOS','accent':'#9B6670','icon':'archive',
        'lead':'La primera archivera de la Corona de Aragón.',
        'body':['Ingresó en el Cuerpo Facultativo de Archiveros en 1921.',
                'Trabajó con fondos históricos de gran valor, abrió camino',
                'a las mujeres y preservó el patrimonio documental.']
    },
    {
        'n':'03','name':['José Antonio','Gómez Hernández'],'meta':'UNIVERSIDAD DE MURCIA · BIBLIOTECAS','accent':'#71856D','icon':'library',
        'lead':'Bibliotecas para aprender, incluir y participar.',
        'body':['Catedrático y antiguo bibliotecario universitario. Referente',
                'en alfabetización informacional, gestión y marketing de',
                'bibliotecas; ha formado a generaciones de profesionales.']
    },
    {
        'n':'04','name':['Juan Antonio','Pastor Sánchez'],'meta':'UNIVERSIDAD DE MURCIA · WEB SEMÁNTICA','accent':'#527E89','icon':'nodes',
        'lead':'Conectar conceptos para encontrar conocimiento.',
        'body':['Profesor titular especializado en organización del',
                'conocimiento y tesauros digitales basados en SKOS.',
                'Facilita describir, relacionar y recuperar información web.']
    },
    {
        'n':'05','name':['Celia María','Chaín Navarro'],'meta':'UNIVERSIDAD DE MURCIA · PATRIMONIO','accent':'#A65F49','icon':'map',
        'lead':'Documentar el pasado para proteger el patrimonio.',
        'body':['Catedrática con formación en Documentación e Historia.',
                'Investiga gestión y recuperación de información, humanidades',
                'digitales y patrimonio marítimo.']
    },
    {
        'n':'06','name':['Francisco Javier','Martínez Méndez'],'meta':'UNIVERSIDAD DE MURCIA · CIENCIA ABIERTA','accent':'#6A7196','icon':'screen',
        'lead':'Sistemas digitales para organizar mejor el saber.',
        'body':['Catedrático y docente desde 1990. Especialista en recuperación',
                'de información, gestión documental, tesauros, ontologías y',
                'ciencia abierta.']
    }
]

def txt(x,y,s,size,color=INK,weight=400,family='Arial, sans-serif',anchor='start',spacing=0,style=''):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" letter-spacing="{spacing}" style="{style}">{escape(s)}</text>'

def icon(kind,x,y,color):
    st=f'stroke="{color}" stroke-width="13" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    if kind=='book': d='<path d="M0 18q70-20 116 12v145q-58-28-116-9zm232 0q-70-20-116 12v145q58-28 116-9zM116 30v145"/>'
    elif kind=='archive': d='<rect x="12" y="20" width="208" height="150" rx="12"/><path d="M0 20h232M75 78h82v54H75z"/>'
    elif kind=='library': d='<path d="M0 63L116 0l116 63zM18 182h196M40 72v88m50-88v88m52-88v88m50-88v88"/>'
    elif kind=='nodes': d='<path d="M30 35l86 60 86-60M116 95l-70 83m70-83l78 83"/><circle cx="30" cy="35" r="25"/><circle cx="202" cy="35" r="25"/><circle cx="116" cy="95" r="27"/><circle cx="46" cy="178" r="25"/><circle cx="194" cy="178" r="25"/>'
    elif kind=='map': d='<path d="M0 30L75 4l82 26 75-26v157l-75 26-82-26-75 26zM75 4v157m82-131v157"/><path d="M177 68c0 35-35 68-35 68s-35-33-35-68a35 35 0 1170 0z"/><circle cx="142" cy="68" r="8"/>'
    else: d='<rect x="0" y="0" width="232" height="154" rx="15"/><path d="M58 190h116m-58-36v36M30 115l43-42 35 25 54-60 42 31"/>'
    return f'<g transform="translate({x} {y})" {st}>{d}</g>'

def portrait(x,y,accent,variant):
    hair = '#292A2B'
    if variant in (1,4):
        hairshape='<path d="M75 170Q72 25 210 22Q348 25 345 174L322 255Q300 125 210 122Q118 127 98 255Z" fill="#292A2B"/>'
    else:
        hairshape='<path d="M105 128Q112 30 210 28Q312 30 318 130Q258 77 105 128Z" fill="#292A2B"/>'
    glasses = '<g fill="none" stroke="#292A2B" stroke-width="9"><circle cx="158" cy="157" r="35"/><circle cx="262" cy="157" r="35"/><path d="M193 157h34"/></g>' if variant in (0,3,5) else ''
    return f'''<g transform="translate({x} {y})">
      <circle cx="210" cy="210" r="205" fill="{accent}" opacity=".16"/>
      <circle cx="210" cy="210" r="178" fill="{accent}"/>
      <path d="M42 396Q62 278 210 270Q358 278 378 396Z" fill="#303538"/>
      <ellipse cx="210" cy="158" rx="104" ry="128" fill="#D9AB86"/>
      {hairshape}{glasses}
      <circle cx="158" cy="158" r="7" fill="{hair}"/><circle cx="262" cy="158" r="7" fill="{hair}"/>
      <path d="M172 220Q210 246 248 220" fill="none" stroke="#925F4E" stroke-width="7" stroke-linecap="round"/>
      <path d="M165 290l45 72 45-72" fill="#F1E5D4"/>
    </g>'''

def card(p,x,y,variant):
    a=p['accent']; parts=[]
    parts.append(f'<g filter="url(#shadow)"><rect x="{x}" y="{y}" width="1060" height="640" rx="34" fill="{CREAM}"/></g>')
    parts.append(f'<rect x="{x}" y="{y}" width="18" height="640" rx="9" fill="{a}"/>')
    parts.append(txt(x+990,y+95,p['n'],94,a,800,anchor='end'))
    parts.append(portrait(x+55,y+92,a,variant))
    parts.append(icon(p['icon'],x+150,y+470,a))
    tx=x+495
    parts.append(txt(tx,y+105,p['meta'],22,a,800,spacing=2.2))
    parts.append(txt(tx,y+185,p['name'][0],53,INK,700,'Georgia, serif'))
    parts.append(txt(tx,y+242,p['name'][1],53,INK,700,'Georgia, serif'))
    parts.append(f'<line x1="{tx}" y1="{y+275}" x2="{x+995}" y2="{y+275}" stroke="{a}" stroke-width="4"/>')
    parts.append(txt(tx,y+328,p['lead'],29,a,700,'Georgia, serif',style='font-style:italic'))
    for i,line in enumerate(p['body']):
        parts.append(txt(tx,y+400+i*43,line,25,INK,400,'Georgia, serif'))
    parts.append(txt(tx,y+578,'TRAYECTORIA  ·  APORTACIÓN  ·  LEGADO',18,MUTED,700,spacing=2.1))
    return ''.join(parts)

def poster():
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '''<defs>
      <radialGradient id="bg" cx="50%" cy="30%" r="90%"><stop offset="0" stop-color="#30383B"/><stop offset="1" stop-color="#171A1C"/></radialGradient>
      <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".45" numOctaves="4" seed="12"/><feComponentTransfer><feFuncA type="table" tableValues="0 .09"/></feComponentTransfer></filter>
      <filter id="shadow"><feDropShadow dx="0" dy="20" stdDeviation="22" flood-color="#000" flood-opacity=".25"/></filter>
    </defs>''',
    f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
    f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity=".5"/>',
    '<circle cx="2200" cy="30" r="620" fill="#D3A84B" opacity=".07"/><circle cx="80" cy="3430" r="500" fill="#D3A84B" opacity=".05"/>',
    txt(140,135,'SEMINARIO 2  ·  INFORMACIÓN Y DOCUMENTACIÓN',24,GOLD,800,spacing=4),
    txt(140,310,'De escribas a',112,CREAM,700,'Georgia, serif'),
    txt(140,430,'gestores digitales',112,GOLD,700,'Georgia, serif'),
    txt(142,515,'Huellas de una profesión en Murcia',38,PAPER,400,'Georgia, serif',style='font-style:italic'),
    txt(2350,240,'XVII',150,'#FFFFFF',800,anchor='end',style='opacity:.07'),
    txt(2350,400,'→ HOY',105,'#FFFFFF',800,anchor='end',style='opacity:.07'),
    '<line x1="140" y1="590" x2="2340" y2="590" stroke="#D3A84B" stroke-width="3" opacity=".7"/>',
    txt(140,648,'SEIS PERSONAS · UNA MISMA MISIÓN:',25,GOLD,800,spacing=3),
    txt(775,648,'CONSERVAR, ORGANIZAR Y COMPARTIR EL CONOCIMIENTO',25,CREAM,800,spacing=2.4)]
    positions=[(140,720),(1280,720),(140,1400),(1280,1400),(140,2080),(1280,2080)]
    for i,(p,(x,y)) in enumerate(zip(profiles,positions)):
        out.append(card(p,x,y,i))
    out += [
      '<line x1="140" y1="2805" x2="2340" y2="2805" stroke="#D3A84B" stroke-width="3"/>',
      txt(140,2890,'LA EVOLUCIÓN EN UNA MIRADA',23,GOLD,800,spacing=3),
      '<line x1="185" y1="3005" x2="2290" y2="3005" stroke="#D3A84B" stroke-width="6"/>']
    years=[(185,'SIGLO XVII','MEMORIA'),(590,'1921','ARCHIVOS'),(995,'1984','BIBLIOTECAS'),(1400,'WEB','CONEXIONES'),(1805,'PATRIMONIO','HUMANIDADES'),(2290,'HOY','DATOS')]
    for x,yr,label in years:
        out += [f'<circle cx="{x}" cy="3005" r="19" fill="{GOLD}"/>',txt(x,3070,yr,25,CREAM,800,anchor='middle'),txt(x,3110,label,17,PAPER,700,anchor='middle',spacing=2)]
    out += [
      f'<rect x="140" y="3170" width="2200" height="150" rx="25" fill="{GOLD}"/>',
      txt(1240,3230,'DE CONSERVAR DOCUMENTOS A GESTIONAR DATOS',26,INK,800,anchor='middle',spacing=3),
      txt(1240,3282,'La información sigue siendo la base del conocimiento.',34,INK,700,'Georgia, serif',anchor='middle'),
      txt(140,3380,'FUENTES: Real Academia de la Historia · Ministerio de Cultura · Portales de Investigación y webs académicas de la Universidad de Murcia',18,PAPER,400),
      txt(140,3422,'Retratos conceptuales: ilustraciones vectoriales originales. No se reproducen fotografías sin licencia abierta verificada.',16,'#B8B0A4',400),
      txt(2340,3422,'EQUIPO: __________________________________',18,GOLD,700,anchor='end'),
      '</svg>']
    return ''.join(out)

svg=poster()
(OUT/'poster-seminario-2-a3.svg').write_text(svg,encoding='utf-8')
html='''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Póster Seminario 2</title><style>body{margin:0;background:#555;display:grid;place-items:center;padding:30px}img{width:min(92vw,900px);height:auto;box-shadow:0 20px 70px #0009}</style></head><body><img src="poster-seminario-2-a3.svg" alt="Póster De escribas a gestores digitales"></body></html>'''
(OUT/'poster.html').write_text(html,encoding='utf-8')
print('Póster A3 generado: 2480 × 3508 px')
