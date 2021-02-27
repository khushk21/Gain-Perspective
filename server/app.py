from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from google_language import LanguageModel
from news_extraction import NewsExtraction
from toxicity_analysis import text_analysis

app = Flask(__name__)
CORS(app)
PORT = os.getenv('PORT',8000)
language_model = LanguageModel()
news_retrieval = NewsExtraction()

@app.route("/endpoint", methods=["GET"])
def endpoint():
    text = request.args.get("text")
    sentiment = language_model.text_sentiment(text).score
    entities = language_model.text_entities(text)
    articles = news_retrieval.get_news_articles(entities)
    toxicity = ["No toxicity detected! Keep smiling :)"]
    if sentiment <= -0:
        toxicity = text_analysis(text)
        if "error" not in toxicity:
            toxicity = toxicity['result']
        else:
            toxicity = ["toxic"]
    return {"articles" : articles, "toxicity" : toxicity}

@app.route("/", methods=["GET"])
def main():
    return "Welcome to Intuition Hack"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)