# Player Database - Venita_Kissell_T1A3
## Link to Source Control Repository & Screenshot

## GitHub Repository
Provide link to GitHub Repository
https://github.com/Venitak2004/Venita_Kissell_T1A3

![GitHub Respository](/docs/github_repository.png)


### Player Database
Developing a player database for a sports club involves defining features that will support the clubs various aspects and requirements, this application has been designed for player data storage, specifically to keep all player data in one database..
The Player Database is designed to be a simple tool for managing player information. It is designed to be easy to use and can be customised to suit clubs needs for the storage of player data.
The features have been designed around ease of usability, this is a basic model, but can be enhanced depending on sports clubs needs and requirements.
We begin by creating the Player class encapsulate the data, from there we add specific functions with are listed below in each feature.

The features are as follows;

#### Player Data Input
- The program starts with a simple input function where the user is prompted to input a players details, it will step the user through all required fields to fill the database and store basic data for each player. Data fields (attributes) for this program are first name, last name, unique FFA_id number, team allocation, mobile number, and email address. The save_players function was created to store the data by linking to the csv file. The add_player function was created to append the player information to the csv file storing the objects on each iteration in separate rows.

#### Update or Change Player Details
- This function has been created to assist in making changes to player files, the user can amend players stored details easily.  The user will be stepped through each required field to amend, or can simply enter to pass that field if there is no change required in that particular field. The original version enabled the user to search via a last name of a player to change stored data. This posed issues with data integrity, as if there was more than one player with the same last name, changes would be made to all those players. To avoid this happening the search function was changed to require the players unique ffa_id identification number which is a number issued to each player via Football Australia. This was a far better option in respect of maintaining data integrity. The update_player function was created as a for loop, to iterate through the objects, and append the updated information to each attribute in the csv file when saved.

#### Full Player List
- This function enables the user to generate a report of every player listed in the database, this useful function draws all player details from the csv file and displays in the terminal.
To enable this feature the list_player function was created to store the date in its variable. The function loops through every attribute column in the csv file while true displaying each object, until all objects have been retrieved from the file.

#### Search for a Specific Player
- This function was designed for easier search function, for example if you didn't know the players stored ffa_id number and you needed to make a change to their stored phone number, the User can input the last name of the player they want to make changes to, and search the database, the search will return the player with the last name that matches the user input. It will also return multiple names if there are multiple matches. This is not an error, and is useful in the instance of families at a sporting club that have more than one child at the club, and the search needs to be able to return all siblings in the search parameter. The list_player function has been created to store the objects in the variable and while true, loop through each attribute and iterate each instance and print to terminal each player that matches the criteria.

#### Generate Specific Team List
- This function was designed to give the user the ability to specify a specific team for eg. U16FQ, this will generate for the user a complete list of all players that have been allocated to a certain team, hence returning a complete list of team players. The user at the prompt enters for example U16FQ in the input line and the app will loop through and generate a list with all players matching U16FQ. The find_player function was created and the variable stores the object of the users specific entry, this then for loops through the attributes while true, and iterates each line and prints to the terminal each player that matches the criteria.

#### Save
- Save function was designed to save all changes before exiting the app, just another failsafe to protect the data and the changes. The save_player function was designed to store the objects in the variable until the function is activated. Then it is appended to the csv file.

#### Exit without Saving
- Exit without saving is a failsafe to ensure data integrity, if an error has been made, the user can exit out of the app, and not save any of the changes. This function breaks out of the program entirely.

#### Error Handling
Error handling has been installed in every feature, in actively prompts the user to either
- select a valid number
- check for spelling errors
- player not in database
- exiting without saving

### Features
The initial display has been spaced out for better aesthetics and readability, the design has been enhanced with Rich formatting to clearer display the options of the simple but useful features. The user interface prompts the user to make a selection from the list of available options.
 - Add a Player - will add a new player to the database and save their details in a csv file.
 - Update a Player - will update the existing details already stored in the csv file, but will append the new data to the existing players data.
 - Full Player List - will give you every player listed in the entire database.
 - Search for a Specific Player - will prompt the user to input a players last name to search the system for a specific player, the system will return either one player or in the case of families, then multiple players, if the player is not in the database, the it will return an error message asking the user to check the spelling as player not found.
 - Generate a Team List - this will generate a team specific list for the user, they just need to put in the team name, for example U16FQ this will give the user an output of all the players listed in the database with U16FQ as the team they are allocated into, generating a full list of players for that team only.
 - Save - The save function will save changes made to player files.
 - Exit Without Saving - in the event the user has made a change and doesn't want to store it in the player file they can exit without saving.


## Design Help Documentation
Design help documentation - User Manual

### Steps to Install Application
This installation manual will help guide you throught the installation process.

#### System Requirements/Hardware Requirements
All operating systems and harware requirements below will operate with the program application. Some programs have more complex requirements, but this application doesn't require alot of RAM storage or fast CPU.

##### Operating System
You can use either of the following operating systems macOS/Windows/Linux

