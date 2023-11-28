import json
import csv
from consts import logging
import argparse
import pandas as pd


logging.info("Save data into csv file")

parser = argparse.ArgumentParser()

parser.add_argument("--placeData", required=True, help="Ouput of google API info")


def csv_parser(target, county, placeData):

    """
    Save data into csv file
    """

    placeData = json.loads(placeData)

    # create dfs
    dfs = []

    cityName = [city for city in placeData]

    # Write data
    for city, target_info in placeData.items():

        # if no website information, then filter out

        display_name = []
        phone = []
        address = []
        website = []
        email = []
        notes = []


        for place in target_info:

            if place.get("websiteUri", "") == "":
                continue

            if place.get("internationalPhoneNumber", "") == "":
                continue

            if place.get("formattedAddress", "") == "" or city not in place["formattedAddress"]:
                continue

            display_name.append(place["displayName"]["text"])
            phone.append(place["internationalPhoneNumber"][3:])
            address.append(place["formattedAddress"])
            website.append(place["websiteUri"])
            email.append("")  # No email information provided
            notes.append("")  # Empty notes field

        # Create a DataFrame for each place
        df = pd.DataFrame({
            "Name": display_name,
            "Phone": phone,
            "Address": address,
            "Website": website,
            "Email": email,
            "Notes": notes,
            "1st Contact": [""] * len(notes),
            "2nd Contact": [""] * len(notes)
        })

        dfs.append(df)

    with pd.ExcelWriter(f"{target}-{county}.xlsx") as writer:
        for i, df in enumerate(dfs):
            logging.info(f"save target of {cityName[i]}")
            df.to_excel(writer, sheet_name=f'{cityName[i]}', index=False)
