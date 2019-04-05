from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber, get_offset


class StatementsClient(Client):


    def recent(self, **kwargs):
        """
        #1 GET RECENT CONGRESSIONAL STATEMENTS
        Gets a list of recent statements published on
        congressional websites.

        This response supports
        pagination using an offset querystring parameter with
        multiples of 20.
        """
        path = "statements/latest.json"
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def date(self, date, **kwargs):
        """
        #2 GET CONGRESSIONAL STATEMENTS BY DATE
        Takes a date (YYYY-MM-DD) and gets a list of statements
        published on congressional websites on a particular date.

        This response supports
        pagination using an offset querystring parameter with
        multiples of 20.
        """
        path = "statements/date/{date}.json".format(
            date=date)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def search(self, query, **kwargs):
        """
        #3 GET CONGRESSIONAL STATEMENTS BY SEARCH TERM
        Gets a list of statements published on congressional
        websites using a search term.

        This response supports
        pagination using an offset querystring parameter with
        multiples of 20.
        """
        path = "statements/search.json?query={query}".format(
            query=query)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def subjects(self):
        """
        #4 GET STATEMENT SUBJECTS
        Gets a list of subjects used to categorize congressional
        statements. Request returns all of the subjects that have
        been used at least once.
        """
        path = "statements/subjects.json"
        return self.fetch(path)

    # need to define a function in util to validate member id

    def subject(self, subject, **kwargs):
        """
        #5 GET CONGRESSIONAL STATEMENTS BY SUBJECT
        Uses a slug verions of subject and returns a list of
        statements published on congressional websites for 
        a particular subject.

        ASIDE: The subjects are not automatically assigned
        but are manually curated by ProPublica, although they
        are based on legislative subjects produced by the Library
        of Congress. Advised to use the statement search response
        for a more complete listing of statements about a keyword
        or phrase.

        This response supports
        pagination using an offset querystring parameter with
        multiples of 20.
        """
        path = "statements/subject/{subject}.json".format(
            subject=subject)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    # need to define a function in util to validate member id

    def member(self, member, congress=CURRENT_CONGRESS, **kwargs):
        """
        #6 GET CONGRESSIONAL STATEMENTS BY MEMBER
        Takes the available congress number (113-116) and the member
        id (assigned by the Biographical Directory of the United
        States Congress or can be retrieved from a members list request.

        This request returns the 20 most recent results and supports
        pagination using multiples of 20.
        """
        path = "members/{member}/statements/{congress}.json".format(
            member=member, congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    # need to define a function in util to validate bill id

    def bill(self, bill, congress=CURRENT_CONGRESS, **kwargs):
        """
        #7 GET CONGRESSIONAL STATEMENTS BY BILL
        Takes the available congress number (113-116) and the 
        bill slug, for example s19 - these can be found in bill responses
        and returns the lists of statements that mention a specific bill
        within a Congress.

        This request returns the 20 most recent results and supports
        pagination using multiples of 20.
        """
        path = "{congress}/bills/{bill}/statements.json".format(
            bill=bill, congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

