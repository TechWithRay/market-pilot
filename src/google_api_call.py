from datetime import datetime
from consts import logging, GOOGLE_API_KEY, GOOGLE_DISPLAY_CONTENT
import requests
import json


def get_place_info(target, city, county, state):
    """
    cURL the google placeAPI
    arg:
        searchText: "senior home in napa, california"

    """

    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": GOOGLE_API_KEY,
    "X-Goog-FieldMask": GOOGLE_DISPLAY_CONTENT,
    }

    data = {
    "textQuery": f"{target} in {city} {county} {state}"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        place_info = response.json()
    except Exception:
        logging.info("Houston, we got a problem!")

    return place_info