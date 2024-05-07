# Backend - Yelp Fusion API Calls


## `yelp_cafes.py`

All the functions that call Yelp Fusion API.
Here are all function headers for quick reference:

- `def get_cafes(lat, long, userQuery="", isOpen=False)`
- `def get_reviews(business_id)`

More detailed information can be found in the file.

## `sample_cafes.json`

JSON of sample 20 cafes from a `get_cafes` call.\
Note that it is a JSON of array of `"businesses"`.\
Equivalent call: `get_cafes("34.0479604", "-117.8108955", "fast", False)`

## `sample_reviews.json`

JSON of sample 3 excerpts from a `get_reviews` call.\
Business ID used is first business in `sample_cafes.json`.\
Equivalent call: `get_reviews(K-3eiVb-dAkC3ujgnT4QSQ)`

## `sample_yelp_error.json`

A sample error as JSON returned by Yelp instead of intended output.\
This specific error is response 400, bad/invalid request.

Possible responses from Yelp:
- 200 (Successful; proper output should have been returned)
- 400 ("INVALID_REQUEST"; bad request)
- 401 ("UNAUTHORIZED_API_KEY"; expired/unauthorized key or "TOKEN_INVALID"; invalid key)
- 403 ("AUTHORIZATION_ERROR"; key currently can't query the endpoint)
- 404 ("NOT_FOUND"; resource not found)
- 413 ("PAYLOAD_TOO_LARGE"; length of request exceeded maximum allowed)
- 429 ("TOO_MANY_REQUESTS_PER_SECOND"; exceeded daily quota (500) or queries-per-second limit)
- 500 ("INTERNAL_ERROR"; internal server error)
- 503 ("SERVICE_UNAVAILABLE"; service unavailable)