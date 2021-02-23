import requests, re
from bs4 import BeautifulSoup

query = input("Dork: ")
file_txt = open("result.txt", "a+")
page = requests.get(f"https://www.google.dz/search?q={query}")

def get_links(page):
	all_page_links = []
	soup = BeautifulSoup(page.content, "lxml")
	for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
		line = re.split(":(?=http)",link["href"].replace("/url?q=",""))
		all_page_links.append(line)
	return all_page_links