##### Storage
It is recommended you have a minium of 2GB of storage, to install Python/Virtual Environment/Player Database/CSV File.

##### RAM (Memory)
We recommend about 8GB RAM (Graphisoft.com 2024)

##### CPU processor
Any modern computer contains sufficient operating systems.

##### Internet Connection
You will need to have a stable internet connection when download and installing python and pip packages, Visual Studio Code and or associated libraries. 

##### Dependencies
Rich

#### Installation Steps to Run Player Database Terminal Application

Step 1 - Python
Python is an essential download to run this Player Database program. To do this go to https://www.python.org/downloads/ and follow the download instructions from their website.
![python](/docs/python.png)

Step 2 - Install Visual Studio Code
Visual Studio Code is a text editor and is essential to run this program. Download and istall from the provided link below.
https://code.visualstudio.com/download
![visual_studio_code](/docs/visual_studio.png)

Step 3 - Install pip
Pip is another essential program required to run the Player Database. Follow the link below and follow the download prompts to install.

https://pypi.org/project/pip/

![pip](/docs/pip.png)

First you can check if you already have pip installed by typing into the terminal prompt, see below;

##### for Linux:- 
###### Update package -
```
sudo apt update
```
###### Install Pip-
```
sudo apt install python3-pip
```
###### Verify your installation-
```
pip3 --version
```

##### for MacOS
Open a terminal prompt
###### Install pip
```
python3 -m ensurepip
```
##### Verify your installation-
```
pip3 --version
```

