# importing the python libraries
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contact_book')

contacts = SHEET.worksheet('contacts')
data = contacts.get_all_values()


def contacts_menu():
    """
    Menu to initialize when program first runs. User can view all
    the different contact options and make a selection.
    """
    print("****************************************"
          "***************************************")
    print("\t\t\t\tCONTACT BOOK", flush=False)
    print("****************************************"
          "***************************************")
    print("Welcome to your contacts book! "
          "Please select a number from the options below:")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Update existing contact")
    print("7. Exit phonebook")
    choice = int(input("Please enter your choice: "))


def main():
    """
    Program to run all functions
    """
    contacts_menu()


main()
