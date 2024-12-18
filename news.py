from bs4 import BeautifulSoup
import requests
import pandas as pd

columns = ['title', 'datetime', 'source', 'link', 'top_sentiment', 'sentiment_score']
df = pd.DataFrame(columns = columns)

counter = 0

for page in range(1, 180):
    url = f"https://markets.businessinsider.com/news/nvda-stock?p={page}"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.find_all('div', class_ = 'latest-news__story')

    for article in articles:
        title = article.find('a', class_ = 'news-link').text
        datetime = article.find('time', class_ = 'latest-news__date').get('datetime')
        source = article.find('span', class_ = 'latest-news__source').text
        link = article.find('a', class_ = 'news-link').get('href')

        top_sentiment = ''
        sentiment_score = 0

        df = pd.concat([pd.DataFrame([[title, datetime, source, link, top_sentiment, sentiment_score]], columns=df.columns), df], ignore_index=True)
        counter += 1

    print(f"Page number {page} scraped.")    

print(f"{counter} headlines scraped.")
df.to_csv('/Users/abelsaj/Documents/Personal Coding Projects/Stock-Prediction-Model/nvda.csv')