Step 4 - Extract the zip file
If you have followed the neccessary steps above, then your next step is to download the Player_Database from GitHub to do this click this link (https://github.com/Venitak2004/Venita_Kissell_T1A3) to access the terminal application program.

4.1 Open the terminal window, and check that you are currently in the working directory. In the terminal window type in;
```
pwd
```

4.2 You need to be in the {Venita_Kissell_T1A3} directory to do this type the following into the terminal window;
```
cd {Venita_Kissell_T1A3}
```

4.3 Once in the {Venita_Kissell_T1A3} directory then you need to change directory into the src file, to do this type the following into the terminal window;
```
cd src
```

##### Creating a Virtual Environment

Now that you are in the correct folder, you need to create a virtual environment, this will isolate the application and its dependicies. To this type into the terminal window as follows;

###### For Linux
-To install virtual environment; (note: you may need to put sudo before pip)
```
pip install vitualenv
```

-To create virtual environment
```
python3 -m <venv_name>
```

-To activiate the virtual environment
```
source venv/bin/activate
```

-To Deactivate once finished using the application
```
deactivate
```

###### For MacOs
Open the terminal window 

-To install virtual environment; (note: you may need to put sudo before pip)
```
sudo pip install vitualenv
```

-To create virtual environment
```
virtualenv venv
```

-To activiate the virtual environment
```
source venv/bin/activate
```

-To Deactivate once finished using the application
```
deactivate
```
Step 5 - Install required dependencies file (requirement.txt)
The requirements.txt file inside the src folder will need to be installed to utilise the functions.
- Rich
5.1 Installing the requirements.txt file.
In the terminal window, type the following;
```
pip install -r requirements.txt
```

5.2 - Starting the Player_Database application
In the terminal window, type the following;
```
python3 main.py
```

Once all the above steps have been installed and implemented, you can run the executable file. In the terminal window type the following;
```
./player_database.sh

```

##### Overview of the Player_Database features and functions and how to utilise them.

Once you have opened the program you will see a menu for the Player Database System. You have series of menu items to choose from.

![Main Menu](/docs/main-menu.png)

This program application has the following features;

   - Add a New Player
   - Update a Players Current Details
   - Full Player List
   - Search for a Specific Player
   - Generate a Team List
   - Save
   - Exit Without Saving


#### 1. Add a New Player
   This selection will enable you to start processing a player into the database, please have the following details ready;

   ![New Player](/docs/new_player.png)

   Player First Name
   Player Last Name
   Unique FFA id Number (8 numbers)
   Team Allocation
   Phone Number
   Email

   You will require all of the above information to insert into the database, so have them ready.
   Select 1 and press enter.
   The program will prompt you for each entry line to guide you on which line of information to enter.
   Simply type the information you are prompted to type in, the hit enter.
   Once you have completed all the fields you will be sent back to the main menu.

#### 2. Update a Players Current Details

   ![Update Player](/docs/update_player.png)

   This selection will enable you to update an existing player in the database.
   To do this, firstly select menu item 4 and search the database for a specific players using their last name.
   Once you have the players details on the screen, copy the players unique FFA_id number to access this menu function.
   Once back at the main menu, you can now select option 2 from the menu,
   Insert the copied unique FFA_id number into the terminal prompt and follow the prompts to make the changes.
   
   - Firstly you will be asked if you want to change the players first name, if you don't need to make changes to the first name then just press Enter.
   - Then you will be asked if you want to change the players last name, same applies here, if you don't need to make any changes, just press enter to move to the next field.
   - Next you will be asked if you want to change the players Team Allocation, same applies, if you don't need to make any changes, just enter to move to the next field.
   - Then you will be asked if you want to change the players phone number, same applies, if you don't need to make any changes, just enter to move to the next field.
   - Lastly you will be asked if you want to change the players email address, same applies, if you don't need to make any changes, just enter to move to the next field.
   Once you have done all of these steps
   Select Menu option 6 and Save your changes.
   
#### 3. Full Player List

   ![Full Player List](/docs/full_player_list.png)

   This menu option will give you a full list of players from the database, everything stored in the database is going to be printed to the display screen.
   Simply select Menu option 3 and hit enter.
   You will see on the display screen all players currently stored in the database.

#### 4. Search for a Specific Player

   ![Search Player](/docs/new_player.png)
   
   This menu option will search for a specific player.
   Select menu item 5 and hit enter
   The program will prompt you to input the players last name and hit enter.
   You will see on the screen all player with the same last name will appear (this is useful when you have more than one player with the same last name, but are all from the same family).
   
#### 5. Generate a Team List
   
   ![Generate Team List](/docs/generate_team_list.png)
   
   This menu option will give you a specific list of players in a specific team.
   Select menu item 6 and hit enter
   You will be prompted to input a team name, for example team name may be U16FQ.
   Enter the team name and hit enter.
   You will see on the screen all players allocated to the team you input in the search field.
 

#### 6. Save

   ![Save](/docs/Save.png)

   This menu option will save all changes you have made to the player files.
   Simply select 6 from the menu and hit enter
   You will be notified that your files have been saved.

#### 7. Exit with No Save

   ![Exit](/docs/Exit_no_save.png)

   This menu option will exit the program completely and not save your changes.
   When you want to exit the program make sure you have first saved your changes by selecting menu item 6 and hit enter.
   Then you can select menu item 7 and hit enter.
   This will close the program.


## Error Handling

#### Menu Item 2 - Update Player - Error Message

   ![Error Update Player](/docs/Error_update_player_not_found.png) 

"Player not found"
The program is telling you that the player you are searching for is not in the database, either select menu option 2 and search for the player by their last name, or select menu option 3 and run a full player list, and get the correct FFA_id number, and try again.

#### Menu Item 3 - Full Team List - Error Message
"There are no players in this list"
The program is telling you that there are no players in the database, so you will need to enter players details to populate the database.

#### Menu Item 4 - Search a Specific Player - Error Message

![Error Player Not Found](/docs/Error_player_not_found.png)

"Player you are looking for is not in the list."
The program is telling you that it can not find the player, if you are certain the player is in the database, run menu option 3 and run a full player list check the player details, there may be a spelling error in the last name.

#### Menu Item 6 - Generate a Team List - Error Message

 ![Error Team List](/docs/error_team_list.png)

"Team you are searching for is not in the list"
The program is telling you that the team is not in the list, this could be that there are no allocated players to this team at present, or the players for this specific team have not been loaded into the system yet or have been allocated to another team. To check if the players are in the system, select menu option 3 and run full player list. Once you have the players FFA_id number you can change their team allocation.

### Algorithmic Walk through - Flow chart

 ![Flow Chart](/docs/flowchart_playerdatabase.png)

### Project Management Platform (Implementation Plan)
![trello_board](/docs/R7_trello_board.png)
![trello card 1](/docs/trello_board_eg1.png)
![trello card 2](/docs/trello_board_eg2.png)



### Pep8
Is the Python style guide for writing code I has a set of guidelines that help to improve readability and consistency. 
For example use 4 spaces when indenting, never use TABS.
Maximum line lengths of characters is 79 characters. 
When importing files they should be listed on separate lines and not combined on the same line. 
Imports have a hierarchy and should be imported in the following order standard library imports/related third-party imports/local application imports. 
The use of blank lines and space to make code easier to read.
However large amounts of white space is to be avoided. 
Comments should be complete sentences so it is easier for others to read your code better.
With naming conventions function names should be lowercase as are Variables, but Classes begin with a capital letter.
'Single Quotes' for small strings, and "Double Quotes" for strings that contain 'quotes'
'self' is always the first argument.

![autopep8](/docs/autopep8.png)
```
Reference - 
van Rossum, Guido, et al. “PEP 8 – Style Guide for Python Code.” Peps.python.org, 5 July 2001, peps.python.org/pep-0008/.

```

### Python Rich 
A library for rendering and formatting text outputs and visualisation in the terminal window. It supports features that make the terminal window interface more visually appealing with enhanced aesthetics, it supports bold, italics, underline, and strike through text, enhanced colours and more.

```
Python, Real. “The Python Rich Package: Unleash the Power of Console Text – Real Python.” Realpython.com, realpython.com/python-rich-package/.
```


### References 
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
“System Requirements.” Graphisoft, graphisoft.com/resources-and-support/system-requirements.
```

```
ChatGPT for error handling
```
