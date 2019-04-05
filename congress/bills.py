from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber

    # Need to add offet querystring parameter check for account
    # for any offset with multiples of 20

class BillsClient(Client):

    def by_member(self, member_id, type='introduced'):
        """
        #3 GET RECENT BILLS BY A SPECIFIC MEMBER
        Takes a bioguide ID and a type:
        type (introduced|updated|cosponsored|withdrawn)
        Returns recent bills
        """
        path = "members/{member_id}/bills/{type}.json".format(
            member_id=member_id, type=type)
        return self.fetch(path)

    def subject(self, subject, type=None):
        if type:
            """
            #10 GET A SPECIFIC BILL SUBJECT
            Search for Bill subjects that contain a specified term.

            type: search
            query: a word or phrase (e.g. "health care") to search.
            """
            path = "bills/subjects/search.json?query={subject}".format(
            subject=subject)
            return self.fetch(path)
        else:
            """
            #4 GET RECENT BILLS BY A SPECIFIC SUBJECT
            Returns the 20 most recently updated bills for a
            specific legislative subject. Results can include
            more than one Congress.

            subject - a slug version of a legislative subject,
            displayed as url_name in subject responses.
            """
            path = "bills/subjects/{subject}.json".format(
            subject=subject)
            return self.fetch(path)

    def get(self, bill_id, congress=CURRENT_CONGRESS, type=None):
        if type:
            """
            congress (105-116)
            bill_id (a bill slug, for example hr4881, these can be 
            found in the recent bill response)
            OFFSET allowed by multiples of 20. offset query parameter

            #7 GET AMENDMENTS FOR A SPECIFIC BILL
            type: amendments
            Get Library of Congress-assigned subjects about a 
            particular bill. The request returns the 20 most recent results
            and supports paginated results.

            #8 GET SUBJECTS FOR A SPECIFIC BILL
            type: subjects
            Get Library of Congress-assigned subjects about a particular bill.
            The request returns the 20 most recent results and supports
            paginated requests.

            #9 GET RELATED BILLS FOR A SPECIFIC BILL
            type: related
            Get Library of Congress-identified related bills for a 
            particular bill The request returns the 20 most recent
            results and supports paginated requests.

            #11 GET COSPONSORS FOR A SPECIFIC BILL
            type: consponsors
            Get Information about the cosponsors of a particular bill.
            """
            path = "{congress}/bills/{bill_id}/{type}.json".format(
                congress=congress, bill_id=bill_id, type=type)
        else:
            """
            #6 GET A SPECIFIC BILL
            Get Details about a particular bill, including actions
            taken and votes. The attributes 'house_passage_vote' and 
            'senate_passage_vote' are populated (with the date of passage)
            only upon successful passage of the bill. Bills before the
            113th Congress (prior to 2013) have fewer attribute values
            than those from the 113th COngress onward.

            congress (105-116)
            bill_id (a bill slug, for example hr4881, these can be 
            found in the recent bill response)
            """
            path = "{congress}/bills/{bill_id}.json".format(
                congress=congress, bill_id=bill_id)

        return self.fetch(path)

    def amendments(self, bill_id, congress=CURRENT_CONGRESS):
        "#7"
        return self.get(bill_id, congress, 'amendments')

    def related(self, bill_id, congress=CURRENT_CONGRESS):
        "#9"
        return self.get(bill_id, congress, 'related')

    def subjects(self, bill_id, congress=CURRENT_CONGRESS):
        "#8"
        return self.get(bill_id, congress, 'subjects')

    def cosponsors(self, bill_id, congress=CURRENT_CONGRESS):
        "#11"
        return self.get(bill_id, congress, 'cosponsors')

    def recent(self, chamber, congress=CURRENT_CONGRESS, type='introduced'):
        """
        #2 GET RECENT BILLS
        Returns a list of recent bills. Recent means the last 
        20 bills of that Congress.
        
        chamber (house or senate or both)
        Congress (105-115)
        type: introduced | sorted by response field - introduced_date
              updated | sorted by latest_major_action_date
              active | sorted by latest_major_action_date
              passed | sorted by latest_major_action_date
              enacted | sorted by enacted
              vetoed | sorted by vetoed

        OFFSET allowed by multiples of 20. offset query parameter
        """
        check_chamber(chamber)
        path = "{congress}/{chamber}/bills/{type}.json".format(
            congress=congress, chamber=chamber, type=type)
        return self.fetch(path)

    def introduced(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting introduced bills"
        return self.recent(chamber, congress, 'introduced')

    def updated(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting updated bills"
        return self.recent(chamber, congress, 'updated')

    def active(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting active bills"
        return self.recent(chamber, congress, 'active')

    def passed(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting passed bills"
        return self.recent(chamber, congress, 'passed')

    def enacted(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting enacted bills"
        return self.recent(chamber, congress, 'enacted')

    def vetoed(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting vetoed bills"
        return self.recent(chamber, congress, 'vetoed')

    """ DOESNT APPEAR IN API DOCS AT THE MOMENT - 04042019
    def vetoed(self, chamber, congress=CURRENT_CONGRESS):
        "#2 Shortcut for getting major bills"
        return self.recent(chamber, congress, 'major')"""

    def upcoming(self, chamber, congress=CURRENT_CONGRESS):
        """
        #5 GET UPCOMING BILLS
        Get Details on Bills that may be considered by the House or Senate
        in the near future, based on scheduled published or announced
        by congressional leadership. The bills and their potential
        consideration are taken from the House Majority Leader
        and floor updates from Senate Republicans.

        The responses include a legislative_day attribute which is
        the earliest the bills could be considered, and a range attribute
        that indicates whether the bill information comes from a weekly
        schedule or a daily one. Combine the two for the best sense
        of when a bill might come up for consideration. For senate
        bills, the response includes a context attribute reproducing
        the sentence that includes mention of the bill These responses
        omit bills that have not yet been assigned a bill number or
        introduced, and additional bills may be considered at any time.

        chamber (house or senate)
        """
        check_chamber(chamber)
        path = "bills/upcoming/{chamber}.json".format(chamber=chamber)
        return self.fetch(path)

    # Need to add optional paramters of sort, dir
    def search(self, query):
        """
        #1 SEARCH BILLS
        Search the title and full text of legislation by keyword to get
        the 20 most recent bills. Searches cover House and Senate bills
        from the 113th Congress through the current Congress (116th).

        If multiple words are given, the search is treated as multiple
        keywords using the OR operator. Quoting words (e.q. "health care")
        makes it a phrase search. Search results can be sorted by
        date or by relevance, and in ascending or descending
        order.

        query - keyword or phrase
        sort - _score or date (default)
        dir - asc or desc (default)
        """
        path = "bills/search.json?query={query}".format(query=query)
        return self.fetch(path)