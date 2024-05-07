import random
from utility import *
from flask import Flask, jsonify, request

def compare_query_restaurant(query_string, restaurant_string):
    return chat(
        f"""
            Return a json format object with one element called 'score' which is on the range [0, 100].
            This score should reflect how well the restaurant description {restaurant_string} matches query {query_string}
        """
    )

def get_score(query, restaurant, num=0):
    try:
        text = compare_query_restaurant(query, restaurant_string_from_object(restaurant)).message.content
        print(text)
        return find_score_in_json(text)
    except:
        if num >= -1: # allow once
            print(f'Failure in getting score')
            return 0
        else:
            return get_score(query, restaurant, num=num+1)        

def rank_restaurants(query, restaurants):
    # push element objects as such: 
    # {
    #   'id': ID,
    #   'name': NAME,
    #   'score': SCORE
    # }
    restaurant_ranks = []

    # get the scores

    for restaurant in restaurants:
        rank = {}
        rank['score'] = get_score(query, restaurant)
        rank['name'] = restaurant['name']
        rank['id'] = restaurant['id']
        restaurant_ranks.append(rank)

    # sort
    return sorted (restaurant_ranks, key=get_score_obj, reverse=True)

def get_score_obj(obj):
    return obj['score']

app = Flask(__name__)

@app.route('/api/business', methods=['GET'])
def get_restaurants():
    # Get parameters from query string
    query = request.args.get('q')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    # Rank businesses near lat lng based on query

    # get_cafes function
    cafes = get_cafes(lat, lng, query)

    # rank cafes
    ranked_cafes = rank_restaurants(query, cafes)

    # send jsonified ranked cafes
    # return whole business object
    return jsonify(ranked_cafes)


@app.route('/api/business/popular', methods=['GET'])
def get_restaurants():
    # Get parameters from query string
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    # Return most popular businesses

    # get_popular_afes function
    # return whole business object
    return jsonify(get_popular_cafes(lat, lng))

if __name__ == '__main__':
    app.run()