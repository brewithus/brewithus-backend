
from utility import chat, parse_json_string
from utility import save_variable_to_file
import random

REST_TEMPLATE = """
{
        "name": "PLACEHOLDER",
        "categories": [
            {
                "alias": "PLACEHOLDER",
                "title": "PLACEHOLDER"
            }
        ],
        "rating": "PLACEHOLDER",
        "reviews": [
            {
                "id": "PLACEHOLDER",
                "url": "PLACEHOLDER",
                "text": "PLACEHOLDER",
                "rating": "PLACEHOLDER",
                "time_created": "PLACEHOLDER"
            }
        ]
    }

"""

REV_TEMPLATE = """
    {
        "text": "PLACEHOLDER",
        "rating": "PLACEHOLDER",
        "time_created": "PLACEHOLDER"
    }
"""

def generate_testing(n=1):
    test_cases = []
    for i in range(n):
        prompt = f"Return only this JSON template filled with realistic restaurant data: {REST_TEMPLATE}"

        r = chat(prompt, token_limit=500).message.content
        case = parse_json_string(r)
        print('|', end='')

        num_reviews = random.randint(10, 25)
        for k in range(num_reviews):
            prompt = f"Return only this JSON template with a review for a restaurant described with the JSON object {r}: {REV_TEMPLATE}"
            r = chat(prompt, token_limit=500).message.content
            rev = parse_json_string(r)
            case['reviews'].append(rev)
            print('=', end='')
        print(" -", case['name'])
        test_cases.append(case)
    save_variable_to_file(test_cases)
    return test_cases


if __name__ == "__main__":
    generate_testing()



