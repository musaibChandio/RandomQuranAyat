import os
from dotenv import load_dotenv
load_dotenv()

import requests
import random

BASE_URL = os.getenv("BASE_URL")

def get_random_ayah(edition):
    random_number = random.randint(1, 6236)
    url = f"{BASE_URL}/{random_number}/editions/quran-uthmani,{edition}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Error: API ne {response.status_code} bheja.")
            return None

        data = response.json()
        arabic = data["data"][0]
        translation = data["data"][1]
        return arabic, translation

    except requests.exceptions.Timeout:
        print("Error: API bahut slow hai.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Internet nahi chal raha ya API down hai.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

