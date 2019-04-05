"""
A Python client for the ProPublica Congress API

API docs: https://propublica.github.io/congress-api-docs/
"""
__author__ = "Chris Amico (eyeseast@gmail.com)"
__modified__ = "WebCandy, LLC (webcandyllc@gmail.com)"
__version__ = "0.3.0"

import os

from .client import Client
from .utils import CongressError, NotFound, check_chamber, get_congress, CURRENT_CONGRESS, check_category, check_chamber, check_comms, check_quarter, get_offset

# subclients
from .bills import BillsClient
from .members import MembersClient
from .committees import CommitteesClient
from .votes import VotesClient
from .nominations import NominationsClient

# New as of 4/4/2019
from .communications import CommunicationsClient
from .explanations import ExplanationsClient
from .flooractions import FloorActionsClient
from .lobbying import LobbyingClient
from .officeexpenses import OfficeExpensesClient
from .statements import StatementsClient


__all__ = ('Congress', 'CongressError', 'NotFound', 'get_congress', 'CURRENT_CONGRESS', 'check_category', 'check_chamber', 'check_comms', 'check_quarter', 'get_offset')


class Congress(Client):
    """
    Implements the public interface for the ProPublica Congress API

    Methods are namespaced by topic (though some have multiple access points).
    Everything returns decoded JSON, with fat trimmed.

    In addition, the top-level namespace is itself a client, which
    can be used to fetch generic resources, using the API URIs included
    in responses. This is here so you don't have to write separate
    functions that add on your API key and trim fat off responses.

    Create a new instance with your API key, or set an environment
    variable called ``PROPUBLICA_API_KEY``.

    Congress uses `httplib2 <https://github.com/httplib2/httplib2>`_, and caching is pluggable. By default,
    it uses `httplib2.FileCache <https://httplib2.readthedocs.io/en/latest/libhttplib2.html#httplib2.FileCache>`_,
    in a directory called ``.cache``, but it should also work with memcache
    or anything else that exposes the same interface as FileCache (per httplib2 docs).
    """

    def __init__(self, apikey=None, cache='.cache', http=None):
        if apikey is None:
            apikey = os.environ.get('PROPUBLICA_API_KEY')

        super(Congress, self).__init__(apikey, cache, http)

        self.bills = BillsClient(self.apikey, cache, self.http)
        self.committees = CommitteesClient(self.apikey, cache, self.http)
        self.members = MembersClient(self.apikey, cache, self.http)
        self.nominations = NominationsClient(self.apikey, cache, self.http)
        self.votes = VotesClient(self.apikey, cache, self.http)

        #New as of 4/4/2019
        self.communications = CommunicationsClient(self.apikey, cache, self.http)
        self.explanations = ExplanationsClient(self.apikey, cache, self.http)
        self.flooractions = FloorActionsClient(self.apikey, cache, self.http)
        self.lobbying = LobbyingClient(self.apikey, cache, self.http)
        self.officeexpenses = OfficeExpensesClient(self.apikey, cache, self.http)
        self.statements = StatementsClient(self.apikey, cache, self.http)
