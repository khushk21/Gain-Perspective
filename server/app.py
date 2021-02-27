from flask import Flask, request
from flask_cors import CORS
import os
from google_language import LanguageModel
from news_extraction import NewsExtraction

app = Flask(__name__)
CORS(app)
PORT = os.getenv('PORT',8000)
language_model = LanguageModel()
news_retrieval = NewsExtraction()

@app.route("/endpoint", methods=["GET"])
def endpoint():
    tweet = request.args.get("tweet")
    sentiment = language_model.tweet_sentiment(tweet)
    entities = language_model.tweet_entities(tweet)
    articles = news_retrieval.get_news_article(entities)
    if sentiment < -0.2:
        # Do Perspective Model
        pass
    return

@app.route("/", methods=["GET"])
def main():
    return "Welcome to Intuition Hack"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)