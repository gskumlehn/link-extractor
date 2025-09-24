from flask import Flask, request, Response, jsonify, send_from_directory
from main import extrair_links_de_artigos
import json

app = Flask(__name__, static_folder="static", static_url_path="")

@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.post("/upload")
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400
    file = request.files["file"]
    pdf_bytes = file.read()
    if not pdf_bytes:
        return jsonify({"erro": "Arquivo vazio"}), 400

    resultado = extrair_links_de_artigos(pdf_bytes)
    payload = json.dumps(resultado, ensure_ascii=False, indent=2)
    return Response(
        payload,
        mimetype="application/json",
        headers={"Content-Disposition": 'attachment; filename="artigos.json"'}
    )
