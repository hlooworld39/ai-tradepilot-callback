
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "AI TradePilot",
        "status": "Callback service running",
        "mode": "Paper Trading"
    })

@app.route("/callback")
def callback():
    # Do not print or expose authentication tokens.
    return jsonify({
        "status": "Callback endpoint active",
        "message": "AI TradePilot callback reached successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
