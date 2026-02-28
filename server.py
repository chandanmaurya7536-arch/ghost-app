from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("8777436576:AAEYiKjDdLROJUJoQeW3Ltf5iShIwG3VwRk")
CHAT_ID = os.environ.get("8391954882")

@app.route("/")
def home():
    return "Server Running"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
            data={"chat_id": CHAT_ID},
            files={"photo": file}
        )
    else:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendDocument",
            data={"chat_id": CHAT_ID},
            files={"document": file}
        )

    return "Uploaded"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
