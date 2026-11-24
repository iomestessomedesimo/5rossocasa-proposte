#!/usr/bin/env python3
"""Genera il pacchetto di produzione per il dominio ufficiale (Aruba) a partire da natale-2026/index.html.

Uso:  python3 aruba/build_produzione.py [cartella_output]
Non modifica natale-2026/ (che resta noindex su GitHub Pages). Il pacchetto NON va committato nel repository
(sarebbe una copia indicizzabile su github.io): si carica solo sull'hosting Aruba.
"""
import re, sys, shutil, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT.parent / "5rossocasa-produzione")
SITE = "https://www.5rossocasa.it"
TITLE = "5 Rosso Casa — Articoli per la casa a Firenze (Le Cure) · Natale 2026"
DESC = ("5 Rosso Casa, negozio di articoli per la casa alle Cure, a Firenze: cucina, tavola e dispensa, tessili, "
        "zerbini e idee regalo per il Natale. A dicembre sempre aperti, tutti i giorni, 9–13 / 16–19.")
OGIMG = SITE + "/img/natale_locandina.jpg"

h = (ROOT / "natale-2026" / "index.html").read_text(encoding="utf-8")
h = h.replace('<meta name="robots" content="noindex,nofollow">', "")
assert "noindex" not in h and "nofollow" not in h
h = h.replace("../img/", "img/")
h = re.sub(r"<title>.*?</title>", "<title>%s</title>" % TITLE, h, count=1)
spec = lambda a, b: ('{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],'
                     '"opens":"%s","closes":"%s","validFrom":"2026-12-01","validThrough":"2026-12-31"}' % (a, b))
ld = ('{"@context":"https://schema.org","@type":"Store","name":"5 Rosso Casa","url":"%s/","image":"%s",'
      '"description":"Negozio di articoli per la casa a Firenze: cucina, tavola, tessili, zerbini e idee regalo.",'
      '"address":{"@type":"PostalAddress","streetAddress":"Via Agnolo Firenzuola, 5r","addressLocality":"Firenze","postalCode":"50133","addressCountry":"IT"},'
      '"hasMap":"https://www.google.com/maps/search/?api=1&query=Via+Agnolo+Firenzuola+5r+50133+Firenze",'
      '"sameAs":["https://www.instagram.com/5rosso_casa_/","https://www.facebook.com/5rossoflorence"],'
      '"openingHoursSpecification":[%s,%s]}') % (SITE, OGIMG, spec("09:00", "13:00"), spec("16:00", "19:00"))
head = ('<meta name="description" content="%s">\n<link rel="canonical" href="%s/">\n'
        '<meta property="og:type" content="website"><meta property="og:locale" content="it_IT"><meta property="og:site_name" content="5 Rosso Casa">\n'
        '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s/">\n'
        '<meta property="og:image" content="%s"><meta property="og:image:alt" content="Locandina di 5 Rosso Casa: il tuo negozietto di quartiere">\n'
        '<meta name="twitter:card" content="summary_large_image">\n<script type="application/ld+json">%s</script>\n') % (DESC, SITE, TITLE, DESC, SITE, OGIMG, ld)
h = h.replace("</title>", "</title>\n" + head, 1)

if OUT.exists():
    shutil.rmtree(OUT)
(OUT / "img").mkdir(parents=True)
used = sorted(set(re.findall(r"img/([A-Za-z0-9_.\-]+)", h)))
for f in used:
    shutil.copy2(ROOT / "img" / f, OUT / "img" / f)
(OUT / "index.html").write_text(h, encoding="utf-8")
(OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    '  <url><loc>%s/</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>\n</urlset>\n'
    % (SITE, datetime.date.today().isoformat()))
(OUT / ".htaccess").write_text("""# 5 Rosso Casa — Hosting Linux Aruba (Apache)
DirectoryIndex index.html
Options -Indexes
RewriteEngine On
# canonico: https + www, redirect permanente
RewriteCond %{HTTPS} !=on [OR]
RewriteCond %{HTTP_HOST} !^www\\. [NC]
RewriteRule ^ https://www.5rossocasa.it%{REQUEST_URI} [L,R=301]
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType image/jpeg "access plus 30 days"
ExpiresByType image/png "access plus 30 days"
ExpiresByType text/html "access plus 10 minutes"
</IfModule>
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript application/xml
</IfModule>
""")
missing = [f for f in used if not (OUT / "img" / f).exists()]
print("pacchetto:", OUT, "| immagini:", len(used), "| mancanti:", missing)
