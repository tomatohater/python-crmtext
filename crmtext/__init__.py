"""Package: `crmtext`
A Python client for the CRMText API.
"""

# client version
__version__ = '0.1dev'

# api constants
API_ENDPOINT = 'https://restapi.crmtext.com/smapi/rest'


def connect(auth_string=None, username=None, password=None, keyword=None,
            endpoint=API_ENDPOINT):
    """Connect to the CRMText API.

    Valid credentials must be provided in the form of either `username`,
    `password` and `keyword`, or a valid `auth_string`.

    Keyword arguments:
    `auth_string` -- Your auth string
    `username` -- Username of your primary CRMText account
    `password` -- Password of your primary CRMText account
    `keyword` -- Keyword of your CRMText store
    `endpoint` -- endpoint of CRMText API (default: API_ENDPOINT)

    Returns:
    `crmtext.connection.Connection` instance
    """
    from crmtext.connection import Connection
    return Connection(auth_string, username, password, keyword, endpoint)
