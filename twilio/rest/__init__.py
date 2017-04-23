# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

import os
import platform
from twilio import __version__
from twilio.exceptions import TwilioException
from twilio.http.httplib2_client import Httplib2Client
from twilio.rest.api import Api
from twilio.rest.chat import Chat
from twilio.rest.ip_messaging import IpMessaging
from twilio.rest.lookups import Lookups
from twilio.rest.monitor import Monitor
from twilio.rest.notify import Notify
from twilio.rest.preview import Preview
from twilio.rest.pricing import Pricing
from twilio.rest.taskrouter import Taskrouter
from twilio.rest.trunking import Trunking


class Client(object):
    """ A client for accessing the Twilio API. """

    def __init__(self, username=None, password=None, account_sid=None,
                 http_client=None, environment=None):
        """
        Initializes the Twilio Client
        
        :param str username: Username to authenticate with
        :param str password: Password to authenticate with
        :param str account_sid: Account Sid, defaults to Username
        :param HttpClient http_client: HttpClient, defaults to Httplib2Client
        :param dict environment: Environment to look for auth details, defaults to os.environ
        
        :returns: Twilio Client
        :rtype: twilio.rest.Client
        """
        environment = environment or os.environ
        
        self.username = username or environment.get('TWILIO_ACCOUNT_SID')
        """ :type : str """
        self.password = password or environment.get('TWILIO_AUTH_TOKEN')
        """ :type : str """
        self.account_sid = account_sid or self.username
        """ :type : str """
        
        if not self.username or not self.password:
            raise TwilioException("Credentials are required to create a TwilioClient")
        
        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client = http_client or Httplib2Client()
        """ :type : HttpClient """
        
        # Domains
        self._api = None
        self._chat = None
        self._ip_messaging = None
        self._lookups = None
        self._monitor = None
        self._notify = None
        self._preview = None
        self._pricing = None
        self._taskrouter = None
        self._trunking = None

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
        """
        Makes a request to the Twilio API using the configured http client
        Authentication information is automatically added if none is provided
        
        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects
        
        :returns: Response from the Twilio API
        :rtype: twilio.http.response.Response
        """
        auth = auth or self.auth
        headers = headers or {}
        
        headers['User-Agent'] = 'twilio-python/{} (Python {})'.format(
            __version__,
            platform.python_version(),
        )
        headers['Accept-Charset'] = 'utf-8'
        
        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        
        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'
        
        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    @property
    def api(self):
        """
        Access the Api Twilio Domain
        
        :returns: Api Twilio Domain
        :rtype: Api
        """
        if self._api is None:
            self._api = Api(self)
        return self._api

    @property
    def chat(self):
        """
        Access the Chat Twilio Domain
        
        :returns: Chat Twilio Domain
        :rtype: Chat
        """
        if self._chat is None:
            self._chat = Chat(self)
        return self._chat

    @property
    def ip_messaging(self):
        """
        Access the IpMessaging Twilio Domain
        
        :returns: IpMessaging Twilio Domain
        :rtype: IpMessaging
        """
        if self._ip_messaging is None:
            self._ip_messaging = IpMessaging(self)
        return self._ip_messaging

    @property
    def lookups(self):
        """
        Access the Lookups Twilio Domain
        
        :returns: Lookups Twilio Domain
        :rtype: Lookups
        """
        if self._lookups is None:
            self._lookups = Lookups(self)
        return self._lookups

    @property
    def monitor(self):
        """
        Access the Monitor Twilio Domain
        
        :returns: Monitor Twilio Domain
        :rtype: Monitor
        """
        if self._monitor is None:
            self._monitor = Monitor(self)
        return self._monitor

    @property
    def notify(self):
        """
        Access the Notify Twilio Domain
        
        :returns: Notify Twilio Domain
        :rtype: Notify
        """
        if self._notify is None:
            self._notify = Notify(self)
        return self._notify

    @property
    def preview(self):
        """
        Access the Preview Twilio Domain
        
        :returns: Preview Twilio Domain
        :rtype: Preview
        """
        if self._preview is None:
            self._preview = Preview(self)
        return self._preview

    @property
    def pricing(self):
        """
        Access the Pricing Twilio Domain
        
        :returns: Pricing Twilio Domain
        :rtype: Pricing
        """
        if self._pricing is None:
            self._pricing = Pricing(self)
        return self._pricing

    @property
    def taskrouter(self):
        """
        Access the Taskrouter Twilio Domain
        
        :returns: Taskrouter Twilio Domain
        :rtype: Taskrouter
        """
        if self._taskrouter is None:
            self._taskrouter = Taskrouter(self)
        return self._taskrouter

    @property
    def trunking(self):
        """
        Access the Trunking Twilio Domain
        
        :returns: Trunking Twilio Domain
        :rtype: Trunking
        """
        if self._trunking is None:
            self._trunking = Trunking(self)
        return self._trunking

    @property
    def account(self):
        """
        :returns: Account provided as the authenticating account
        :rtype: AccountContext
        """
        return self.api.v2010.account

    @property
    def accounts(self):
        """
        :rtype: AccountList
        """
        return self.api.v2010.accounts

    @property
    def addresses(self):
        """
        :rtype: AddressList
        """
        return self.account.addresses

    @property
    def applications(self):
        """
        :rtype: ApplicationList
        """
        return self.account.applications

    @property
    def authorized_connect_apps(self):
        """
        :rtype: AuthorizedConnectAppList
        """
        return self.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        """
        :rtype: AvailablePhoneNumberCountryList
        """
        return self.account.available_phone_numbers

    @property
    def calls(self):
        """
        :rtype: CallList
        """
        return self.account.calls

    @property
    def conferences(self):
        """
        :rtype: ConferenceList
        """
        return self.account.conferences

    @property
    def connect_apps(self):
        """
        :rtype: ConnectAppList
        """
        return self.account.connect_apps

    @property
    def incoming_phone_numbers(self):
        """
        :rtype: IncomingPhoneNumberList
        """
        return self.account.incoming_phone_numbers

    @property
    def keys(self):
        """
        :rtype: KeyList
        """
        return self.account.keys

    @property
    def messages(self):
        """
        :rtype: MessageList
        """
        return self.account.messages

    @property
    def new_keys(self):
        """
        :rtype: NewKeyList
        """
        return self.account.new_keys

    @property
    def new_signing_keys(self):
        """
        :rtype: NewSigningKeyList
        """
        return self.account.new_signing_keys

    @property
    def notifications(self):
        """
        :rtype: NotificationList
        """
        return self.account.notifications

    @property
    def outgoing_caller_ids(self):
        """
        :rtype: OutgoingCallerIdList
        """
        return self.account.outgoing_caller_ids

    @property
    def queues(self):
        """
        :rtype: QueueList
        """
        return self.account.queues

    @property
    def recordings(self):
        """
        :rtype: RecordingList
        """
        return self.account.recordings

    @property
    def sandbox(self):
        """
        :rtype: SandboxList
        """
        return self.account.sandbox

    @property
    def signing_keys(self):
        """
        :rtype: SigningKeyList
        """
        return self.account.signing_keys

    @property
    def sip(self):
        """
        :rtype: SipList
        """
        return self.account.sip

    @property
    def short_codes(self):
        """
        :rtype: ShortCodeList
        """
        return self.account.short_codes

    @property
    def tokens(self):
        """
        :rtype: TokenList
        """
        return self.account.tokens

    @property
    def transcriptions(self):
        """
        :rtype: TranscriptionList
        """
        return self.account.transcriptions

    @property
    def usage(self):
        """
        :rtype: UsageList
        """
        return self.account.usage

    @property
    def validation_requests(self):
        """
        :rtype: ValidationRequestList
        """
        return self.account.validation_requests

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio {}>'.format(self.account_sid)
