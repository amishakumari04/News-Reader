import requests
import json
lines=int(input("How many headlines do you want ? : "))
category=input("Enter Category of headlines(possible options: business,entertainment,general,health,science,sports,technology) : ").lower()
url=f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=923705fe3bea439a8bc9fc5eef2412b1"
r=requests.get(url)
news=json.loads(r.text)
i=1
for article in news['articles']:
    if(i<=lines):
        print(article["title"] +"\n")
        i=i+1    
    else:
        break

