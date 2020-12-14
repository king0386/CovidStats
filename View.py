# CST8333 20F Assignment 4
#
# Date: November 30, 2020
# Read data from a .csv file and create a pie chart.
# Created by Stewart King - 040 793 799

from Model import Model

"""Object for View class"""


class View(object):

    """
    Constructor
    Parameters: none
    Returns: none
    """
    def __init__(self):
        self.model = Model()

    """
    Main menu with options for the user
    Parameters: none
    Returns: none
    """
    def main_menu(self):
        print("\nInternational COVID19 Loader - By Stewart King\n")
        print("Main Menu, load the list by selecting option 1 before selecting any option \n"
              "1. Reload the data from the dataset \n"
              "2. Write to a new file \n"
              "3. Select one record to display, or all records \n"
              "4. Create a new record and store it in the list \n"
              "5. Edit an existing record \n"
              "6. Delete an existing record \n"
              "7. Display a chart for the # of Cases by Country \n"
              "0. To exit the program \n")

        option = int(input("Select one of the following menu items: "))

        # While loop to ensure user selects only from menu items
        while option != 0:

            # if/else statement for the user inputs
            if option == 1:
                # Reload data from the dataset
                Model().reload_list()
                # print menu
                v.main_menu()

            elif option == 2:
                # Create a file
                Model().create_file()
                v.main_menu()

            elif option == 3:
                # User has to choose normal display or by multiple columns
                choice = int(input("Enter a row between 1 to 100 to display one record, 0 to see all: "))
                Model().display_list(choice)
                v.main_menu()

            elif option == 4:
                # User enters the following fields
                id_entry = str(input("Enter the ID of the country: "))
                date_entry = str(input("Enter the date: year-month-day "))
                cases_entry = str(input("Enter the # of cases: "))
                deaths_entry = str(input("Enter the # of deaths: "))
                name_fr_entry = str(input("Enter the french name of the country "))
                name_en_entry = str(input("Enter english name of the country "))
                # pass these entries to model then controller
                Model().create_country(id_entry, date_entry, cases_entry, deaths_entry, name_fr_entry, name_en_entry)
                # call menu again
                v.main_menu()

            elif option == 5:
                # User edit an existing country, select an existing row and update the attributes
                selected_country = int(input("Enter the row of the country to edit: "))
                id_edit = str(input("Enter the new ID of the country: "))
                date_edit = str(input("Enter the new date: year-month-day: "))
                cases_edit = str(input("Enter the # of cases: "))
                deaths_edit = str(input("Enter the # of deaths: "))
                name_fr_edit = str(input("Enter the french name of the country: "))
                name_en_edit = str(input("Enter english name of the country: "))
                # pass these entries to model then controller
                Model().update_covidList(selected_country, id_edit, date_edit, cases_edit, deaths_edit,
                                         name_fr_edit, name_en_edit)
                v.main_menu()

            elif option == 6:
                # User delete an existing country, enters an ID
                delete_country = int(input("Enter the row of the country to delete: "))
                # Pass this ID to the model then controller
                Model().delete_country(delete_country)
                v.main_menu()

            elif option == 7:
                # Out of 34459 records for countries, up to how many records to display
                choice = int(input("Enter number of records betweeen 0 - 4000 to generate pie chart: "))
                # Call pie chart
                Model().display_chart(choice)
                v.main_menu()

            # If user selects 0 then exits program
            exit(0)


if __name__ == "__main__":
    v = View()
    v.main_menu()