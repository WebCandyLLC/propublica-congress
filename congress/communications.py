import datetime

from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber, check_comms


class CommunicationsClient(Client):

    def recent(self, congress=CURRENT_CONGRESS):
        """
        #1 GET RECENT OFFICIAL COMMUNICATIONS
        Gets list of offical communications to Congress from the
        president, executive branch agencies and state legislatures
        to congressional committees. Request returns the 20 most
        recent results. The data covers communications to the
        house of representatives since 2015, and communications
        to the Senate since 1979.

        congress(114-115 for house or 96-115 for senate)
        """
        path = "{congress}/communications.json".format(
            congress=congress)
        return self.fetch(path)

    def category(self, category, congress=CURRENT_CONGRESS):
        """
        #2 GET RECENT OFFICIAL COMMUNICATIONS BY CATEGORY
        Returns a list of official communications to Congress in 
        a specific category. This request returns the 20 most recent results
        for the specified type.

        Types:
            ec (Executive Communication)
            pm (Presidential Message)
            pom (Petition or Memorial)

        congress(114-115 for house or 96-115 for senate)
        """
        check_comms(category)
        path = "{congress}/communications/category/{category}.json".format(
            congress=congress, category=category)
        return self.fetch(path)

    def date(self, date):
        """
        #3 GET RECENT OFFICIAL COMMUNICATIONS BY DATE
        Returns a list of official communications to Congress on
        a specific date. This request returns the 20 most recent results
        for the specified date.

        date (YYYY-MM-DD format)
        """
        path = "communications/date/{date}.json".format(
            date=date)
        return self.fetch(path)

    def today(self):
        "#4 Return today's list of official communications to Congress"
        now = datetime.date.today()
        return self.date(now)

    def chamber(self, chamber, congress=CURRENT_CONGRESS):
        """
        #4 GET RECENT OFFICIAL COMMUNICATIONS BY CHAMBER
        Returns a list of official communications to Congress for
        a specific chamber. This request returns the 20 most recent
        results for the specified chamber.

        chamber (house or senate)
        congress(114-115 for house or 96-115 for senate)
        """
        check_chamber(chamber)
        path = "{congress}/communications/{chamber}.json".format(
            congress=congress, chamber=chamber)
        return self.fetch(path)