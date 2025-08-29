from flask import Flask, request, Response, jsonify, send_from_directory
from main import extrair_links_de_artigos
import json

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"erro": "Nome de arquivo inválido"}), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"erro": "Formato inválido. Envie um PDF"}), 400

    pdf_bytes = file.read()
    file.close()

    if not pdf_bytes:
        return jsonify({"erro": "Arquivo vazio"}), 400

    resultado = extrair_links_de_artigos(pdf_bytes)

    payload = json.dumps(resultado, ensure_ascii=False, indent=2)
    return Response(
        payload,
        mimetype="application/json",
        headers={"Content-Disposition": 'attachment; filename="artigos.json"'}
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
