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
atag = soup.a

first_a_string = atag.string

print(first_a_string)