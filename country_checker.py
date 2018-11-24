import json

import requests


class CountryChecker:

    def __init__(self):
        print("Created object")

    def check_if_in_poland(self, lattitude, longittiude):
        address = "https://nominatim.openstreetmap.org/reverse?format=json"
        concat = "&"
        lat = "lat=" + str(lattitude)
        long = "lon=" + str(longittiude)

        address = address + concat + lat + concat + long
        response = requests.get(address)

        response_json = json.loads(response.content)

        return response_json['address']['country_code'] == 'pl'

