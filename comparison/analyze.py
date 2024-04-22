from utility import *

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
    results = []

    # convert to string for prompt
    for i in range(len(rests)):
        rests[i] = restaurant_string_from_object(rests[i])

    for i in range(len(queries)):
        print('_'*50)
        line = []
        for k in range(len(rests)):
            c = compare_query_restaurant(queries[i], rests[k]).message.content
            score = parse_json_string(c)['score']
            print(score, end=' \t')
            line.append(score)
        results.append(line)
        print()

    save_variable_to_file(results)



            

    








