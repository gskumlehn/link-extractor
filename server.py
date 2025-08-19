from flask import Flask, request, jsonify
from main import extrair_links_de_artigos

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"erro": "Nome de arquivo inválido"}), 400

    if not file.filename.endswith(".pdf"):
        return jsonify({"erro": "Formato inválido. Envie um PDF"}), 400

    pdf_bytes = file.read()
    resultado = extrair_links_de_artigos(pdf_bytes)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
