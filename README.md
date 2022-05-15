# Contacts Book

## Contents
- [About](#about)
- [User Experience](#user-experience)
    - [Target audiences](#target-audiences)
    - [User Stories](#user-stories)
    - [Contact Book Aims](#contact-book-aims)
    - [First Time Visitors](#first-time-visitors)
    - [Returning Visitors](#returning-visitors)
    - [User Journey](#user-journey)
- [Features](#features)
    - [Initialisation title](#initialisation-title)
    - [Contact book main menu](#contact-book-main-menu)
    - [Add contact function](#add-contact-function)
    - [Remove contact function](#remove-contact-function)
    - [Search for contact function](#search-for-contact-function)
    - [Display all contacts function](#display-all-contacts-function)
    - [Delete all contacts function](#delete-all-contacts-function)
    - [Update contact function](#update-contact-function)
    - [Exit contact book function](#exit-contact-book-function)
    - [Return to menu option](#return-to-menu-option)
    - [Validation for user inputs](#validation-for-user-inputs)

## About

Contacts book is a Python terminal database, which runs in the Code Institute mock terminal on Heroku.

Users can create, access and delete records of their contacts including name, address, number and email.

## User Experience

### Target Audiences

- For users that want to compile their contacts
- For users that already have a physical contact book, but are looking to transfer this to a digital version
- For users that are familiar to accessing information on a digital database
- For users new to accessing information on a digital database


### User Stories

- As a user, I am looking to store my contacts digitally
- As a user, I need to be able to add contacts to the database
- As a user, I need to be see my list of contacts
- As a user, I would like to be able to search for my contacts
- As a user, I need to be able to update any changes to my contacts
- As a user, I need an interface that lets me navigate my stored information
- As a user, I need clear instructions how to navigate the database


### Contact Book Aims

- To create a database that runs in the terminal (in this case the Code Institute mock terminal run on Heroku)
- To provide the user with a valuable database where they can store their contact information
- To provide the user with a means to navigate the database and access their information
- To provide clear navigation between different functions
- To provide the user with a means to amend their stored information
- To allow the user to delete any unwanted information
- To make sure that the user is only entering valid information into the database


### First Time Visitors

- Visitors are greeted by an initialisation title and a menu that displays the clear functionality of the contact book
- Input commands and error messages guide the user through the experience of adding, updating and removing contacts
- Messages confirming the completion of tasks appear in the terminal to confirm to the user what actions have been taken, thus improving user experience and understanding


### Returning Visitors

- Options to display all existing contacts and searching through contacts are of particular benefit to returning users who have returned to the contact book, as they provide a easy way to retrieve their stored information
- Returning users also have the ability to update and information that may no longer be accurate


### User Journey

1. As a user, I initialise my contact book in the terminal and am met by a menu that displays all the different things I am able to do
2. I see that the options are numbered and to choose one I need to input that number into the terminal
3. I choose to add a new contact so enter number 1, the terminal confirms my selection and I can see it is redirecting me
4. The terminal tells me what information to enter
5. I didn't enter enough values for the phone number, so this is returned to me as an error for me to try again
6. Once all the information is entered, the terminal confirms that the contact is successfully added and asks if I would like to add another contact or return to the main menu. It tells me I need to press y or n
7. I press y, as I want to add some more contacts then once I am finished return to the main menu
8. I need to get a number for one of my contacts, so I press 4 to search through my contacts
9. I see I can enter either their first or last name to search my contacts list. The contact is returned to me showing all information on that contact
10. I am done with the contacts for now, so when asked I press n to return to main menu and then 7 to exit
11. The system confirms it is shutting down


Whilst planning the functionality for the contacts book, I had to consider how I was going to achieve both the aims for the user and the contact book creators. This led to the creation of the features found in the Features section.


## Features

### Initialisation title

- For visual effect upon initialisation
- Welcomes user to program and confirms purpose


### Contact book main menu

- Plays a pivotal role in allowing the user to navigate around between functions
- User can review the different functions of the contact book and choose which one(s) they would like to use
- Numbered so that user can enter the number of the function the wish to use


### Add contact function

- Appears at the top of the contact list main menu as is the function most first time users will want to start with
- Allows the user to add a new contact to their contacts book
- User will need to input information for first name, last name, address, phone number and email. Each is presented to the user in its own input for ease- the user does not have to worry about formatting the data into a list
- Each data type has it's own validation to ensure the user is inputting accurate data
- Confirms back to the user when the contact has been succesfully added


### Remove contact function

- Allows the user to delete a stored contact
- User can search for the contact through using either their first or last name
- Terminal messages track the system searching for the contact and confirms if the user is found or not
- The use of template literals confirms the search term to the user
- If the contact is not found, the user gets to try the search again
- If the contact is found, the user is asked to confirm whether they wish to delete the contact by pressing either 'y' to delete, or 'n' to cancel and return to the main menu. This helps safeguard the user against accidentally deleting a contact


### Search for contact function

- Function is the primary way that the user would access the information they had stored
- Allows user to search for contact and retrieves the information for that contact
- User can search for contact by using either their first name or their last name
- If contact is found, all of the information for that contact is displayed to the terminal


### Display all contacts function

- Useful for the user to review all of the contact information they hold
- Prints the information for all contacts to the terminal as a list of dictionaries


### Delete all contacts function

- Allows the user to delete all of their current contact information
- If selected from the main contacts menu, the user will have to confirm that they want to delete all contacts using 'y' or 'n'. This helps avoid the user accidentally clearing their contacts database
- Confirms deletion of all contacts in the terminal if user chooses 'y', or cancels deletion and returns user to the menu if the user selects 'n'


### Update contact function

- Lets the user update information for an existing contact
- The user chooses which information field they would like to update by entering a number. I decided this was more user friendly than the user having to input the whole contact again with the new changes, and the user can always run the function again if they have more than one change to implement
- The user then inputs the new information for that contact, which is run through the validator for the respective data type
- Terminal confirms update in contact information


### Exit contact book function

- Once the user has finished with the contact book, they can choose option '7' on the main contact menu to exit the program
- Terminal displays message to thank user for using the contact book, and confirms the system exit


### Return to menu option

- After each function from the main menu has been executed (with the exception of exit contact book), the user is asked if they would like to perform their last function again by entering 'y', or they can choose to press 'n' to return to the main menu
- This improves user experience as means that the user does not need to re-initialise the contact book after they complete a task. It also reduces contact points for those users wishing to repeat a function, and is less visually confusing, when compared to my original idea of automatically bringing up the menu
- The only function from the main menu that the return to menu option does not appear for is the delete all contacts function as there is no point for the user to repeat this task, so the user is still automatically redirected back to the menu


### Validation for user inputs

- Each time the user enters an input, their response will be validated to ensure information accuracy and that the contacts book will run the required task
- Each field is validated to ensure that they cannot enter an empty string
- Choice validation
    - Only accepts one character
    - Will not accept a '0' or any number larger than the number of choices
    - Only accepts numbers
- Name validation
    - Does not allow numbers or special characters (other than space and hyphen as these can occur in names)
    - Minimum length requirement ('2')
- Address validation
    - Limits on special characters
    - Minimum length requirement ('10')
- Number validation
    - Only allow numbers
    - Number of values must be either '10' or '11'
- Email validation
    - Minimum length value '10'
    - Must include '@' and '.'
- If a user input does not meet the validation requirements, an error message will be displayed to the user. This informs the user that there has been an error and improves user experience by telling them what they have done wrong






## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!