# getReviews.py
# getting cafe reviews from yelp fusion api
import requests


APIKEY = "mE_E1oBj1H1Y55_JrqpkWf8Zsrr7HFTeQMTD7C9qcFRDAo3jB7dUG8AFv6lWu3u-wOCB_XYkTBysP_1JSptEBIbr53ozljyJkCWiLN2jqtfzvRbigdbRCLIdar4vZnYx"

# business_id is required, retrieved from getCafes
business_id = "IKoK1Zu8wD50q88rFnRnKA"
# sortBy can be "yelp_sort" or "newest"
sortBy = "yelp_sort"
# numReviews: 1 to 50
numReviews = "4"

url = "https://api.yelp.com/v3/businesses/" + business_id\
+ "/reviews?locale=en_US&limit=" + numReviews + "&sort_by=" + sortBy

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + APIKEY
}

response = requests.get(url, headers=headers)

print(response.text)