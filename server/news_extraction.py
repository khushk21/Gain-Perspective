from newsapi import NewsApiClient
from constants import IMP_ENTITY_TYPE, NEWS_API_KEY
from google_language import LanguageModel

class NewsExtraction:
    def __init__(self):
        self.client = NewsApiClient(api_key=NEWS_API_KEY)
        self.list_of_sources = "bbc-news, cnn, the-new-york-times"
    
    def get_news_articles(self, entities):
        key_entities = []
        for entity in entities:
            if entity.type_ in IMP_ENTITY_TYPE:
                key_entities.append(entity.name)
        result = []
        for i in range(len(key_entities)):
            try:
                response = self.client.get_everything(q='+'.join(key_entities[:len(key_entities)-i]),
                                                        sources=self.list_of_sources,
                                                        language="en",
                                                        sort_by="relevancy",
                                                        page_size=10)['articles']
                result = result + response
            except:
                response = None
            if len(result) >= 5:
                break
        return result

if __name__ == "__main__":
    model = LanguageModel()
    text = "Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."
    entities = model.text_entities(text)
    news = NewsExtraction()
    print(news.get_news_articles(entities))