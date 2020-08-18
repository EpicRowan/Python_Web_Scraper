import requests
from bs4 import BeautifulSoup

URL = ""

headers = {"User-Agent": Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/
			537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="").get_text()
