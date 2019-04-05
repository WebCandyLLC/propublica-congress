from .client import Client
from .utils import check_quarter, check_category, get_offset


class OfficeExpensesClient(Client):
    """House of Representatives published quarterly reports detailing
        official office expenses by lawmakers. """

    # Need to validate member-id potentially

    def member(self, member, year, quarter):
        """
        #1 GET QUARTERLY OFFICE EXPENSES BY A SPECIFIC HOUSE MEMBER
        Member is the ID of the member to retrieve and is assigned by
        the Biographical DIrectory of the United States Congress or
        can be retrieved from a member list request

        Year include (2009-2017)

        Quarter include (1,2,3,4)
        """
        check_quarter(quarter)
        path = "members/{member}/office_expenses/{year}/{quarter}.json".format(
            member=member, year=year, quarter=quarter)
        return self.fetch(path)


    def categories(self, member, category):
        """
        #2 GET QUARTERLY OFFICE EXPENSES BY CATEGORY FOR A SPECIFIC 
        HOUSE MEMBER
        Member is the ID of the member to retrieve and is assigned by
        the Biographical DIrectory of the United States Congress or
        can be retrieved from a member list request

        Categories include 
        (travel, personnel, rent-utilities, other-services, 
        supplies, franked-mail, printing, equipment, total)
        """
        check_category(category)
        path = "members/{member}/office_expenses/category/{category}.json".format(
            member=member, category=category)
        return self.fetch(path)

    def category(self, category, year, quarter, **kwargs):
        """
        #3 GET QUARTERLY OFFICE EXPENSES FOR A SPECIFIED CATEGORY
        Categories include 
        (travel, personnel, rent-utilities, other-services, 
        supplies, franked-mail, printing, equipment, total)

        Years include (2009-2017)

        Quarter include (1,2,3,4)

        This request returns the 20 most recent results and supports
        pagination using multiples of 20.
        """
        path = "office_expenses/category/{category}/{year}/{quarter}.json".format(
            category=category, year=year, quarter=quarter)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)
