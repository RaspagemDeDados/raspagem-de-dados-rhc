from bs4 import BeautifulSoup

helloworld = "<p>Hello World</p>"
soup_xml = BeautifulSoup(helloworld,features= "xml")

print(soup_xml)
