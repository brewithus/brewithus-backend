import random
from utility import *

def compare_query_restaurant(query_string, restaurant_string):
    return chat(
        f"""
            Return a json format object with one element called 'score' which is on the range [0, 100].
            This score should reflect how well the restaurant description {restaurant_string} matches query {query_string}
        """
    )

def get_score(query, restaurant, num=0):
    if num > 3: return 0
    try:
        return parse_json_string(compare_query_restaurant(query, restaurant_string_from_object(restaurant)).message.content)['score']
    except:
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

if __name__ == '__main__':
    rests = get_restaurant_data() # restaurant_string_from_object to get string description

    user_input = ''
    while True:
        print('Enter your query, type "END" to end the loop')
        user_input = input()
        if user_input == 'END': break
        print('Query:', user_input)
        ranked = rank_restaurants(user_input, rests)
        for r in ranked:
            print(r['name'], ' - ', r['score'])


