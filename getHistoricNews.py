import json
from parse_rest.connection import register
from parse_rest.datatypes import Object
from yahoo_finance import Share
from pprint import pprint
from datetime import datetime
import quandl

PARSE_APP_ID="7PdlFRkYtj5kmDaJNIQfGKHOVRCajQKVEfRBWB1e"
PARSE_CLIENT_KEY="0r1owyGri3p7uyo7UX5kivlkhJshtH169KWHGLqk"

register(PARSE_APP_ID, PARSE_CLIENT_KEY, master_key="8dHrxPljlhjB2QJuV0YGrY5tUh7MptdDYnJ3sg6a")

class News(Object):
	pass

quandl.ApiConfig.api_key = "x3osWz9xu1WqjpWVaziX"

mydata = quandl.get("AOS/AAPL")

for i, row in enumerate(mydata.iterrows()):
	if i > 1098:
		newsDate = row[0].to_datetime()
		avgSent = float(row[1][0])
		impactScore = float(row[1][1])
		print avgSent
		print impactScore
		
		news = News(
			date = newsDate,
			avgSent = avgSent,
			impactScore = impactScore)

		news.save()
#print content