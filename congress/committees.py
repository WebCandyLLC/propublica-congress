from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber, get_offset


class CommitteesClient(Client):

    def filter(self, chamber, congress=CURRENT_CONGRESS):
        """
        #1 LISTS OF COMMITTEES
        Returns a list of Senate, House or Joint Committees

        chamber (house or senate or joint)
        congress(110-116)
        """
        check_chamber(chamber)
        path = "{congress}/{chamber}/committees.json".format(
            congress=congress, chamber=chamber)
        return self.fetch(path)

    def get(self, chamber, committee, congress=CURRENT_CONGRESS):
        """
        #2 GET A SPECIFIC COMMITTEE
        Gets Info about a single Senate or House committee, including
        members of that committee

        Committee IDs can be found in the committee list responses.

        chamber(house, senate, or joint)
        congress(110-116)
        committee (committee abbreviation, for ex. HSAG)
        """
        check_chamber(chamber)
        path = "{congress}/{chamber}/committees/{committee}.json".format(
            congress=congress, chamber=chamber, committee=committee)
        return self.fetch(path)

    def hearings(self, congress=CURRENT_CONGRESS, **kwargs):
        """
        #3 GET RECENT COMMITTEE HEARINGS
        Returns a list of 20 upcoming Senate or House Committee meetings.
        Previous Congresses will return the 20 latest by date.

        Pagination is supported

        congress(114-116)
        """
        path = "{congress}/committees/hearings.json".format(
            congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def hearing(self, chamber, committee, congress=CURRENT_CONGRESS, **kwargs):
        """
        #4 GET HEARINGS FOR A SPECIFIC COMMITTEE
        Returns a list of hearings for a specific Senate or House Committee.
        Returns the 20 most recent hearings.

        Pagination is supported

        congress(114-116)
        chamber (house or senate)
        committee (optional committee abbreviation, for ex. HSAG. Use
        the full committees response to find abbreviations)
        """
        check_chamber(chamber)
        path = "{congress}/{chamber}/committees/{committee}/hearings.json".format(
            congress=congress, chamber=chamber, committee=committee)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def subcommittee(self, chamber, committee, subcommittee,  congress=CURRENT_CONGRESS):
        """
        #4 GET A SPECIFIC SUBCOMMITTEE
        Get info about a single Senate or House subcommittee, including members of
        that subcommittee. Subcommittee ids can be found in the committee list
        or detail response.

        congress(114-116)
        chamber (house or senate or joint)
        committee (committee abbreviation, for ex. HSAG. Use
        the full committees response to find abbreviations)
        subcommittee (subcommittee abbreviation, for ex. HSAS28. Use
        the full committee response to find abbreviations)
        """
        check_chamber(chamber)
        path = "{congress}/{chamber}/committees/{committee}/subcommittes/{subcommittee}.json"
        path = path.format(congress=congress, chamber=chamber, committee=committee, 
                        subcommittee=subcommittee)
        return self.fetch(path)
