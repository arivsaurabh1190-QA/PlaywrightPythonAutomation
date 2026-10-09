import json
import os


BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.automationexercise.com"
)


def load_test_data():

    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "test_data",
        "test_data.json"
    )

    with open(file_path, "r") as file:
        return json.load(file)