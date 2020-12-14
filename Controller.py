# CST8333 20F Assignment 4
#
# Date: November 30, 2020
# Read data from a .csv file and create a pie chart.
# Created by Stewart King - 040 793 799

import csv
import Country as Country
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib, random

""" Object for the Controller, manipulates the data """


class Controller(object):
    """ This class contains the code required to open the csv file, create and fill the list,
    then print the contents of the list"""

    # creates an empty list
    covidList = []

    """
    Load the list
    Parameters: none
    Returns: none
    """

    def load_list(self):
        # Try catch for opening the file, exception is the file is missing or unavailable
        try:
            columns = ["ID", "Date", "Cases", "Deaths", "Name_fr", "Name_en"]
            # Read the csv using pandas
            read = pd.read_csv('InternationalCovid19Cases.csv', skiprows=1, names=columns)
            # write it into dataframe
            df = pd.DataFrame(read)
            # loop to create instances of each country and assign attributes to object then add it to the list
            for row in df.itertuples(index=False):
                # read in records and assign new class object with the required __init__ attributes
                country_temp = Country.Country(row.ID, row.Date, row.Cases, row.Deaths, row.Name_fr, row.Name_en)
                # adds country to the list of records
                self.covidList.append(country_temp)
            # trim list to 5000
            del self.covidList[4001:]

        # Exception prints that file is missing or unavailable if file can't be opened
        except FileNotFoundError:
            print("The file is missing or unavailable")

    """
    Create a file
    Parameters: none
    Returns: none
    """

    def create_file(self):
        with open('NewInternationalCovid19Cases.csv', 'w', newline='') as csv_file:
            # Use writer method
            writer = csv.writer(csv_file)
            # Writes the column headers at the top of the file
            writer.writerow(["ID", "Date", "Cases", "Deaths", "name_fr", "name_en"])
            # loop to write each country from the list into the file
            for country in self.covidList:
                # write to each row the following column fields
                writer.writerow([country.id, country.date, country.cases, country.deaths, country.name_fr,
                                 country.name_en])

    """
    Display a specific row or all rows
    Parameters: number
    Returns: none
    """

    def display_list(self, number):
        lineCounter = 0
        # Check user input
        if number < 0 or number > 4001:
            print("Please select a number between 0 and 5000")
            return

        # Column headers
        print("            ID     D      C De Name_fr Name_en")
        # Print the whole list
        if number == 0:
            for row in self.covidList:
                """Added row numbers. 
               Used https://stackoverflow.com/questions/5598181/multiple-prints-on-the-same-line-in-python
                to figure out how to not start a new line after the row number"""
                print(lineCounter, end="", flush=True)
                print(row)

        # Print the users selection
        else:
            print("Record:", number, ")", end=' ')
            print(self.covidList[number - 1])

    """
    Add a new country to the list
    Parameters: id, date, cases, deaths, name_fr, name_en
    Returns: none
    """

    def add_country(self, id, date, cases, deaths, name_fr, name_en):
        # add the new country to the list
        self.covidList.append(Country.Country(id, date, cases, deaths, name_fr, name_en))

    """
    Edit an existing country to the list
    Parameters: selected_country, id, date, cases, deaths, name_fr, name_en
    Returns: none
    """

    def edit_country(self, selected_country, id, date, cases, deaths, name_fr, name_en):
        # edit the country from the list
        self.covidList[selected_country - 1] = Country.Country(id, date, cases, deaths, name_fr, name_en)

    """
    Edit an existing country to the list
    Parameters: deleted_country, id, date, cases, deaths, name_fr, name_en
    Returns: none
    """

    def delete_country(self, delete_country):
        # delete the new country from the list
        del self.covidList[delete_country - 1]

    """
    Display pie chart
    Parameters: none
    Returns: none
    """

    def display_pieChart(self, x):

        # load list
        self.load_list()
        # Trim to the first 1000 records
        del self.covidList[x:]
        # convert the list back to a dataframe using Pandas
        data = pd.DataFrame([t.__dict__ for t in self.covidList])
        # add columns to the dataframe
        data.columns = ['ID', 'Date', 'Cases', 'Deaths', 'Name_fr', 'Name_en']
        # Group the cases by Country, sum the cases for each country
        datasum = data.Cases.groupby(data.Name_en).sum()
        # Give a title to the plot
        plt.title("COVID Cases from March-September 2020")
        # Generate the plot as a pie chart
        datasum.plot(kind='barh', color=['orange'])
        # set x axis and y axis label
        plt.xlabel("Total COVID Cases")
        plt.ylabel("Country Name")
        plt.tight_layout()
        # show the pie chart
        plt.show()
