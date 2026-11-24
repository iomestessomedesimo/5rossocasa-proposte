# Pubblicazione su dominio ufficiale (Aruba) — 5 ROSSO CASA

GitHub Pages è ambiente di sviluppo, verifica e archiviazione. La destinazione commerciale è **https://www.5rossocasa.it/** (indirizzo canonico).
Documento interno: non caricare su Aruba.

## Versione di riferimento
- Sorgente: `natale-2026/index.html` (commit di pubblicazione `a2aad34`, derivato da `anteprima-netta` `9197de8`).
- Pacchetto di produzione generato da `aruba/build_produzione.py`: stessa pagina approvata, senza `noindex`, con title/description, canonical `https://www.5rossocasa.it/`, Open Graph, dati strutturati Schema.org `Store` (solo indirizzo, social e orari di dicembre verificati; **nessun telefono**, il numero noto è quello WhatsApp), `robots.txt`, `sitemap.xml`, `.htaccess`.
- Copia del pacchetto sul Mac: `05_DESIGN/pubblicato_aruba_2026-11-24/`.
- Data di pubblicazione sul dominio: **da registrare** (non ancora avvenuta, vedi «Attività residue»).

## Stato del dominio al 24/11/2026 (rilevato dall'esterno)
- Il dominio serve ancora il progetto SuperSite con contenuti segnaposto del template («Spazio Macramè», Catania, «Tel 1234567890»). Indirizzo effettivo: `https://5rossocasa.it/` (www reindirizza al dominio senza www: è l'inverso del canonico richiesto).
- `robots.txt` generato da SuperSite (Crawl-delay 30, sitemap su dominio senza www), `sitemap.xml` con le pagine segnaposto.
- Stato di servizi, hosting, DNS, SSL e posta: da verificare nel pannello Aruba (accesso richiesto).

## Procedura di aggiornamento (hosting con caricamento file)
1. Modificare `natale-2026/index.html` (o la versione ordinaria) e committare.
2. `python3 aruba/build_produzione.py <cartella>` genera il pacchetto.
3. Caricare il contenuto della cartella nella radice pubblica dell'hosting (FTP/File Manager), inclusi `.htaccess`, `robots.txt`, `sitemap.xml`.
4. Verificare: `https://www.5rossocasa.it/`, redirect da `http://` e dal dominio senza www (301), `robots.txt`, `sitemap.xml`, immagini.
5. Archiviare sul Mac la copia pubblicata e annotare data e commit qui.

## Procedura di ripristino
- Ricaricare l'ultima copia in `05_DESIGN/pubblicato_aruba_*` oppure rigenerare il pacchetto dal commit registrato.
- Prima di ogni sostituzione scaricare una copia dello stato corrente dell'hosting.

## Passaggio alla versione ordinaria a fine festività
Sostituire `index.html` (e le immagini non più usate) con la versione ordinaria, riaggiornare `sitemap.xml`; title, description, dati strutturati e orari (la specifica di dicembre ha `validThrough 2026-12-31`) vanno riscritti nello script. Nessuna ricostruzione del sito è necessaria.

## SEO configurata nel pacchetto
Title e description con Firenze, Cure, articoli per la casa; canonical www; Open Graph/Twitter card (immagine: locandina); JSON-LD `Store`; `robots.txt` con `Allow: /` e riferimento alla sitemap; sitemap con la sola homepage; testi alternativi su tutte le immagini. Le copie su GitHub Pages (`natale-2026`, `anteprima-netta`) mantengono `noindex`.

## Attività residue
- Accesso al pannello Aruba (non disponibile nel browser senza login) e scelta dell'hosting: SuperSite non consente di caricare file propri; la soluzione prevista è Hosting Linux. **Qualsiasi acquisto o cambio di piano richiede autorizzazione.**
- Reindirizzamenti, DNS, SSL, posta (da preservare).
- Google Search Console: verifica proprietà, invio sitemap, richiesta di indicizzazione della homepage (richiede accesso dell'account Google).
- Autorizzazioni fotografiche dei fornitori: vedi `natale-2026/CREDITI-IMMAGINI.md`.
