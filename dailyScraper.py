import json
from parse_rest.connection import register
from parse_rest.datatypes import Object
from pprint import pprint
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup
import quandl

PARSE_APP_ID="7PdlFRkYtj5kmDaJNIQfGKHOVRCajQKVEfRBWB1e"
PARSE_CLIENT_KEY="0r1owyGri3p7uyo7UX5kivlkhJshtH169KWHGLqk"

register(PARSE_APP_ID, PARSE_CLIENT_KEY, master_key="8dHrxPljlhjB2QJuV0YGrY5tUh7MptdDYnJ3sg6a")

quandl.ApiConfig.api_key = "x3osWz9xu1WqjpWVaziX"

mydata = quandl.get("VOL/AAPL")

class Stock(Object):
	pass

class Option(Object):
	pass

class News(Object):
	pass

currDate = datetime.now()

def scrapeDailyStock():
	url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"

	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, "lxml")
	tbl = soup.find("table", {"class": "yfnc_datamodoutline1"}).findNext('table').find_all('tr')[1].find_all('td')
	
	stockDate = datetime.strptime(tbl[0].string, "%b %d, %Y")
	currDate = datetime.strptime(tbl[0].string, "%b %d, %Y")
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

scrapeDailyStock()

quandl.ApiConfig.api_key = "x3osWz9xu1WqjpWVaziX"

def scrapeDailyOptions():
	url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"

	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, "lxml")
	tbl = soup.find("table", {"class": "yfnc_datamodoutline1"}).findNext('table').find_all('tr')[1].find_all('td')
	
	optionDate = datetime.strptime(tbl[0].string, "%b %d, %Y")

	mydata = quandl.get("VOL/AAPL")

	row = mydata.iloc[-1:]
	ivmean10 = float(row['IvMean10'])
	ivmean20 = float(row['IvMean20'])
	ivmean30 = float(row['IvMean30'])
	ivmean60 = float(row['IvMean60'])


	option = Option(
		date = optionDate,
		ivMean10 = ivmean10,
		ivMean20 = ivmean10,
		ivMean30 = ivmean30,
		ivMean60 = ivmean60)

	try:
		option.save()
		print("Save option object ({})".format(option.objectId))
	except:
		print("Option data has already been saved.")

scrapeDailyOptions()



def scrapeDailyNews():
	url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"

	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, "lxml")
	tbl = soup.find("table", {"class": "yfnc_datamodoutline1"}).findNext('table').find_all('tr')[1].find_all('td')
	
	newsDate = datetime.strptime(tbl[0].string, "%b %d, %Y")

	mydata = quandl.get("AOS/AAPL")

	row = mydata.iloc[-1:]
	avgSent = float(row['Article Sentiment'])
	impactScore = float(row['Impact Score'])

	news = News(
		date = newsDate,
		avgSent = avgSent,
		impactScore = impactScore)

	try:
		news.save()
		print("Saved news object ({})".format(news.objectId))
	except:
		print("News data has already been saved.")

scrapeDailyNews()






