import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from comparison.analyze import rank_restaurants
from yelpfusion.yelp_client import YelpFusionAPI
from flask_caching import Cache
from flask_cors import CORS

load_dotenv()

api_key = os.getenv("YELP_API_KEY")
yelp_api = YelpFusionAPI(api_key)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://brewith.us"]}})

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/business', methods=['GET'])
# @cache.cached(timeout=3600)  # Cache for 1 hour (3600 seconds)
def get_restaurants():
    # Get parameters from query string
    query = request.args.get('q')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    categories = request.args.get('categories')
    open_now = request.args.get('open_now', 'false').lower() == 'true'  # Default to False if not specified

    # Check if required parameters are present
    if not query or not lat or not lng:
        return jsonify({'error': 'Missing required parameters'}), 400

    # Split categories if provided, else default to coffee, tea, and bubbletea
    category_list = categories.split(',') if categories else ["coffee", "tea", "bubbletea"]

    # Rank businesses near lat lng based on query
    # get_cafes function
    biz_response = yelp_api.get_cafes(lat, lng, query, category_list, open_now)

    if 'error' in biz_response:
        return jsonify({
            'error': 'Failed to fetch data from Yelp',
            'message': biz_response['error']
        }), 500
    return jsonify({
        "businesses": biz_response['businesses']
    })

    # rank cafes need further testing
    try:
        ranked_cafes = rank_restaurants(query, biz_response['businesses'])
        return jsonify({
            "businesses": ranked_cafes
        })
    except:
        print('error, fall back')
        # send jsonified ranked cafes
        # return whole business object
        return jsonify({
            "businesses": biz_response['businesses']
        })

@app.route('/business/<string:business_id>', methods=['GET'])
@cache.cached(timeout=3600)  # Cache for 1 hour (3600 seconds)
def get_business_details(business_id):
    try:
        # Get business details from Yelp API
        business_details = yelp_api.get_biz_details(business_id)
        return jsonify(business_details)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# @app.route('/api/business/popular', methods=['GET'])
# def get_restaurants():
#     # Get parameters from query string
#     lat = request.args.get('lat')
#     lng = request.args.get('lng')
#     # Return most popular businesses

#     # get_popular_afes function
#     # return whole business object
#     return jsonify(get_popular_cafes(lat, lng))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050,debug=True)