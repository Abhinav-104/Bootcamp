import requests
import bs4

def get_links():
	resp = requests.get("https://www.metrolyrics.com/grateful-dead-lyrics.html")
	soup = bs4.BeautifulSoup(resp.content, features="html.parser")
	links = soup.find_all("a",{"class":"title"})
	for i in links:
		print(i['href'])
get_links()
