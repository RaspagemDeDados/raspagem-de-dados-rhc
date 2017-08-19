# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html_atag = """
<html>
<body>
	<p>Test html a tag example</p>
	<a href='http://www.packtpub.com'>Home</a>
	<a href='http;//www.packtpub.com/books'>Books</a>
</body>
</html>
"""

soup = BeautifulSoup(html_atag,'lxml')

#Imprime A Primeira Ocorrência da Tag a
atag = soup.a
print(atag)

#Imprime A Primeira Ocorrência da Tag p
ptag = soup.p
print(ptag)

#Imprime o tipo da tag
#print(type(atag))

#Imprime o nome da tag
tagname = atag.name
#print(tagname)

#Imprime atributos da tag
#print (atag['href'] )
#print(atag.attrs)