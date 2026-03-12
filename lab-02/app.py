from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
# Assuming you will name your rail fence file rail_fence.py in the cipher folder
from cipher.railfence import RailFenceCipher 

app = Flask(__name__)

# --- HOME PAGE ---
@app.route("/")
def home():
    return render_template('index.html')

# --- CAESAR CIPHER ROUTES ---
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# --- RAIL FENCE CIPHER ROUTES ---
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    rail_fence = RailFenceCipher()
    encrypted_text = rail_fence.encrypt_text(text, key)
    return f"text: {text}<br/>rails: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    rail_fence = RailFenceCipher()
    decrypted_text = rail_fence.decrypt_text(text, key)
    return f"text: {text}<br/>rails: {key}<br/>decrypted text: {decrypted_text}"

# --- MAIN FUNCTION ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)