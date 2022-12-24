from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as err:
		print(err)
	except URLError as err:
		print('no server found or URL mistyped')
	try:
		bs = BeautifulSoup(html.read(), 'lxml')
		title = bs.body.h1
	except AttributeError as err:
		print('tag not found')
	return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
	print('title not found')
else:
	print(title)