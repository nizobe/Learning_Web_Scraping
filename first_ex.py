from bs4 import BeautifulSoup #loading BeautifulSoup class
from urllib2 import urlopen #loading urlopen function

#useful beccause all links start with this and it saves space
BASE_URL = "http://www.chicagoreader.com"

#gets the links for the BOC, "best of category"
def get_categry_links(section_url):
  html = urlopen(section_url).read()#open the section_url into html
  soup = BeautifulSoup(html, "lxml")#instance of BeautifulSoup class. Initialized with html objecct and parsed with lxml
  boccat = soup.find("dl", "boccat")#in soup, find <dl> element with class "boccat"
  categry_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
  return categry_links