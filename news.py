import requests
import json
query=input("What type of news are you interested in ?")
date=input("Date (in yyyy-mm-dd format) ?")
url=f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey=923705fe3bea439a8bc9fc5eef2412b1"
r=requests.get(url)
news=json.loads(r.text)
#print(news, type(news))
for article in news['articles']:
    print("title:  "+ article["title"] +"\n")
    print("description:  "+article["description"]+"\n ------------------------------------------------------\n")
    
    