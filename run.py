"""
Contact book is an application that uses a terminal run
by Python code to access a google sheets document.
The user can retrieve, add and update information stored
in the google sheets document.

Uses gspread, googleauth and tabulate libraries.

Functions:

contacts_menu()
- allows user to navigate different functions
by providing a menu

validate_choice()
- takes 2 arguments, the value and numer of choices
- checks user input is valid

direct_user()
- takes 1 argument, choice
- takes user to chosen function based on the number
they have input

add_contact()
- provides user with input fields for first name, last
name, number, email, address
- runs inputs through validators and adds values to spreadsheet

validate_name()
- takes 1 argument for name
- checks name input valid

validate_number()
- takes 1 argument, number
- checks number input valid

validate_address()
- takes 1 argument, address
- checks address input valid

validate_email()
- takes 1 argument, email
- checks email input valid

remove_contact()
- allows user to delete contact row in spreadsheet

search_workbook()
- takes 2 arguments, term, function
- checks workbook to see if searched term is present

delete_all()
- clears all data in spreadsheet

validate_key()
- takes 1 argument, pressed_key
- checks if the user has pressed 'y' or 'n'
- required when user wants to delete something

search_contact()
- allows user to search for a contact and display
their data in the terminal

display_all()
- displays all contacts in the spreadsheet

update_contact()
- allows the user to search a contact they want to update
and select the information they would like to update

update_column()
- takes 3 arguments, heading, contact, column_no
- user enters new information, function passes input to
validators and updates relevant column for contact

exit phonebook()
- exits contact book system
- prints thank you message to user

main()
- runs main program

"""

# importing the python libraries
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

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
    the different contact options and make a selection, which is
    sent to the validate choice function
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
        print("7. Exit contact book")

        choice = input("Please enter your choice: \n")

        if validate_choice(choice, 7):
            print("Selection accepted. Redirecting you now...\n")
            break

    return choice


