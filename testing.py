import json
import os, sys
import calendar
import time
import urllib2
from datetime import datetime
from parse_rest.connection import register
from parse_rest.datatypes import Object
from pprint import pprint
lib_path = os.path.abspath(os.path.join('alchemyapi_python'))
sys.path.append(lib_path)
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

PARSE_APP_ID="7PdlFRkYtj5kmDaJNIQfGKHOVRCajQKVEfRBWB1e"
PARSE_CLIENT_KEY="0r1owyGri3p7uyo7UX5kivlkhJshtH169KWHGLqk"

register(PARSE_APP_ID, PARSE_CLIENT_KEY, master_key="8dHrxPljlhjB2QJuV0YGrY5tUh7MptdDYnJ3sg6a")

apikey = "d0eaa84bd893b3cf74fc3b9f421d68c565b3eece"

url = "https://access.alchemyapi.com/calls/data/GetNews?apikey=" + apikey + "&return=enriched.url.title,enriched.url.publicationDate,enriched.url.enrichedTitle.docSentiment&start=1463990400&end=1464145200&q.enriched.url.enrichedTitle.entities.entity=|text=AAPL,type=company|&count=25&outputMode=json"

timetest = "20160525T000000"

newsDate = datetime.strptime(timetest, "%Y%m%dT000000")

print newsDate