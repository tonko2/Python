# -*- coding: utf-8 -*-
import ssl
from urllib import request
from bs4 import BeautifulSoup

def scraping():
    url = "https://www.yomiuri.co.jp/"

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    html = request.urlopen(url, context=context)

    soup = BeautifulSoup(html, "html.parser")

    titles = soup.find_all("h3")
    for title in titles:
        print(title.a.string)

if __name__ == "__main__":
    scraping()