def validate_choice(values, no_of_choices):
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
        # throws error if user has input a number bigger than the
        # number of choices
        if int(values) > no_of_choices:
            raise ValueError(
                f"{num} is not a valid option from the list"
            )
        # raises an error if user enters 0
        if values == "0":
            raise ValueError(
                f"{num} is not a valid option from the list"
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

    # call upon a function based upon user input
    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contact()
    elif choice == "3":
        delete_all()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        display_all()
    elif choice == "6":
        update_contact()
    elif choice == "7":
        exit_phonebook()


def add_contact():
    """
    Takes user input to create new contact information for name,
    address, phone number and email address.
    Runs each data type through the relevant validation function
    before adding information to worksheet
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

    while True:
        # Assigns variable for address to user input
        contact_address = input("Please enter contact address including "
                                " postcode:\n")

        if validate_address(contact_address):
            new_contact.append(contact_address)
            break

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
    # User chooses if they wish you update another contact or
    # return to contacts book menu
    run_again(add_contact)


def validate_name(name):
    """
    Checks user input to make sure that user has
    not used any numbers or disallowed special characters.
    Checks user has entered alpha characters.
    Takes name as argument to be tested.
    """

    # Adding valid characters variable for validation rather than using
    # .isalpha() as some names may contain blank spaces or hyphens
    valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'
    alpha_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # if user enters character not in allowed characters, return false
    if not all(char in valid_characters for char in name):
        print("Invalid data. Allowed characters are alphabet, hyphen or space."
              "\n")
        return False
    # if user has not entered at least two characters, return false
    elif len(name) < 2:
        print("Invalid data. Minimum value 2 characters. \n")
        return False
    # if user has not entered at least one alpha character, return false
    elif not any(char in alpha_characters for char in name):
        print("Invalid data: Name must contain alphabet.")
        print("Cannot contain just blank space or hyphen.\n")
        return False
    else:
        return True


def validate_address(address):
    """
    Checks user input to make sure that user has
    not used any numbers or special characters
    """

    # Adding valid characters variable for validation rather than using
    # .isalpha() as some addresses may contain blank spaces, hyphens and commas
    invalid_characters = "?!/+_=()*^%$£@#~"
    alpha_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # check only allowed characters used
    if any(char in invalid_characters for char in address):
        print("Invalid data: Special characters not allowed for address."
              " Please try again.\n")
        return False
    # check address is at least 10 characters
    elif len(address) < 10:
        print("Invalid data: Minimum value 10 characters."
              f" You entered {len(address)}, please try again. \n")
        return False
    # check address has at least one alpha character
    elif not any(char in alpha_characters for char in address):
        print("Invalid data: Name must contain alphabet.")
        print("Cannot contain just blank space or hyphen.\n")
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
        for value in values:
            # check is value is a number
            if not value.isnumeric():
                raise ValueError(
                    "Number required. "
                    f"You entered {values}"
                )
            # Check to see if length of numbers user has entered is 10,
            # if not, then checks to see if length is 11
            elif len(values) != 10:
                if len(values) != 11:
                    # Throws error if user input is not required length
                    raise ValueError(
                        "Minimum value required is 10, maximum 11. "
                        f"You entered {len(values)}"
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
    alpha_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    try:
        # raise error if required characters not in input
        if "@" not in email:
            raise ValueError(
                "Missing '@'. Email address requires '@' and '.'"
            )
        elif "." not in email:
            raise ValueError(
                "Missing '.'. Email address requires '@' and '.'"
            )
        # raise error if input is not at least 10 characters
        elif len(email) < 10:
            raise ValueError(
                f"Minimum value 10 characters. "
                f"You entered {len(email)}"
            )
        # raise error if no alphabet characters in email
        elif not any(char in alpha_characters for char in email):
            raise ValueError(
                "Name must contain alphabet."
                "Cannot contain just blank space or hyphen"
            )
    except ValueError as e:
        # Provide error message to user with example of correct format
        print(f"Invalid data: {e}, please try again\n")
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
            # check if term is in workbook
            confirmed_info = search_workbook(search_term, remove_contact)

            # confirm user to be deleted
            print(f"Are you sure you want to delete "
                  f"{confirmed_info[0]} {confirmed_info[1]}"
                  f"?\n")
            delete_contact = input("Please enter 'Y' to delete and 'N'"
                                   " to return to contact book "
                                   "menu:\n").lower()
            # check user has input a valid key
            if validate_key(delete_contact):
                # delete contact if user chooses yes
                if delete_contact == "y":
                    # find row number
                    first_names = contacts.col_values(1)
                    last_names = contacts.col_values(2)
                    index = 1
                    if confirmed_info[0] in first_names:
                        for confirmed_info[0] in first_names:
                            if (((confirmed_info[0]) in first_names) and
                               (confirmed_info[1]) in last_names):
                                row = (index - 1)
                            index += 1
                    elif confirmed_info[1] in last_names:
                        for confirmed_info[1] in last_names:
                            if (((confirmed_info[0]) in first_names) and
                               (confirmed_info[1]) in last_names):
                                row = (index - 1)
                            index += 1
                    # delete row
                    contacts.delete_rows(row)

                    # Confirm deletion to the user
                    print("Contact successfully deleted.\n")
                    break
                # return user to menu if they choose no
                elif delete_contact == "n":
                    print("Contact deletion cancelled.\n")
                    break

    # User can choose if they want to remove another contact
    # or return to main contact book menu
    run_again(remove_contact)


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

        if validate_key(confirm_delete):
            if confirm_delete == "y":
                # Clear contacts workbook
                contacts.clear()
                # Add headings back in
                contacts.append_row(headings)
                # Confirm deletion to user
                print("All contacts successfully deleted.\n")
                # Automatically redirects user to menu as no more
                # contacts to delete
                print("Automatically redirecting you to menu...\n")
                break
            elif confirm_delete == "n":
                # Divert user back to main menu
                print("Contact deletion cancelled. Redirecting you to menu"
                      "...\n")
                main()
                break


def validate_key(pressed_key):
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
                f" {pressed_key}"
            )
    except ValueError as e:
        print(f"Invalid: {e}. Please try again.\n")
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

    # display contact data
    display_contact()

    run_again(search_contact)


def display_contact():
    """
    Gets user input, validates search term and retrieves contact
    information.
    Displays contact information to user in the terminal.
    """

    while True:

        search_term = input("Please enter the first name or the surname"
                            " of the contact:\n")

        # Pass search term to name validator before searching workbook
        if validate_name(search_term):

            # if the search term in workbook, retrieve row values
            confirmed_info = search_workbook(search_term, display_contact)

            print(f"Pulling up full information for '{search_term}'"
                  "...\n")

            # Print contact information the terminal for user
            print(f"First name: {confirmed_info[0]}")
            print(f"Last name: {confirmed_info[1]}")
            print(f"Address: {confirmed_info[2]}")
            print(f"Phone number: {confirmed_info[3]}")
            print(f"Email: {confirmed_info[4]}\n")
            break

    # Return row of chosen contact
    return confirmed_info


def display_all():
    """
    Retrieves all cell values and prints them to the terminal
    as a list of dictionaries
    """

    print("****************************************"
          "***************************************")
    # Confirm to user which function they have selected
    print("You have selected to display all contacts.\n")
    print("Retrieving list of contacts now...\n")

    # Retrieve all values from contacts workbook as list
    # of dictionaries
    list_of_contacts = contacts.get_all_records()

    # Prints list of contacts in a table
    print(tabulate(list_of_contacts, headers='keys', tablefmt='fancy_grid'))

    run_again(display_all)


def update_contact():
    """
    Use search_contact function to find contact user wishes
    to update.
    User can then decide which field they would like to update
    with an input method.
    Choice is validated and information passed to update_column
    function
    """

    print("****************************************"
          "***************************************")
    print("You have chosen to update an existing contact.\n")

    # User searches for contact they wish to update and contact information
    # is displayed to the terminal
    confirmed_info = display_contact()

    # confirm contact row
    first_names = contacts.col_values(1)
    last_names = contacts.col_values(2)
    index = 1
    if confirmed_info[0] in first_names:
        for confirmed_info[0] in first_names:
            if (((confirmed_info[0]) in first_names) and
               (confirmed_info[1]) in last_names):
                row = (index)
            index += 1
    elif confirmed_info[1] in last_names:
        for confirmed_info[1] in last_names:
            if (((confirmed_info[0]) in first_names) and
               (confirmed_info[1]) in last_names):
                row = (index)
            index += 1

    # Loop repeats until user makes a valid number selection, allow user to
    # select which information type they would like to update
    while True:
        print("Which would you like to update?")
        print("1. First name")
        print("2. Last name")
        print("3. Address")
        print("4. Phone number")
        print("5. Email")

        # User input to select which contact field they would like to update
        update_choice = input("Please enter your choice: \n")

        if validate_choice(update_choice, 5):

            # pass column no and row no to update_column function
            if update_choice == "1":
                update_column(row, "1")
                break
            elif update_choice == "2":
                update_column(row, "2")
                break
            elif update_choice == "3":
                update_column(row, "3")
                break
            elif update_choice == "4":
                update_column(row, "4")
                break
            elif update_choice == "5":
                update_column(row, "5")
                break


def update_column(contact, column_no):
    """
    Receive information for contact and which column should be updated and
    updates with user input.
    """

    update_message = "Updating contact information now...\n"

    # Send new info to relevant validation function for its type
    if column_no == "1":
        while True:
            new_name = input("Please enter new contact name:\n")

            if validate_name(new_name):
                print(update_message)
                break

        # Find cell in contacts spreadsheet and update it with the
        # new info given by user
        contacts.update_cell(contact, column_no, new_name)

        # Confirm successful operation to user
        print("Contact information successfully updated!\n")

    elif column_no == "2":
        while True:
            new_name = input("Please enter new contact name:\n")

            if validate_name(new_name):
                print(update_message)
                break

        # Find cell in contacts spreadsheet and update it with the
        # new info given by user
        contacts.update_cell(contact, column_no, new_name)

        # Confirm successful operation to user
        print("Contact information successfully updated!\n")

    elif column_no == "3":
        while True:
            new_address = input("Please enter a new address:\n")

            if validate_address(new_address):
                print(update_message)
                break

        contacts.update_cell(contact, column_no, new_address)
        print("Contact information successfully updated!\n")

    elif column_no == "4":
        while True:
            new_number = input("Please enter new phone number:\n")

            if validate_number(new_number):
                print(update_message)
                break

        contacts.update_cell(contact, column_no, new_number)
        print("Contact information successfully updated!\n")

    elif column_no == "5":
        while True:
            new_email = input("Please enter new email address:\n")

            if validate_email(new_email):
                print(update_message)
                break

        contacts.update_cell(contact, column_no, new_email)
        print("Contact information successfully updated!\n")

    run_again(update_contact)


def exit_phonebook():
    """
    Provide exit message to user and exit system
    """

    print("****************************************"
          "***************************************")
    print("System exiting...\n")
    print("Thank you for using your contact book!")
    print("****************************************"
          "***************************************")
    # exit system
    SystemExit()


def run_again(function):
    """
    Give user the option to run the same function again or
    return to the main menu.
    Provides better user experience
    """

    print("****************************************"
          "***************************************")

    while True:

        print("Would you like to run this function again?")
        repeat_function = input("Please enter 'Y' to run function again, or"
                                " 'N' to return to the main contact"
                                " book menu:\n").lower()

        # Runs function to check what key the user has pressed
        if validate_key(repeat_function):
            # Runs the same function again for the user if 'y'
            if repeat_function == "y":
                function()
                break
            # Takes user back to menu if 'n'
            elif repeat_function == "n":
                main()
                break


def search_workbook(term, function):
    """
    checks to see how many return results there are
    """

    print(f"Searching contacts list for '{term}'...\n")

    list_of_contacts = contacts.findall(term)
    # Get number of contacts matching search term
    no_contacts = len(list_of_contacts)

    first_names = contacts.col_values(1)
    last_names = contacts.col_values(2)
    index = 1
    rows = []

    # code to be executed if only one matching contact
    if no_contacts == 1:

        print(f"{term} found!\n")

        if term in first_names:
            for first_name in first_names:
                if first_name == term:
                    rows.append(index)
                index += 1

        if term in last_names:
            for last_name in last_names:
                if last_name == term:
                    rows.append(index)
                index += 1

        only_contact = rows[0]
        chosen_contact = contacts.row_values(only_contact)
        return chosen_contact

    # code to be exectuted if more than one contact found
    elif no_contacts > 1:
        print("Multiple matches found!")

        if term in last_names:
            for last_name in last_names:
                if last_name == term:
                    rows.append(index)
                index += 1

        elif term in first_names:
            for first_name in first_names:
                if first_name == term:
                    rows.append(index)
                index += 1

        for row in rows:
            found_contact = (contacts.row_values(row))

            # print row numbers which user can use to select contact
            print(f"{row}. {found_contact[0]} {found_contact[1]}")

        user_choice = input("Please input the index number of the "
                            "contact you wish to select:\n")

        row_num = int(user_choice)
        chosen_contact = contacts.row_values(row_num)

        return chosen_contact

    # give error message if user not found
    else:
        print(f"Contact '{term}' not found."
              " Please try again.\n")
        # ask user if they want to run again
        run_again(function)
        return False


def main():
    """
    Program to begin running all functions
    """
    choice = contacts_menu()
    direct_user(choice)


# Print message first to appear on initializing contact book
print("****************************************"
      "***************************************")
print("\t\t\t\tCONTACT BOOK", flush=False)

main()
