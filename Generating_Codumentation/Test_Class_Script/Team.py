"""
This script contains Test class
"""


class Team:
    """
    This class contains Student members of Team
    """

    def __init__(self, name):
        """
        This is constructor method
        :param name: name of the team
        :type name: str
        :param name:
        """
        self._name = name
        self._members = []

    @property
    def name(self):
        """
        This method returns the name of the team
        :return:
        """
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def members(self):
        return self._members

    def add_member(self, member):
        """
        This method adds a member to the team
        :param member: Student member
        :type member: Student
        :return:
        """
        self._members.append(member)

    @members.setter
    def members(self, value):
        self._members = value

