import json
from parse_rest.connection import register
from parse_rest.datatypes import Object
from pprint import pprint
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup

PARSE_APP_ID="7PdlFRkYtj5kmDaJNIQfGKHOVRCajQKVEfRBWB1e"
PARSE_CLIENT_KEY="0r1owyGri3p7uyo7UX5kivlkhJshtH169KWHGLqk"

register(PARSE_APP_ID, PARSE_CLIENT_KEY, master_key="8dHrxPljlhjB2QJuV0YGrY5tUh7MptdDYnJ3sg6a")

class Stock(Object):
	pass

def scrapeDaily():
	url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"

	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, "lxml")
	tbl = soup.find("table", {"class": "yfnc_datamodoutline1"}).findNext('table').find_all('tr')[1].find_all('td')
	
	stockDate = datetime.strptime(tbl[0].string, "%b %d, %Y")
	stockOpen = float(tbl[1].string)
	stockHigh = float(tbl[2].string)
	stockLow = float(tbl[3].string)
	stockClose = float(tbl[4].string)
	stockVol = int(tbl[5].string.replace(',', ''))
	
	stock = Stock(date = stockDate,
		high = stockHigh,
		low = stockLow,
		close = stockClose,
		open = stockOpen,
		volume = stockVol)

	try:
		stock.save()
		print("Save stock object ({})".format(stock.objectId))
	except:
		print("Stock data has already been saved.")

scrapeDaily()
