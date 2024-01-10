import requests
import json

# print("in - India,us - usa etc")
# country=input("Enter the country: ")
# print("The category are business  entertainment  general  health  science  sports  technology")
# category=input("Enter category: ")
# url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=293e896d927a435eae245b5084a92c52"
# r = requests.get(url)
# print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# for heading in soup.find_all("h2"):
#   print(heading.text)

# print("press 1 for India")
# print("press 2 for Usa")
print("press 1 top headlines")
print("press 2 search articles on any topic")
selected=input("Press to continue: ")
if selected=="1":
    country="In"
    print("press 1 for business , 2 for entertainment, 3 for  general, 4 for health,5 for science,6 for sports,7 for technology")
    category=input("Selectd category: ")
    if category=="1":
        category="business"
    elif category=="2":
        category="entertainment"
    elif category=="3":
        category="general"
    elif category=="4":
        category="health"
    elif category=="5":
        category="science"
    elif category=="6":
        category="sports"
    elif category=="7":
        category="technology"
    if country=="1":
        country="In"    
    if country=="2":
        country="us"    
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=293e896d927a435eae245b5084a92c52"
    r = requests.get(url)
    news = json.loads(r.text)
    print(news)
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("----------------------------------")
else:
    query=input("Enter the topic on which you want news: ")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey=293e896d927a435eae245b5084a92c52"
    r = requests.get(url)
    news = json.loads(r.text)
    print(news)
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("----------------------------------")

