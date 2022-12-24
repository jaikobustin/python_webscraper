from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'html.parser')

#format '../img/gift/img3.jpg'
imgs = bs.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.\.jpg')})
for pic in imgs:
	print(pic['src'])

two = bs.findAll(lambda tag: len(tag.attrs) == 2)
for item in two:
	print('')
	print(item)