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
    print("Welcome to your contacts book!")

    while True:
        print("Please select a number from the options below:")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Delete all contacts")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Update existing contact")
        print("7. Exit phonebook")

        choice = input("Please enter your choice: ")

        if validate_choice(choice):
            print("Selection accepted. Redirecting you now...")
            break

    return choice


def validate_choice(values):
    """
    Inside the try, check the user has only entered one character,
    and that character is an integer
    """
    try:
        # Checks user has input only one value, else throws error
        [int(value) for value in values]
        if len(values) > 1:
            raise ValueError(
                 f"Select 1 option from the list. You provided {len(values)}"
            )
    # Throws error if user has not entered a number
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def direct_user(choice):
    """
    Function to take user selection from menu
    function and direct user to correct function
    """

    if choice == '1':
        add_contact()

        """
    elif choice == 2:
        remove_contact()
    elif choice == 3:
        delete_all()
    elif choice == 4:
        search_contact()
    elif choice == 5:
        display_all()
    elif choice == 6:
        update_contact()
    elif choice == 7:
        exit_phonebook()
        """


def add_contact():
    """
    Takes user input to create new contact information for name,
    address, phone number and email address.
    """
    new_contact = []

    print("****************************************"
          "***************************************")
    print("You have selected to add a new contact.")
    print("Please enter the following details:")

    while True:
        # Assigns variable for first name to user input, converts to lowercase
        contact_fname = input("Please enter first name for contact:").lower()

        if validate_name(contact_fname):
            new_contact.append(contact_fname)
            break

    while True:
        # Assigns variable for last name to user input, converts to lowercase
        contact_lname = input("Please enter last name for contact:").lower()

        if validate_name(contact_lname):
            new_contact.append(contact_lname)
            break

    contact_address = input("Please enter contact address including postcode:")
    contact_number = input("Please enter contact number:")
    contact_email = input("Please enter contact email address:")

    new_contact.append(contact_address)
    new_contact.append(contact_number)
    new_contact.append(contact_email)
    contacts.append_row(new_contact)

    # Provides feedback to user that they have been successful
    print("Contact added successfully.\n")


def validate_name(name):
    """
    Checks user input to make sure that user has
    not used any numbers or special characters
    """

    # Adding valid characters variable for validation rather than using
    # .isalpha() as some names may contain blank spaces or hyphens
    valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'

    if not all(char in valid_characters for char in name):
        print("Invalid data. Allowed characters are alphabet, hyphen or space")
        return False
    else:
        return True


def main():
    """
    Program to run all functions
    """
    choice = contacts_menu()
    direct_user(choice)


main()
