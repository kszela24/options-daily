import json
from parse_rest.connection import register
from parse_rest.datatypes import Object
from yahoo_finance import Share
from pprint import pprint
from datetime import datetime

PARSE_APP_ID="7PdlFRkYtj5kmDaJNIQfGKHOVRCajQKVEfRBWB1e"
PARSE_CLIENT_KEY="0r1owyGri3p7uyo7UX5kivlkhJshtH169KWHGLqk"

register(PARSE_APP_ID, PARSE_CLIENT_KEY, master_key="8dHrxPljlhjB2QJuV0YGrY5tUh7MptdDYnJ3sg6a")

aapl = Share('AAPL')

class Stock(Object):
	pass

historic = aapl.get_historical('2016-05-24', '2016-05-24')
print type(historic[0]['High'])

for i in reversed(historic):

	stockDate = datetime.strptime(i['Date'], "%Y-%m-%d")
	stockClose = float(i['Close'])
	stockHigh = float(i['High'])
	stockLow = float(i['Low'])
	stockOpen = float(i['Open'])
	stockVol = int(i['Volume'])

	stock = Stock(date = stockDate,
		high = stockHigh,
		low = stockLow,
		close = stockClose,
		open = stockOpen,
		volume = stockVol)

	
	stock.save()
	#print("Saved stock object ({})".format(stock.objectID))
	#except:
	#	print("Twit has already been saved.")