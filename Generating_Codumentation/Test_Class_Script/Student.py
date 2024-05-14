"""
This python script include Student class
"""


class Student:
    def __init__(self, name, age):
        """
        This is constructor.
        :param name: name of student
        :type name: str
        :param age: age of student
        :type age: int
        """
        self._name = name
        self._age = age

    @property
    def name(self):
        """
        This is getter of name.
        :return: name of student
        :return:
        """
        return self._name

    @name.setter
    def name(self, _name):
        """
        This is setter of name of student.
        :param _name: name of student
        :type _name: str
        :return: None
        """
        self._name = _name

    @property
    def age(self):
        """
        This is getter of age of student.
        :return: age of student
        :return:
        """
        return self._age

    @age.setter
    def age(self, _age):
        """
        This is setter of age of student.
        :param _age: age of student
        :type _age: int
        :param _age:
        :return:
        """
        self._age = _age
