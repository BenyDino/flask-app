from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola desde la nube!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port, debug=True)
