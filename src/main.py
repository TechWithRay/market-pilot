from consts import client, logging
import json
from csv_parser import csv_parser
from google_api_call import get_place_info
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("--target", required=True, help="marketing target")
parser.add_argument("--county", required=True, help="location of your city")
parser.add_argument("--state", required=True, help="state")


# Use OpenAI to get the city in a county
def openai_call(query):
    """
    OpenAI call:
    args:
        query: county of a state.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "user", "content": "what are the cities in " + str({query}) + "in a format such as: [ 'a', 'b']"
            }
        ]
    )
    
    return response


if __name__ == "__main__":
    args = parser.parse_args()

    target = args.target
    county = args.county
    state = args.state

    response = openai_call(county)

    text = response.choices[0].message.content

    matches = re.findall(r'\[([^\]]*)\]', text)

    # Get the first match (assuming there's only one)
    if matches:
        content_inside_brackets = matches[0]

    # use regex to parse the city output
    cities = [item.strip("'") for item in content_inside_brackets.split(', ')]

    print(cities)


    all_info = {}

    for city in cities:
        place_info = get_place_info(target, city, county, state)

        all_info[f"{city}"] = place_info["places"]

    all_info = json.dumps(all_info)

    csv_parser(target, county, all_info)
        