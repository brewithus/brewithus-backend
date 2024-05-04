# getCafes.py
# getting cafes from yelp fusion api
import requests


APIKEY = "mE_E1oBj1H1Y55_JrqpkWf8Zsrr7HFTeQMTD7C9qcFRDAo3jB7dUG8AFv6lWu3u-wOCB_XYkTBysP_1JSptEBIbr53ozljyJkCWiLN2jqtfzvRbigdbRCLIdar4vZnYx"

# location info: to be retrieved from frontend
latitude = "34.0479604"
longitude = "-117.8108955"
# user search term: can give "" if there is none
userSearchTerm = "iced coffee"
# radius: in meters
radius = "12000"
# numCafes: set from 1 to 50
numCafes = "10"
# filtering out cafes that aren't open right now
openNow = False


url = "https://api.yelp.com/v3/businesses/search?latitude=" + latitude\
+ "&longitude=" + longitude

if len(userSearchTerm) > 0:
    url = url + "&term=" + userSearchTerm

url = url + "&radius=" + radius\
+ "&categories=coffee&locale=en_US"
# &categories=tea&categories=bubbletea

# including "&open_now=false" in the api call
# EXCLUDES cafes open right now
# so please leave this alone thanks
if openNow:
    url = url + "&open_now=true"

url = url + "&sort_by=best_match&limit=" + numCafes

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + APIKEY
}

response = requests.get(url, headers=headers)

print(response.text)