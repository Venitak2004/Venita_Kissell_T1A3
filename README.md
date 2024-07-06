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
Pep 8 is the Python style guide for writing code I has a set of guidlines that help to improve readability and consistency. 
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
## R6
# Player Database
Developing a player database for a sports club involves defining features that will support the clubs various aspects and requirements, this application has been designed for player data storage, specifically to keep all player data in one database.
The Player Database is designed to be a simple tool for managing player information. It is designed to be easy to use and can be customised to suit clubs needs for the storage of player data.
Player Data Input
- Input and store basic data for each player, first name, last name, unique FFA_id number, team allocation, mobile number, and email address.

Update or Change Player Details
- User can ammend players stored details, you must use their stored unique FFA_id number to make changes to the players information, simply by going through each stored column and simply changing the data that needs to be altered, and saving at the end.

Full Player List
- Generates a report of every player listed in the database.

Search for a Specific Player
- User can input the last name of the player they want to search the database for, it will return multiple names if there are multiple matches. This being because families have more than one child at a club, and may need to return all siblings in the search.

Generate Specific Team List
- The database can return to the user team specific team list. The user at the prompt enters for example U16FQ in the input line and the app will loop through and generate a list with all players matching U16FQ.

Save
- Save function is designed to save all changes before exiting the app, just another failsafe to protect the data and the changes.

Exit without Saving
- Exit without saving is a failsafe to ensure data integrity, if an error has been made, the user can exit out of the app, and not save any of the changes.
## Features
The initial display has been spaced out for better aesthetics and readability, with simple but useful features. The user just needs to make a selection from the list of options.
 - Add a Player - will add a new player to the database and save their details in a csv file.
 - Update a Player - will update the exsting details already stored in the csv file, but will append the new data to the existing players data.
 - Full Player List - will give you every player listed in the entire database.
 - Search for a Specific Player - will prompt the user to input a players last name to search the system for a specific player, the system will return either one player or in the case of families, then multiple players, if the player is not in the database, the it will return an error message asking the user to check the spelling as player not found.
 - Generate a Team List - this will generate a team specific list for the user, they just need to put in the team name, for example U16FQ this will give the user an output of all the players listed in the database with U16FQ as the team they are allocated into, generating a full list of players for that team only.
 - Save - The save function will save changes made to player files.
 - Exit Without Saving - in the event the user has made a change and doesn't want to store it in the player file they can exit without saving.


