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








![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

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