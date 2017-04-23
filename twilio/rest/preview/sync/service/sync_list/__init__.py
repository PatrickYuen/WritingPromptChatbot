# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page
from twilio.rest.preview.sync.service.sync_list.sync_list_item import SyncListItemList


class SyncListList(ListResource):

    def __init__(self, version, service_sid):
        """
        Initialize the SyncListList
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        
        :returns: SyncListList
        :rtype: SyncListList
        """
        super(SyncListList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
        }
        self._uri = '/Services/{service_sid}/Lists'.format(**self._solution)

    def create(self, unique_name=values.unset):
        """
        Create a new SyncListInstance
        
        :param unicode unique_name: The unique_name
        
        :returns: Newly created SyncListInstance
        :rtype: SyncListInstance
        """
        data = values.of({
            'UniqueName': unique_name,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams SyncListInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncListInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of SyncListInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return SyncListPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SyncListContext
        
        :param sid: The sid
        
        :returns: SyncListContext
        :rtype: SyncListContext
        """
        return SyncListContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a SyncListContext
        
        :param sid: The sid
        
        :returns: SyncListContext
        :rtype: SyncListContext
        """
        return SyncListContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncListList>'


class SyncListPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SyncListPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        
        :returns: SyncListPage
        :rtype: SyncListPage
        """
        super(SyncListPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncListInstance
        
        :param dict payload: Payload response from the API
        
        :returns: SyncListInstance
        :rtype: SyncListInstance
        """
        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncListPage>'


class SyncListContext(InstanceContext):

    def __init__(self, version, service_sid, sid):
        """
        Initialize the SyncListContext
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid
        
        :returns: SyncListContext
        :rtype: SyncListContext
        """
        super(SyncListContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Lists/{sid}'.format(**self._solution)
        
        # Dependents
        self._sync_list_items = None

    def fetch(self):
        """
        Fetch a SyncListInstance
        
        :returns: Fetched SyncListInstance
        :rtype: SyncListInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the SyncListInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def sync_list_items(self):
        """
        Access the sync_list_items
        
        :returns: SyncListItemList
        :rtype: SyncListItemList
        """
        if self._sync_list_items is None:
            self._sync_list_items = SyncListItemList(
                self._version,
                service_sid=self._solution['service_sid'],
                list_sid=self._solution['sid'],
            )
        return self._sync_list_items

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncListContext {}>'.format(context)


class SyncListInstance(InstanceResource):

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the SyncListInstance
        
        :returns: SyncListInstance
        :rtype: SyncListInstance
        """
        super(SyncListInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'url': payload['url'],
            'links': payload['links'],
            'revision': payload['revision'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: SyncListContext for this SyncListInstance
        :rtype: SyncListContext
        """
        if self._context is None:
            self._context = SyncListContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique_name
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def revision(self):
        """
        :returns: The revision
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The created_by
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a SyncListInstance
        
        :returns: Fetched SyncListInstance
        :rtype: SyncListInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncListInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def sync_list_items(self):
        """
        Access the sync_list_items
        
        :returns: sync_list_items
        :rtype: sync_list_items
        """
        return self._proxy.sync_list_items

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncListInstance {}>'.format(context)
