"""Module: `crmtext.utils`
Utility methods.
"""
import base64

import requests
import untangle


def get_auth_string(username, password, keyword):
    """Creates an auth string from credentials."""
    return base64.b64encode('%s:%s:%s' % (username, password, keyword.upper()))


def request(conn, data):
    """Makes API request and returns a parsed reponse."""
    headers = {'Authorization': 'Basic %s' % conn.auth_string}
    r = requests.post(conn.endpoint, data=data, headers=headers)
    return parse_response(r.content)


def parse_response(raw_response):
    """Parses API response."""
    untangled = untangle.parse(raw_response).response
    return untangled
