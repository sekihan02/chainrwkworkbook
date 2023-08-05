"""
    ユーザーがプロンプトを送信したときに、まず全体的なプロットを生成します。次に、このプロットを文章に分割し、各文章について詳細なバージョンを生成します。最後に、詳細な文章を結合して小説を作成します。
"""
from flask import Blueprint, render_template, request
import openai
import re
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

bp = Blueprint('chat', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']
        messages = [
            {"role": "system", "content": prompt},
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            # max_tokens=2000,  # We first generate a plot within 800 tokens
            temperature=0.8
        )
        plot = response["choices"][0]["message"]["content"].strip()

        # Split the plot into sentences
        sentences = re.split('。', plot)

        # Generate a detailed version for each sentence
        detailed_sentences = [generate_detailed_sentence(s) for s in sentences]

        # Join the detailed sentences into a single story
        novel = '。'.join(detailed_sentences)
        
        # If the generated novel is too long, we trim it to 4000 characters
        # novel = novel[:4000]

        return render_template('index.html', novel=novel)
    return render_template('index.html', novel="")

def generate_detailed_sentence(sentence):
    prompt = sentence + " より詳細を日本語で生成: "
    messages = [
        {"role": "system", "content": prompt},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        # max_tokens=2000,  # We generate more detail for the sentence within 100 tokens
        temperature=0.8
    )
    detailed_sentence = response["choices"][0]["message"]["content"].strip()
    # return sentence + detailed_sentence
    return detailed_sentence