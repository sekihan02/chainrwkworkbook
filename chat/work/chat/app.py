import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder=".", static_folder="static")

messages = []

def create_image():
    sns.set(style="whitegrid")
    tips = sns.load_dataset("tips")
    ax = sns.boxplot(x=tips["total_bill"])
    img = BytesIO()
    ax.figure.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        if message == "画像":
            messages.append((message, "画像を出力します。", False, False))
            response = create_image()
            messages.append(("", response, True, True))
        elif message == "クリア":
            messages.clear()
        else:
            response = "Hello World!"
            messages.append((message, response, False, False))
    return render_template("template.html", messages=messages)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.get_json()["user_input"]
    
    response = "Hello World!"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
