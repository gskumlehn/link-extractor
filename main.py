import fitz

def extrair_links_de_artigos(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    artigos = []
    titulo_temp = None
    link_titulo_temp = None
    link_original_temp = None

    for page in doc:
        links = page.get_links()
        texto_pag = page.get_text("blocks")

        for b in texto_pag:
            bloco_texto = b[4].strip()

            for l in links:
                if "uri" in l and l["uri"] and fitz.Rect(b[:4]).intersects(fitz.Rect(l["from"])):
                    if "link original" not in bloco_texto.lower() and "original link" not in bloco_texto.lower():
                        titulo_temp = bloco_texto
                        link_titulo_temp = l["uri"]
                        break

            if bloco_texto.lower() in ["link original", "original link"]:
                for l in links:
                    if "uri" in l and l["uri"] and fitz.Rect(b[:4]).intersects(fitz.Rect(l["from"])):
                        link_original_temp = l["uri"]
                        break

            if titulo_temp and link_titulo_temp and link_original_temp:
                artigos.append({
                    "titulo": titulo_temp,
                    "link_titulo": link_titulo_temp,
                    "link_original": link_original_temp
                })
                titulo_temp = None
                link_titulo_temp = None
                link_original_temp = None

    doc.close()
    return artigos
