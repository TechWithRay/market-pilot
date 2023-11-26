from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
)

load_dotenv()

# configure the openai authorizaiton
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

GOOGLE_DISPLAY_CONTENT="places.id,places.displayName,places.formattedAddress,places.internationalPhoneNumber,places.websiteUri,places.subDestinations"