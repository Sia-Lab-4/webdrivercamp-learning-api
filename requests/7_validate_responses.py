import json
import requests
from pprint import pprint
def find_mismatched_data(url, file_name):
    with open(file_name, "r") as file:
        expected_data = json.load(file)["results"]

    response = requests.get(url)
    response_data = response.json()["results"]

    mismatches = {}

    for exp_planet, act_planet in zip(expected_data, response_data):
        planet_name = exp_planet["name"]
        planet_mismatches = []

        for key in exp_planet:
            if key in act_planet:
                expected_value = exp_planet[key]
                actual_value = act_planet[key]

                if expected_value != actual_value:
                    planet_mismatches.append({
                        key: {'Expected': expected_value, 'Actual': actual_value}
                        })

        if planet_mismatches:
            mismatches[planet_name] = planet_mismatches

    return mismatches


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"
    pprint(find_mismatched_data(url, file_name))















