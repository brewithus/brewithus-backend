import requests
from requests.exceptions import RequestException

class YelpFusionAPI:
    def __init__(self, api_key):
        self.APIKEY = api_key
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self.APIKEY
        }

    def get_cafes(self, lat, long, userQuery, categories=["coffee", "tea", "bubbletea"], openNow=False):
        try:
            url = f"https://api.yelp.com/v3/businesses/search?latitude={lat}&longitude={long}&term={userQuery}&radius=12000&locale=en_US"
            categories_str = ",".join(categories)
            url += f"&categories={categories_str}"

            if openNow:
                url += "&open_now=true"

            url += "&sort_by=best_match&limit=20"

            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()  # Will trigger an HTTPError if the HTTP request returned an unsuccessful status code
        except RequestException as e:
            # Log the error or handle it otherwise
            return {"error": str(e), "details": "Failed to fetch data from Yelp API"}


    def get_reviews(self, business_id):
        url = "https://api.yelp.com/v3/businesses/{}/reviews?locale=en_US&limit=50&sort_by=best_match".format(business_id)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_biz_details(self, business_id):
        """
        Retrieves detailed information for a specific business.

        Args:
            business_id (str): The ID or alias of the business.

        Returns:
            dict: A dictionary containing the business details.
        """
        url = f"https://api.yelp.com/v3/businesses/{business_id}"
        print('send new request')
        response = requests.get(url, headers=self.headers)
        return response.json()