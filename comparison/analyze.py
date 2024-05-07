import comparison.utility as utility

def compare_query_restaurant(query_string, restaurant_string):
    return utility.chat(
        f"""
            Return a json format object with one element called 'score' which is on the range [0, 100].
            This score should reflect how well the restaurant description {restaurant_string} matches query {query_string}
        """
    )

def get_score(query, restaurant, num=0):
    try:
        text = compare_query_restaurant(query, utility.restaurant_string_from_object(restaurant)).message.content
        print(text)
        return utility.find_score_in_json(text)
    except:
        if num >= -1: # allow once
            print(f'Failure in getting score')
            return 0
        else:
            return get_score(query, restaurant, num=num+1)        

def rank_restaurants(query, restaurants):
    # Sort the restaurants based on the score
    return sorted(restaurants, key=lambda r: get_score(query, r), reverse=True)

def get_score_obj(obj):
    return obj['score']
