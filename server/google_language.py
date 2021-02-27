from google.cloud import language
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'LanguageToken.json'

class Language_Model:
    def __init__(self):
        self.client = language.LanguageServiceClient()
        self.encoding_type = language.EncodingType.UTF8
        self.type_ = language.Document.Type.PLAIN_TEXT

    def tweet_sentiment(self, tweet):
        document = {"content": tweet, "type_": self.type_}
        sentiment = self.client.analyze_sentiment(request = {'document': document, 'encoding_type': self.encoding_type}).document_sentiment
        return sentiment

    def tweet_entities(self, tweet):
        document = {"content": tweet, "type_": self.type_}
        entities = self.client.analyze_entities(request = {'document': document, 'encoding_type': self.encoding_type}).entities
        return entities

if __name__ == "__main__":
    model = Language_Model()
    tweet = "Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."
    print(model.tweet_sentiment(tweet))
    print(model.tweet_entities(tweet))