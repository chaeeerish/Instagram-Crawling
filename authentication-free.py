import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.instagram.com/p/C5pGcE4vZw7/?img_index=1")
html = res.text

soup = BeautifulSoup(html, "html.parser")
post_text = soup.select("title")

for p in post_text:
    print(p.text)