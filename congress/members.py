from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber


class MembersClient(Client):

    
    def get(self, member_id):
        """
        #2 GET A SPECIFIC MEMBER
        Takes a bioguide_id, returns a legislator
        The ID of the member to retrieve; it is assigned by the
        Biological Directory of the United States Congress or
        can be retrieved from a member list request.
        """
        path = "members/{0}.json".format(member_id)
        return self.fetch(path)

    def filter(self, chamber, congress=CURRENT_CONGRESS, **kwargs):
        """
        Takes a chamber and Congress,
        OR state and district, returning a list of members
        """
        check_chamber(chamber)

        kwargs.update(chamber=chamber, congress=congress)

        if 'state' in kwargs and 'district' in kwargs:
            """
            #4 Get Current Members by State/District
            Chamber (house or senate)
            state (Two-letter state abbreviation)
            district (House of Representatives district number
            [House requests only])
            """
            path = ("members/{chamber}/{state}/{district}/"
                    "current.json").format(**kwargs)

        elif 'state' in kwargs:
            path = ("members/{chamber}/{state}/"
                    "current.json").format(**kwargs)

        else:
            """
            #1 LISTS OF MEMBERS
            Takes a chamber and congress and returns a list of departing members
            chamber - (house or senate)
            congress - (102-115 for house or 80-115 for Senate)
            """
            path = ("{congress}/{chamber}/"
                    "members.json").format(**kwargs)

        return self.fetch(path, parse=lambda r: r['results'])

    def bills(self, member_id, type='introduced'):
        """
        #9 GET BILLS COSPONSORED BY A SPECIFIC MEMBER
        Same as BillsClient.by_member
        type can be (introduced, cosponsored, withdrawn)
        The ID of the member is assigned by the Biographical Directory of the
        United States Congress or can be retrived from a member list request.
        """
        path = "members/{0}/bills/{1}.json".format(member_id, type)
        return self.fetch(path)

    def new(self, **kwargs):
        """
        #3 Get New Members
        Returns a list of new members
        """
        path = "members/new.json"
        return self.fetch(path)

    def departing(self, chamber, congress=CURRENT_CONGRESS):
        """
        #5 GET MEMBERS LEAVING OFFICE
        Takes a chamber and congress and returns a list of departing members
        congress (111-116)
        chamber (house or senate)
        """
        check_chamber(chamber)
        path = "{0}/{1}/members/leaving.json".format(congress, chamber)
        return self.fetch(path)

    def votes(self, member_id):
        """
        #6 GET A SPECIFIC MEMBERS VOTE POSITIONS
        Takes a member id and return the most recent vote positions for a specific
        member of the House of Representative or Senate

        The ID of the member is assigned by the Biographical Directory of the
        United States Congress or can be retrived from a member list request.
        """
        path = "members/{0}/votes.json".format(member_id)
        return self.fetch(path)

    def compare(self, first, second, chamber, type='votes', congress=CURRENT_CONGRESS):
        """
        #7 COMPARE TWO MEMBERS VOTE POSITIONS
        #8 COMPARE TWO MEMBERS BILL SPONSORSHIPS
        See how often two members voted together in a given Congress.
        Takes two member IDs, a chamber and a Congress number.

        Type can be (votes or bills)
        chamber (house or senate)
        The ID of the member is assigned by the Biographical Directory of the
        United States Congress or can be retrived from a member list request.
        congress (102-115 for house OR 101-115 for senate)
        """
        check_chamber(chamber)
        path = "members/{first}/{type}/{second}/{congress}/{chamber}.json"
        path = path.format(first=first, second=second, type=type,
                           congress=congress, chamber=chamber)
        return self.fetch(path)

    def party(self):
        """
        #1 GET STATE PARTY COUNTS - OTHER RESPONSES
        Get state party counts for the current Congress
        """
        path = "states/members/party.json"
        return self.fetch(path, parse=lambda r: r['results'])
    
