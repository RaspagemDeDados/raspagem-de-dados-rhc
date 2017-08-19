import urllib2
from bs4 import BeautifulSoup

url = "http://www.packtpub.com/books"
page = urllib2.urlopen(url)
soup_packtpage = BeautifulSoup(page)


print(soup_packtpage)