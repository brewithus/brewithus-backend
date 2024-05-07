import requests

class YelpFusionAPI:
    def __init__(self, api_key):
        self.APIKEY = api_key
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self.APIKEY
        }

    def get_cafes(self, lat, long, userQuery="", openNow=False):
        url = "https://api.yelp.com/v3/businesses/search?latitude={}&longitude={}&term={}&radius=12000&categories=coffee&categories=tea&categories=bubbletea&locale=en_US".format(lat, long, userQuery)

        if openNow:
            url += "&open_now=true"

        url += "&sort_by=best_match&limit=10"

        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_reviews(self, business_id):
        url = "https://api.yelp.com/v3/businesses/{}/reviews?locale=en_US&limit=50&sort_by=yelp_sort".format(business_id)
        response = requests.get(url, headers=self.headers)
        return response.json()