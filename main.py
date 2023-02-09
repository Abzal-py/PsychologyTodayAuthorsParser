from bs4 import BeautifulSoup
from get_data import get_data
import json


def get_articles_link(url):
    r = get_data(url)
    head = "https://www.psychologytoday.com/"
    articles_link = []

    soup = BeautifulSoup(r, "lxml")

    a_s = soup.findAll("a", rel = "bookmark")
    for a in a_s:
        href = a.get("href")
        articles_link.append(f"{head}{href}")

    return articles_link


def get_info(url):
    r = get_data(url=url)
    soup = BeautifulSoup(r, "lxml")
    img = soup.find("div",class_ = "profile-card__photo").find("img").get("src")
    name = soup.find("div", class_ = "h3 profile-card__profile-name").find("a").text
    title = soup.find("h1", class_ = "blog-entry__title--full").text.strip()

    dict_info = {
        "image_link" : img,
        "name": name,
        "tittle": title
    }
    return dict_info


def main():
    info = []
    total = int(input("How many pages to pars: "))
    for i in range(total):
        count = 1
        articles_link = get_articles_link(f"https://www.psychologytoday.com/us?page={i}")
        for article in articles_link:
            info_dict = get_info(article)
            info.append(info_dict)
            print(f"{i+1}.{count}")
            count+=1
        print(f"Articles left: {total-1-i}")


    with open("data/info.json","w") as file:
        json.dump(info, file, indent=4, ensure_ascii=False)




if __name__ == "__main__":
    main()
