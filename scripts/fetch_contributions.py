import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
from datetime import datetime



USERNAME = "NikhilShinde77"


URL = (
    f"https://github.com/users/"
    f"{USERNAME}/contributions"
)


OUTPUT = Path(
    "data/contributions.json"
)



def fetch():

    headers = {

        "User-Agent":
        "Mozilla/5.0"

    }


    response = requests.get(
        URL,
        headers=headers
    )


    if response.status_code != 200:

        raise Exception(
            "GitHub request failed"
        )


    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )


    days = []


    cells = soup.select(
        "td.ContributionCalendar-day"
    )


    for cell in cells:


        date = cell.get(
            "data-date"
        )


        level = cell.get(
            "data-level",
            "0"
        )


        days.append({

            "date": date,

            "level": int(level)

        })



    data = {

        "username": USERNAME,

        "updated":
        datetime.now().isoformat(),

        "total":
        len(days),

        "contributions":
        days

    }



    OUTPUT.parent.mkdir(
        exist_ok=True
    )


    OUTPUT.write_text(

        json.dumps(
            data,
            indent=2
        )

    )


    print(
        "✅ contributions.json created"
    )



if __name__ == "__main__":

    fetch()
    