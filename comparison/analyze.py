from utility import *

def restaurant_string_from_object(restaurant):
    name = restaurant["name"]
    categories = ""
    rating = restaurant["rating"]
    reviews = ""

    for cat in restaurant["categories"]:
        title = cat["title"]
        categories = f"'{title}', {categories}"

    for review in restaurant["reviews"]:
        text = review["text"]
        stars = review["rating"]
        reviews = f"'{text}: rated {stars}', {reviews}"

    return f"a restaurant called {name};with the following categories: {categories};a rating of {rating};with the following user reviews: {reviews}."

def compare_query_restaurant(q, r):
    return chat(
        f"""
            Return a json format object with one element called 'score' which is on the range [0, 100].
            This score should reflect how well the restaurant description {r} matches query {q}
        """
    )

if __name__ == '__main__':
    queries = get_queries()
    rests = get_restaurant_data()

    # convert to string for prompt
    for i in range(len(rests)):
        rests[i] = restaurant_string_from_object(rests[i])

    for i in range(len(queries)):
        print('_'*50)
        for k in range(len(rests)):
            print('"' + compare_query_restaurant(queries[i], rests[k]).message.content + '"')



            

    








