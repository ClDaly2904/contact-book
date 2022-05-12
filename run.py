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

    # Loop repeats until user makes a valid number selection
    while True:
        print("Please select a number from the options below:")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Delete all contacts")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Update existing contact")
        print("7. Exit phonebook")

        choice = input("Please enter your choice: \n")

        if validate_choice(choice):
            print("Selection accepted. Redirecting you now...\n")
            break

    return choice


def validate_choice(values):
    """
    Inside the try, check the user has only entered one character,
    and that character is an integer
    """
    try:
        # Checks user has input only one value, else throws error
        num = [int(value) for value in values]
        if len(num) > 1:
            raise ValueError(
                 f"Select 1 option from the list. You provided {len(num)}\n"
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
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        delete_all()
    elif choice == '4':
        search_contact()
        """
    elif choice == '5':
        display_all()
    elif choice == '6':
        update_contact()
    elif choice == '7':
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
    print("You have selected to add a new contact.\n")
    print("Please enter the following details:")

    while True:
        # Assigns variable for first name to user input, converts to lowercase
        contact_fname = input("Please enter first name for contact:"
                              " \n").lower()

        if validate_name(contact_fname):
            new_contact.append(contact_fname)
            break

    while True:
        # Assigns variable for last name to user input, converts to lowercase
        contact_lname = input("Please enter last name for contact: \n").lower()

        if validate_name(contact_lname):
            new_contact.append(contact_lname)
            break

    contact_address = input("Please enter contact address including postcode: "
                            "\n")
    new_contact.append(contact_address)

    while True:
        contact_number = input("Please enter contact number: \n")

        if validate_number(contact_number):
            new_contact.append(contact_number)
            break

    while True:
        # Assigns variable for email to user input, converts to lowercase
        contact_email = input("Please enter contact email address: \n").lower()

        if validate_email(contact_email):
            new_contact.append(contact_email)
            break

    # Adds new row to contacts sheet if all data is valid
    contacts.append_row(new_contact)

    # Provides feedback to user that they have been successful
    print("Contact added successfully.\n")
    # Return user back to menu
    main()


def validate_name(name):
    """
    Checks user input to make sure that user has
    not used any numbers or special characters
    """

    # Adding valid characters variable for validation rather than using
    # .isalpha() as some names may contain blank spaces or hyphens
    valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'

    if not all(char in valid_characters for char in name):
        print("Invalid data. Allowed characters are alphabet, hyphen or space."
              "\n")
        return False
    else:
        return True


def validate_number(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """

    try:
        num = [int(value) for value in values]
        # Check to see if length of numbers user has entered is 10,
        # if not, then checks to see if length is 11
        if len(num) != 10:
            if len(num) != 11:
                # Throws error if user input is not required length
                raise ValueError(
                    "Minimum value required is 10, maximum 11."
                    f"You provided {len(num)}"
                )
    # Throws error if user has not entered a number
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_email(email):
    """
    Inside the try, check to see if the email contains
    necessary characters '@' and '.'.
    Raises ValueError if user has not input email characters
    """

    try:
        if "@" not in email:
            raise ValueError(
                "Email address requires @ and ."
            )
        elif "." not in email:
            raise ValueError(
                "Email address requires @ and ."
            )
    except ValueError:
        # Provide error message to user with example of correct format
        print("Invalid data, email must contain '@' and '.'"
              ". Please try again.")
        print("Example: contact@email.com\n")
        return False

    return True


def remove_contact():
    """
    Allows user to input the contact they want to delete,
    passes term to search_workbook function and deletes row if found
    """

    print("****************************************"
          "***************************************")
    # Confirm to user which function they have selected
    print("You have selected to delete a contact.\n")

    while True:

        search_term = input("Please input the first name or last name of"
                            " contact: \n")

        # Pass search term to name validator before searching workbook
        if validate_name(search_term):
            # if the search term in workbook, find row and delete it
            if search_workbook(search_term):
                confirmed_contact = contacts.find(search_term)
                contacts.delete_rows(confirmed_contact.row)
                # Confirm deletion to the user
                print("Contact successfully deleted.\n")
                break

    # Return user back to menu
    main()


def search_workbook(term):
    """
    Searches workbook and returns value if found,
    otherwise throws warning
    """

    print(f"Searching contacts list for '{term}'...\n")

    find_contact = contacts.find(term)

    if find_contact:
        # Confirm to user contact has been found
        print(f"{term} found!\n")
        return find_contact
    else:
        print(f"Contact '{term}' not found."
              " Please try again.\n")


def delete_all():
    """
    Deletes all values in contact book
    """

    print("****************************************"
          "***************************************")

    headings = ["first name", "last name", "address", "phone number",
                "email"]

    while True:
        print("You have selected to delete all contacts.\n")
        # Warn user they are about to clear all contacts
        print("Are you sure you want to proceed?")

        # Assigns variable for confirmation input, converts to lowercase
        # Make user confirm they wish to delete all contacts
        confirm_delete = input("Press 'Y' to delete all contacts"
                               " or 'N' to cancel and return to menu: "
                               "\n").lower()

        if validate_delete(confirm_delete):
            if confirm_delete == "y":
                # Clear contacts workbook
                contacts.clear()
                # Add headings back in
                contacts.append_row(headings)
                # Confirm deletion to user
                print("All contacts successfully deleted.\n")
                break
            elif confirm_delete == "n":
                # Divert user back to main menu
                print("Contact deletion cancelled. Redirecting you to menu"
                      "...\n")
                main()
                break

    main()


def validate_delete(pressed_key):
    """
    Inside the try, check to see if user has entered 'y' or 'n'.
    Raises value error if user has pressed incorrect key.
    """
    try:
        # Return y if user has pressed key
        if pressed_key == "y":
            return pressed_key
        # Return n if user has pressed key
        elif pressed_key == "n":
            return pressed_key
        else:
            # Reject user input, trigger loop again until acceptable input
            raise ValueError(
                "Invalid input. 'Y' or 'N' required, you entered"
                f" {pressed_key}\n"
            )
    except ValueError:
        print(f"Invalid input: {pressed_key}. Please try again.\n")
        return False

    return True


def search_contact():
    """
    Use search workbook function to find contact, get contact row,
    break down and print contact information to the terminal
    """

    print("****************************************"
          "***************************************")
    # Confirm to user which function they have selected
    print("You have selected to search for a contact.\n")

    while True:

        search_term = input("Please enter the first name or the surname"
                            " of the contact you would like to search:\n")

        # Pass search term to name validator before searching workbook
        if validate_name(search_term):
            # if the search term in workbook, find row and display to user
            if search_workbook(search_term):

                print(f"Pulling up full information for {search_term}...\n")

                # Find row number for contact
                confirmed_contact = (contacts.find(search_term)).row
                # Get a list of all contact information
                confirmed_info = contacts.row_values(confirmed_contact)

                # Print contact information the terminal for user
                print(f"First name: {confirmed_info[0]}")
                print(f"Last name: {confirmed_info[1]}")
                print(f"Address: {confirmed_info[2]}")
                print(f"Phone number: {confirmed_info[3]}")
                print(f"Email: {confirmed_info[4]}\n")
                break

    main()


def main():
    """
    Program to run all functions
    """
    choice = contacts_menu()
    direct_user(choice)


# Print message first to appear on initializing contact book
print("****************************************"
      "***************************************")
print("\t\t\t\tCONTACT BOOK", flush=False)

main()
