from flask import Flask
from .routes import chat

app = Flask(__name__)
app.register_blueprint(chat.bp)
