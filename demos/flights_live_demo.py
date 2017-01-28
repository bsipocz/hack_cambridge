#!/usr/bin/env python3

import requests

API_KEY = "ha393385273835879384162930498674"


def _poll_live_pricing(session_url):
    return requests.get("{}?apikey={}".format(session_url, API_KEY))


session_response = requests.post("http://business.skyscanner.net/apiservices/pricing/v1.0/?apikey=".format(API_KEY),
                                 data={'country': 'UK',
                                       'currency': 'GBP',
                                       'locale': 'en-GB',
                                       'locationSchema': 'iata',
                                       'apikey': API_KEY,
                                       'grouppricing': 'on',
                                       'originplace': 'EDI',
                                       'destinationplace': 'LHR',
                                       'outbounddate': '2016-12-17',
                                       'inbounddate': '2016-12-24'})

session_url = session_response.headers['Location']

print("Session URL from Skyscanner: {}".format(session_url))

pricing_response = _poll_live_pricing(session_url)
while pricing_response.status_code != 200:
    pricing_response = _poll_live_pricing(session_url)

print(pricing_response.json())
