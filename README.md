# Venita_Kissell_T1A3
## R3
Provide full attribution to referenced sources.
```
Cole, Anna. “Building a Python App Using Terminal - Python’s Gurus - Medium.” Medium, Python’s Gurus, Feb. 2024, medium.com/pythons-gurus/
```
```
a-beginners-guide-on-how-to-build-a-simple-python-application-with-a-command-line-interface-6d7fb187789b. Accessed 5 July 2024.
```
```
“Database Flowchart Symbols.” Https://Www.conceptdraw.com, www.conceptdraw.com/How-To-Guide/database-flowchart-symbols.
```
```
Programiz. “Design Flowchart in Programming (with Examples) - Programiz.” Programiz.com, 2019, www.programiz.com/article/flowchart-programming.
```
```
van Rossum, Guido, et al. “PEP 8 – Style Guide for Python Code.” Peps.python.org, 5 July 2001, peps.python.org/pep-0008/.
```
```
https://www.conceptdraw.com/How-To-Guide/database-flowchart-symbols
```
```
ChatGPT for error handling
```
## R4
Provide link to GitHub Repository
https://github.com/Venitak2004/Venita_Kissell_T1A3

## R5
### Pep 8
Is the Python style guide for writing code I has a set of guidlines that help to improve readability and consistency. 
For example use 4 spaces when indeting, never use TABS.
Maximum line lengths of characters is 79 characters. 
When importing files they should be listed on separate lines and not combined on the same line. 
Imports have a heirarchy and should be imported in the following order standard libarary imports/related third-party imports/local appliation imports. 
The use of blank lines and space to make code easier to read.
However large amounts of white space is to be avoided. 
Comments should be complete sentences so it is easier for others to read your code better.
With naming conventions function names should be lowercase as are Variables, but Classes begin with a capital letter.
'Single Quotes' for small strings, and "Double Quotes" for strings that contain 'quotes'
'self' is always the first argument.
```
Reference - 
van Rossum, Guido, et al. “PEP 8 – Style Guide for Python Code.” Peps.python.org, 5 July 2001, peps.python.org/pep-0008/.

```

### Python Rich 
A library for rendering and formatting text outputs and visualisation in the terminal window. It supports features that make the terminal window interface more visually appealing with enhanced aesthetics, it supports bold, italics, underline, and strike through text, enhanced colours and more.

```
Python, Real. “The Python Rich Package: Unleash the Power of Console Text – Real Python.” Realpython.com, realpython.com/python-rich-package/.
```

## R6
### Player Database
Developing a player database for a sports club involves defining features that will support the clubs various aspects and requirements, this application has been designed for player data storage, specifically to keep all player data in one database..
The Player Database is designed to be a simple tool for managing player information. It is designed to be easy to use and can be customised to suit clubs needs for the storage of player data.
The features have been designed around ease of usability, this is a basic model, but can be enhanced depending on sports clubs needs and requirements.
We begin by creating the Player class encapsulate the data, from there we add specific functions with are listed below in each feature.

The features are as follows;

#### Player Data Input
- The program starts with a simple input funcion where the user is prompted to input a players details, it will step the user through all required fields to fill the database and store basic data for each player. Data fields (attributes) for this program are first name, last name, unique FFA_id number, team allocation, mobile number, and email address. The save_players function was created to store the data by linking to the csv file. The add_player function was created to append the player information to the csv file storing the objects on each iteration in separate rows.

#### Update or Change Player Details
- This function has been created to assist in making changes to player files, the user can ammend players stored details easily.  The user will be stepped through each required field to ammend, or can simply enter to pass that field if there is no change required in that particular field. The original version enabled the user to search via a last name of a player to change stored data. This posed issues with data integrity, as if there was more than one player with the same last name, changes would be made to all those players. To avoid this happening the search function was changed to require the players unique ffa_id identification number which is a number issued to each player via Football Australia. This was a far better option in respect of maintaining data integrity. The update_player function was created as a for loop, to iterate through the objects, and append the updated information to each attricute in the csv file when saved.

#### Full Player List
- This function enables the user to generate a report of every player listed in the database, this useful function draws all player details from the csv file and displays in the terminal.
To enable this feature the list_player function was created to store the date in its variable. The function loops through every attribute column in the csv file while true displaying each object, until all objects have been retrived from the file.

#### Search for a Specific Player
- This function was designed for easier search function, for example if you didn't know the players stored ffa_id number and you needed to make a change to their stored phone number, the User can input the last name of the player they want to make changes to, and search the database, the search will return the player with the last name that matches the user input. It will also return multiple names if there are multiple matches. This is not an error, and is useful in the instance of families at a sporting club that have more than one child at the club, and the search needs to be able to return all siblings in the search parameter. The list_player function has been created to store the objects in the variable and while true, loop through each attribute and iterate each instance and print to terminal each player that matches the criteria.

### Generate Specific Team List
- This function was designed to give the user the ability to specify a specific team for eg. U16FQ, this will generate for the user a complete list of all players that have been allocated to a certain team, hence returning a complete list of team players. The user at the prompt enters for example U16FQ in the input line and the app will loop through and generate a list with all players matching U16FQ. The find_player function was created and the variable stores the object of the users specific entry, this then for loops through the attributes while true, and iterates each line and prints to the terminal each player that matches the criteria.

### Save
- Save function was designed to save all changes before exiting the app, just another failsafe to protect the data and the changes. The save_player function was designed to store the ojects in the variable until the function is activated. Then it is appended to the csv file.

Exit without Saving
- Exit without saving is a failsafe to ensure data integrity, if an error has been made, the user can exit out of the app, and not save any of the changes. This function breaks out of the program etirely.

### Error Handling
Error handling has been installed in every feature, in activly prompts the user to either
- select a valid number
- check for spelling errors
- player not in database
- exiting without saving

#### Features
The initial display has been spaced out for better aesthetics and readability, the design has been enhanced with Rich formatting to clearer display the options of the simple but useful features. The user interface prompts the user to make a selection from the list of availble options.
 - Add a Player - will add a new player to the database and save their details in a csv file.
 - Update a Player - will update the exsting details already stored in the csv file, but will append the new data to the existing players data.
 - Full Player List - will give you every player listed in the entire database.
 - Search for a Specific Player - will prompt the user to input a players last name to search the system for a specific player, the system will return either one player or in the case of families, then multiple players, if the player is not in the database, the it will return an error message asking the user to check the spelling as player not found.
 - Generate a Team List - this will generate a team specific list for the user, they just need to put in the team name, for example U16FQ this will give the user an output of all the players listed in the database with U16FQ as the team they are allocated into, generating a full list of players for that team only.
 - Save - The save function will save changes made to player files.
 - Exit Without Saving - in the event the user has made a change and doesn't want to store it in the player file they can exit without saving.


