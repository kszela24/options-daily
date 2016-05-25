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

class Option(Object):
	pass

quandl.ApiConfig.api_key = "x3osWz9xu1WqjpWVaziX"

mydata = quandl.get("VOL/AAPL")

for i, row in enumerate(mydata.iterrows()):
	if i > 3270:
		optionDate = row[0].to_datetime()
		ivmean10 = float(row[1][18])
		ivmean20 = float(row[1][22])
		ivmean30 = float(row[1][26])
		ivmean60 = float(row[1][30])
		print optionDate
		print ivmean10
		print ivmean20
		print ivmean30
		print ivmean60
		
		option = Option(
			date = optionDate,
			ivMean10 = ivmean10,
			ivMean20 = ivmean10,
			ivMean30 = ivmean30,
			ivMean60 = ivmean60)

		option.save()

print type(mydata)
print list(mydata.columns.values)
print len(mydata)

