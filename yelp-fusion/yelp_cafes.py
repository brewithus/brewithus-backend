# yelp_cafes.py
# cafes info and reviews from yelp fusion api

import requests

APIKEY = "mE_E1oBj1H1Y55_JrqpkWf8Zsrr7HFTeQMTD7C9qcFRDAo3jB7dUG8AFv6lWu3u-wOCB_XYkTBysP_1JSptEBIbr53ozljyJkCWiLN2jqtfzvRbigdbRCLIdar4vZnYx"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + APIKEY
    }


# ==== get_cafes ==============================================================
# Take parameters and return 10 cafes that fit the requirements.
#
# IN
# lat, long: latitude & longitude of location.             floats as strings
# (optional) userQuery: user's search term.                string
# (optional) isOpen: only get cafes open right now.        boolean
#
# OUT
# array of businesses OR error                             JSON
# See sample_cafes.json for sample output.
# See sample_yelp_error.json for sample error.
#
# NOTES
# Look for coffee, tea OR bubbletea.
# Search radius is set to 12000m (7.46 miles).
# Locale set to en_US only. (not intended for outside US)
# Sort by best match.
# Only up to 10 results will be given.
# Only return businesses with 1+ reviews.

def get_cafes(lat, long, userQuery="", isOpen=False):
    url = "https://api.yelp.com/v3/businesses/search?latitude=" + lat\
    + "&longitude=" + long\
    + "&term=" + userQuery\
    + "&radius=12000&categories=coffee&categories=tea&categories=bubbletea&locale=en_US"
    
    if isOpen:
        url = url + "&open_now=true"
    
    url = url + "&sort_by=best_match&limit=10"
    
    return requests.get(url, headers=headers)

# ==== get_reviews ============================================================
# Take a business ID and return 3 excerpts of reviews.
#
# IN
# business_id: business ID as given in yelp.               string
# 
# OUT
# 3 review excerpts OR error                               JSON
# See sample_reviews.json for sample output.
# See sample_yelp_error.json for sample error.
#
# NOTES
# Locale set to en_US only. (not intended for outside US)
# Reviews limit set to 50. (arbitrary because only returns 3 excerpts anyway)
# Sort by "yelp sort".

def get_reviews(business_id):
    url = "https://api.yelp.com/v3/businesses/" + business_id\
    + "/reviews?locale=en_US&limit=50&sort_by=yelp_sort"
    
    return requests.get(url, headers=headers)
# =============================================================================

# end of yelp_cafes.py