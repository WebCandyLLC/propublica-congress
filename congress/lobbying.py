from .client import Client
from .utils import get_offset

class LobbyingClient(Client):


    def recent(self, **kwargs):
        """
        #1 GET RECENT LOBBYING REPRESENTATION FILINGS
        Gets the 20 most recent lobbying representation filings.
        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "lobbying/latest.json"
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def search(self, query, **kwargs):
        """
        #2 SEARCH LOBBYING REPRESENTATION FILINGS
        Gets the 20 most recent lobbying representation filings
        for a given search term. This response supports
        pagination using an offset querystring parameter with
        multiples of 20.
        """
        path = "lobbying/search.json?query={query}".format(
            query=query)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def get(self, filing):
        """
        #3 GET A SPECIFIC LOBBYING REPRESENTATION FILING
        Get a specific lobbying representation filing (filing is a
        numeric id attribute from search or latest responses)
        """
        path = "lobbying/{filing}.json".format(
            filing=filing)
        return self.fetch(path)
