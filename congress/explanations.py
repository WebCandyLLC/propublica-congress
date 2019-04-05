from .client import Client
from .utils import CURRENT_CONGRESS, get_offset


class ExplanationsClient(Client):
    # Need to add offet querystring parameter check for account
    # for any offset with multiples of 20


    def recent(self, congress=CURRENT_CONGRESS, **kwargs):
        """
        #1 GET RECENT PERSONAL EXPLANATIONS
        Gets the 20 most recent personal explanations for missed
        or mistaken votes in the Congressional Record. These 
        explanations can refer to a single vote or to multiple
        votes.

        congress (107-115)

        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "{congress}/explanations.json".format(congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def personal(self, congress=CURRENT_CONGRESS, **kwargs):
        """
        #2 GET RECENT PERSONAL EXPLANATION VOTES
        Gets the 20 most recent personal explanations for missed
        or mistaken votes in the Congressional Record. This response
        contains explanations parsed to a individual votes and have
        an additional 'category' attribute describing the general
        reason for the absense or incorrect vote.

        congress (107-115)

        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "{congress}/explanations/votes.json".format(congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def category(self, type, congress=CURRENT_CONGRESS, **kwargs):
        """
        #3 GET RECENT PERSONAL EXPLANATION VOTES BY CATEGORY
        Gets the 20 most recent personal explanations for missed
        or mistaken votes in the Congressional Record. This response
        contains explanations parsed to individual votes and have an
        additional 'category' attibute describing the general reason
        for the absence or incorrect vote. Gets list of recent personal
        explanations votes filtered by a category.

        congress (107-115)

        type:
            voted-incorrectly | voted yes or no by mistake
            official-business | away on official congressional business
            ambiguous | no reason given
            travel-difficulties | travel delays and issues
            personal | personal or family reason
            claims-voted | vote made but not recorded
            medical | medical issue for lawmaker (not family)
            weather | inclement weather
            memorial | attending memorial service
            misunderstanding | not informed of vote
            leave of absence | granted leave of absence
            prior-committment | attending to prior commitment
            election-related | participating in an election
            military-service | military service
            other | other

        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "{congress}/explanations/votes/{type}.json".format(
            type=type)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def recent_member(self, member_id, congress=CURRENT_CONGRESS, **kwargs):
        """
        #4 GET RECENT PERSONAL EXPLANATION BY A SPECIFIC MEMBER
        Gets the 20 most recent personal explanations for missed
        or mistaken votes in the Congressional Record by a specific
        member

        congress (110-116)
        member_id (Id assigned by the Biographical Directory of the
        United States Congress or can be retrived from a member list
        request.)

        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "members/{member_id}/explanations/{congress}.json".format(
            member_id=member_id, congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def personal_member(self, member_id, congress=CURRENT_CONGRESS, **kwargs):
        """
        #5 GET RECENT PERSONAL EXPLANATION BY A SPECIFIC MEMBER
        Gets the 20 most recent personal explanations for missed
        or mistaken votes in the Congressional Record by a specific
        member. This response contains explanations parsed to a 
        individual votes and have an additional 'category' attribute 
        describing the general reason for the absense or incorrect vote.

        congress (110-116)
        member_id (Id assigned by the Biographical Directory of the
        United States Congress or can be retrived from a member list
        request.)

        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "members/{member_id}/explanations/{congress}/votes.json".format(
            member_id=member_id, congress=congress)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)

    def category_member(self, type, member_id, congress=CURRENT_CONGRESS, **kwargs):
        """
        #6 GET RECENT PERSONAL EXPLANATION VOTES BY CATEGORY
        Gets the 20 most recent personal explanations for missed
        or mistaken votes in the Congressional Record by a specific
        member. This response contains explanations parsed to 
        individual votes and have an additional 'category' attibute 
        describing the general reason for the absence or incorrect 
        vote. Gets list of recent personal explanations votes 
        filtered by a category.

        congress (110-116)
        member_id (Id assigned by the Biographical Directory of the
        United States Congress or can be retrived from a member list
        request.)
        type:
            voted-incorrectly | voted yes or no by mistake
            official-business | away on official congressional business
            ambiguous | no reason given
            travel-difficulties | travel delays and issues
            personal | personal or family reason
            claims-voted | vote made but not recorded
            medical | medical issue for lawmaker (not family)
            weather | inclement weather
            memorial | attending memorial service
            misunderstanding | not informed of vote
            leave of absence | granted leave of absence
            prior-committment | attending to prior commitment
            election-related | participating in an election
            military-service | military service
            other | other

        This response supports pagination using an offset
        parameter with multiples of 20.
        """
        path = "members/{member_id}/explanations/{congress}/votes/{type}.json".format(
            member_id=member_id, congress=congress, type=type)
        if 'page' in kwargs:
            offset = get_offset(kwargs.get('page'))
            path = path.join("?offset={offset}".format(offset))
        return self.fetch(path)