"""Module: `crmtext.connection`
Connection classes for accessing CRMText API.
"""
from crmtext import API_ENDPOINT
from crmtext.utils import get_auth_string, request


class Connection(object):
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
    `crmtext.connection.Connection` object
    """
    def __init__(self, auth_string=None, username=None, password=None,
                 keyword=None, endpoint=API_ENDPOINT):
        self.auth_string = auth_string
        self.endpoint = endpoint
        if not self.auth_string:
            if username and password and keyword:
                self.auth_string = get_auth_string(username, password, keyword)
        if not self.auth_string:
            raise 'Missing authentication credentials.'

    def opt_in_customer(self, firstname, lastname, phone_number):
        """Opt-in a customer.

        Keyword arguments:
        `firstname`
        `lastname`
        `phone_number`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'optincustomer',
            'firstname': firstname,
            'lastname': lastname,
            'phone_number': phone_number,
        }
        return self._request(data)

    def opt_out_customer(self, phone_number):
        """Opt-out a customer.

        Keyword arguments:
        `phone_number`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'optoutcustomer',
            'phone_number': phone_number,
        }
        return self._request(data)

    def get_callback(self):
        """Get the callback.

        Returns:
        `Element` instance
        """
        data = {
            'method': 'getcallback',
        }
        return self._request(data)

    def set_callback(self, callback):
        """Set the callback.

        Keyword arguments:
        `callback`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'setcallback',
            'callback': callback,
        }
        return self._request(data)

    def send_sms_msg(self, phone_number, message=None, mmsurl=None):
        """Send a SMS messsage

        Keyword arguments:
        `phone_number`
        `message` -- optional
        `mmsurl` -- optional

        Returns:
        `Element` instance
        """
        data = {
            'method': 'sendsmsmsg',
            'phone_number': phone_number,
        }
        if message:
            data['message'] = message
        if message:
            data['mmsurl'] = mmsurl
        return self._request(data)

    def send_campaign(self, name, message):
        """Send a campaign message.

        Keyword arguments:
        `name`
        `message`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'sendcampaign',
            'name': name,
            'message': message,
        }
        return self._request(data)

    def is_keyword_available(self, keyword):
        """Check if keyword is available.

        Keyword arguments:
        `keyword`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'iskeywordavailable',
            'keyword': keyword,
        }
        return self._request(data)

    def create_store_and_user(self, storename, storekeyword, firstname,
                              lastname, emailid, phonenumber, password):
        """Create a new store and user.

        Keyword arguments:
        `storename`
        `storekeyword`
        `firstname`
        `lastname`
        `emailid`
        `phonenumber`
        `password`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'createstoreanduser',
            'storename': storename,
            'storeKeyword': storekeyword,
            'firstname': firstname,
            'lastname': lastname,
            'emailid': emailid,
            'phonenumber': phonenumber,
            'password': password,
        }
        return self._request(data)

    def create_keyword(self, keyword, autoresponder):
        """Create a new keyword.

        Keyword arguments:
        `keyword`
        `autoresponder`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'createkeyword',
            'keyword': keyword,
            'autoresponder': autoresponder,
        }
        return self._request(data)

    def change_store_textcode_msg(self, textcode, optinmsg, nonoptinmsg):
        """Change store textcode message.

        Keyword arguments:
        `textcode`
        `optinmsg`
        `nonoptinmsg`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'changestoretextcodemsg',
            'textcode': textcode,
            'optinmsg': optinmsg,
            'nonoptinmsg': nonoptinmsg,
        }
        return self._request(data)

    def delete_keyword(self, keyword, autoresponder):
        """Delete a keyword.

        Keyword arguments:
        `keyword`
        `autoresponder`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'deletekeyword',
            'keyword': keyword,
            'autoresponder': autoresponder,
        }
        return self._request(data)

    def get_cust_by_status(self, status, offset, count):
        """Get customers by status.

        Keyword arguments:
        `status`
        `offset`
        `count`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'getcustbystatus',
            'status': status,
            'offset': offset,
            'count': count,
        }
        return self._request(data)

    def get_customer_info(self, phone_number):
        """Get customer info.

        Keyword arguments:
        `phone_number`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'getcustomerinfo',
            'phone_number': phone_number,
        }
        return self._request(data)


    def get_cust_msgs_by_mobile(self, phone_number, startdate, enddate,
                                startcount, msgcount):
        """Get customer messages by date range.

        Keyword arguments:
        `phone_number`
        `startdate`
        `enddate`
        `startcount`
        `msgcount`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'getcustmsgsbymobile',
            'phone_number': phone_number,
            'startdate': startdate.isoformat(),
            'enddate': enddate.isoformat(),
            'startcount': startcount,
            'msgcount': msgcount,
        }
        return self._request(data)

    def get_inbound_msgs(self, startdate, enddate):
        """Get inbound messages by date range.

        Keyword arguments:
        `startdate`
        `enddate`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'getinboundmsgs',
            'startdate': startdate.isoformat(),
            'enddate': enddate.isoformat(),
        }
        return self._request(data)

    def get_outbound_msgs(self, startdate, enddate):
        """Get outbound messages by date range.

        Keyword arguments:
        `startdate`
        `enddate`

        Returns:
        `Element` instance
        """
        data = {
            'method': 'getoutboundmsgs',
            'startdate': startdate.isoformat(),
            'enddate': enddate.isoformat(),
        }
        return self._request(data)

    def _request(self, data):
        return request(self, data)
