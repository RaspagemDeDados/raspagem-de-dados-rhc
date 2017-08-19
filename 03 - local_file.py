from bs4 import BeautifulSoup

with open("exemplo.html","r") as arquivo_exemplo:
	soup = BeautifulSoup(arquivo_exemplo)

print soup
arquivo_exemplo.close()

#soup = BeautifulSoup("exemplo.html")
#print(soup)

#soup_url = BeautifulSoup("http://www.packtpub.com/books")
#print(soup_url)