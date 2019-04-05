from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber, get_offset


class FloorActionsClient(Client):
    # Need to add offet querystring parameter check for account
    # for any offset with multiples of 20


    def recent(self, chamber, congress=CURRENT_CONGRESS, **kwargs):
        """
        #1 GET RECENT HOUSE AND SENATE FLOOR ACTIONS
        Takes the available congress number (113-116) and the
        chamber (house or senate) and returns the 20 most recent
        results and supports pagination using multiples of 20.

        The date attribute in result represents the "legislative day"
        in which the action took place. (actions that occur after
        midnight often are part of the previous day's activity)
        """
        check_chamber(chamber)
        path = "{congress}/{chamber}/floor_updates.json".format(
            congress=congress, chamber=chamber)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def date(self, chamber, year, month, day, **kwargs):
        """
        #2 GET HOUSE AND SENATE FLOOR ACTIONS BY DATE
        Takes the chamber (house or senate) and year (YYYY),
        month (MM), day (DD) and returns the 20 most recent
        results for that date and supports pagination using
        multiples of 20.
        """
        check_chamber(chamber)
        path = "{chamber}/floor_updates/{year}/{month}/{day}.json".format(
            chamber=chamber, year=year, month=month, day=day)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)
