# CST8333 20F Assignment 4
#
# Date: November 30, 2020
# Read data from a .csv file and create a pie chart.
# Created by Stewart King - 040 793 799

class Record:

    """
    Constructor to assign values for the attributes
    Parameters: id, date
    Returns: An object using the attributes in method header and sets the user-entered attributes to the class
    attributes
    """

    def __init__(self, id, date):
        self.id = id
        self.date = date

    """
    Method that prints the two attributes of the class in a string format
    Parameters: none  
    Returns: String with id and date
    """

    def __str__(self):
        return self.id + " " + self.date


""" Object for Country including its fields, inherits from the Record class """


class Country(Record):

    """
    Constructor to assign values for the attributes
    Parameters: cases, deaths, name_fr, name_en
    Returns: Creates an object using the attributes in method header and sets the user-entered attributes to the class attributes
    """

    def __init__(self, id, date, cases, deaths, name_fr, name_en):
        super().__init__(id, date)
        self.cases = cases
        self.deaths = deaths
        self.name_fr = name_fr
        self.name_en = name_en

    """
    Method that prints all the attributes of the class in a string format
    Parameters: none  
    Returns: String with id and date coming from a super class method, cases, deaths, name_fr and name_en
    """

    def __str__(self):
        return super().__str__() + " " + str(self.cases) + " " + str(self.deaths) + " " + self.name_fr + " " \
               + self.name_en