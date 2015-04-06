from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def get_categry_links(section_url):
  html = urlopen(section_url).read()
  soup = BeautifulSoup(html, "lxml")
  boccat = soup.find("dl", "boccat")
  categry_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
  return categry_links