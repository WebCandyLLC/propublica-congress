import datetime

from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber, parse_date, get_offset, get_congress


class VotesClient(Client):

    # date-based queries
    """
    #4 GET VOTES BY DATE
    Get all votes for one or both chambers in a particular month, or all votes
    in a particular date range (fewer than 30 days).

    chamber (house, or senate, or both)
    year - YYYY format
    month - MM format
    """
    def by_month(self, chamber, year=None, month=None):
        """
        #4 Return votes for a single month, defaulting to the current month.
        """
        check_chamber(chamber)

        now = datetime.datetime.now()
        year = year or now.year
        month = month or now.month

        path = "{chamber}/votes/{year}/{month}.json".format(
            chamber=chamber, year=year, month=month)
        return self.fetch(path, parse=lambda r: r['results'])

    def by_range(self, chamber, start, end):
        """
        #4 Return votes cast in a chamber between two dates,
        up to one month apart.

        chamber (house or senate)
        start - YYYY-MM-DD format
        end - YYYY-MM-DD format
        """
        check_chamber(chamber)

        start, end = parse_date(start), parse_date(end)
        if start > end:
            start, end = end, start

        path = "{chamber}/votes/{start:%Y-%m-%d}/{end:%Y-%m-%d}.json".format(
            chamber=chamber, start=start, end=end)
        return self.fetch(path, parse=lambda r: r['results'])

    def by_date(self, chamber, date):
        "#4 Return votes cast in a chamber on a single day"
        date = parse_date(date)
        return self.by_range(chamber, date, date)

    def today(self, chamber):
        "#4 Return today's votes in a given chamber"
        now = datetime.date.today()
        return self.by_range(chamber, now, now)

    # detail response
    def get(self, chamber, rollcall_num, session, congress=CURRENT_CONGRESS):
        """
        #2 GET A SPECIFIC ROLL CALL VOTE
        Return a specific roll-call vote, including a complete list of member positions

        congress (102-115 for house, 80-115 for senate)
        chamber (house or senate)
        session-number (1 or 2, depending on year (1 - odd years, 2 - even years))
        roll-call-number (integer)
        """
        check_chamber(chamber)

        path = ("{congress}/{chamber}/sessions/{session}"
                "/votes/{rollcall_num}.json")
        path = path.format(congress=congress, chamber=chamber,
                           session=session, rollcall_num=rollcall_num)
        return self.fetch(path, parse=lambda r: r['results'])

    # votes by type
    def by_type(self, chamber, type, congress=CURRENT_CONGRESS):
        """
        #3 GET VOTES BY TYPE
        Return votes by type: missed, party, lone no, perfect
        Missed votes provides info about the voting attendance of each member
        of a specific chamber and congress. Party votes provides info about how often
        each member of a specific chamber and congress votes with a majority of his or her
        party. Lone no votes provides info lists members in a specific chamber and congress
        who were the only members to vote No on a roll call vote, and how often that
        happened. Perfect votes lists members in a specific chamber and congress who voted 
        Yes or No on every vote for which he or she was eligible.

        congress (102-115 for house, 80-115 for Senate)
        chamber (house or senate)
        vote-type (missed, party, loneno, or perfect)
        """
        check_chamber(chamber)

        path = "{congress}/{chamber}/votes/{type}.json".format(
            congress=congress, chamber=chamber, type=type)
        return self.fetch(path)

    def missed(self, chamber, congress=CURRENT_CONGRESS):
        "#3 Missed votes by member"
        return self.by_type(chamber, 'missed', congress)

    def party(self, chamber, congress=CURRENT_CONGRESS):
        "#3 How often does each member vote with their party?"
        return self.by_type(chamber, 'party', congress)

    def loneno(self, chamber, congress=CURRENT_CONGRESS):
        "#3 How often is each member the lone no vote?"
        return self.by_type(chamber, 'loneno', congress)

    def perfect(self, chamber, congress=CURRENT_CONGRESS):
        "#3 Who never misses a vote?"
        return self.by_type(chamber, 'perfect', congress)

    def recent(self, chamber, **kwargs):
        """
        #1 GET RECENT VOTES
        Get recent votes from the House, Senate, or both chambers.
        The request returns the 20 most recent results, sorted by
        date and roll call number, and you can paginate through the votes
        using the offset querystring parameter that accepts multiples of 20.

        chamber (house, senate, or both)
        """
        check_chamber(chamber)

        path = "{chamber}/votes/recent.json".format(
            chamber=chamber)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def nominations(self, congress=CURRENT_CONGRESS):
        """
        #5 GET SENATE NOMINATION VOTES
        Return Senate votes on presidential nominations

        congress (101-116)
        """
        path = "{congress}/nominations.json".format(congress=congress)
        return self.fetch(path)
