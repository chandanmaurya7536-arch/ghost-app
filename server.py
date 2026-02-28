from flask import Flask, request
import requests

TOKEN = "8777436576:AAEYiKjDdLROJUJoQeW3Ltf5iShIwG3VwRk"
CHAT_ID = "8391954882"

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file.filename.endswith((".jpg", ".png", ".jpeg")):
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

app.run(host="0.0.0.0", port=5000)