# Overview

<code>python-crmtext</code> is a Python client for the CRMText service.


# Getting Started

* Read the [CRMText API documentation](http://crmtext.com/api/docs).
* [Request an API Key](http://open.pbs.org/pbs-api-key-request/) from PBS
* Install Python dependencies: <code>pip install -r REQUIREMENTS.txt</code>


# Installation

Install <code>crmtext</code> to your Python path (hopefully in a [virtualenv](http://www.virtualenv.org/)!).

    pip install python-crmtext


# Usage

To do anything, you will first need a connection to the CRMText API:

    import crmtext
    conn = crmtext.connect(auth_string='YOUR-AUTH_STRING')

Or:

    conn = crmtext.connect(username='YOUR-USERNAME', password='YOUR-PASSWORD', keyword='YOUR-KEYWORD')
