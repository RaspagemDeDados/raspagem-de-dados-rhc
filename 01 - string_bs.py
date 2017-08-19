from bs4 import BeautifulSoup

helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld)

print(soup_string)