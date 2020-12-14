# CST8333 20F Assignment 4
#
# Date: November 30, 2020
# Read data from a .csv file and create a pie chart.
# Created by Stewart King - 040 793 799

from Controller import Controller

"""Object for Model"""


class Model(object):

    """
    Constructor to initialize list and controller
    Parameters: none
    Returns: Creates an object and initializes list using readALl method
    """
    def __init__(self):
        # instance of controller created
        self.controller = Controller()

    """
    Reads from the list
    Parameters: none
    Returns: list of records
    """
    def reload_list(self):
        self.controller.load_list()
        print("List has been successfully reloaded")

    """
    Create a new file
    Parameters: none
    Returns: none
    """
    def create_file(self):
        self.controller.create_file()
        print("File was successfully created")

    """
    Displays the list of records
    Parameters: user_input
    Returns: none
    """
    def display_list(self, user_input):
        self.controller.display_list(user_input)
        print("List is successfully displayed")

    """
    Create a new record in the list
    Parameters: id, date, cases, deaths, name_fr, name_en
    Returns: none
    """
    def create_country(self, id, date, cases, deaths, name_fr, name_en):
        self.controller.add_country(id, date, cases, deaths, name_fr, name_en)
        print("Country was successfully created")

    """
    Update an existing record on the list
    Parameters: id, date, cases, deaths, name_fr, name_en
    Returns: none
    """
    def update_covidList(self, selected_country, id, date, cases, deaths, name_fr, name_en):
        self.controller.edit_country(selected_country, id, date, cases, deaths, name_fr, name_en)
        print("Country info updated")

    """
    Delete an existing record
    Parameters: none
    Returns: none
    """
    def delete_country(self, delete_country):
        self.controller.delete_country(delete_country)
        print("Country successfully deleted")

    """
    Display chart
    Parameters: none
    Returns: none
    """
    def display_chart(self, choice):
        self.controller.display_pieChart(choice)