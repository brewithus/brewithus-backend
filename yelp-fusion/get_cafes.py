# get_cafes.py
# getting cafes from yelp fusion api
import requests

APIKEY = "mE_E1oBj1H1Y55_JrqpkWf8Zsrr7HFTeQMTD7C9qcFRDAo3jB7dUG8AFv6lWu3u-wOCB_XYkTBysP_1JSptEBIbr53ozljyJkCWiLN2jqtfzvRbigdbRCLIdar4vZnYx"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + APIKEY
    }


# lat, long: numbers in strings
# userQuery: string (optional)
# isOpen: boolean
# RETURNS: array of businesses (json)

def get_cafes(lat, long, userQuery="", isOpen):
    url = "https://api.yelp.com/v3/businesses/search?latitude=" + latitude\
    + "&longitude=" + longitude\
    + "&term=" + userQuery\
    + "&radius=12000&categories=coffee&categories=tea&categories=bubbletea&locale=en_US"
    
    if openNow:
        url = url + "&open_now=true"
    
    url = url + "&sort_by=best_match&limit=10"
    
    return requests.get(url, headers=headers)


# business ID: string
# RETURNS: 3 excerpts

def get_reviews(business_id):
    
    url = "https://api.yelp.com/v3/businesses/" + business_id\
    + "/reviews?locale=en_US&limit=50&sort_by=yelp_sort"
    
    return requests.get(url, headers=headers)