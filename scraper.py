import requests
from bs4 import BeautifulSoup
import smtplib
import time
import config

URL = ""

headers = {"User-Agent": {config.user_agent}}


def check_headlines():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="").get_text()


def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login({config.email}, {config.password})

	subject = ""
	body = ""
	msg = f"Subject: {subject} \n\n {body}"

	server.sendmail(
			{config.email},
			{config.email},
			msg
		)
	server.quit()

while True:
	check_headlines()
	time.sleep(86400)