import csv
import os
from typing import List

#Defining the Player Class
class Player:
    def __init__(self, lname: str, fname: str, ffa_id: str, team: str, mobile: str, email: str):
        self.lname = lname
        self.fname = fname
        self.ffa_id = ffa_id
        self.team = team
        self.mobile = mobile
        self.email = email

    def __str__(self):
        return f"{self.lname}, {self.fname}, FFA_ID: {self.ffa_id}, Team: {self.team}, Mobile: {self.mobile}, Email: {self.email}"

def load_players(filename: str) -> List[Player]:
        players = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    player = Player(
                        lname = row['lname'],
                        fname = row['fname'],
                        ffa_id = row['ffa_id'],
                        team = row['team'],
                        mobile = row['mobile'],
                        email = row['email']
                        )
                    players.append(player)
        return players

def save_players(filename: str, players: List[Player]):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['lname', 'fname', 'ffa_id', 'team', 'mobile', 'email'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for player in players:
            writer.writerow({
                'lname': player.lname,
                'fname': player.fname,
                'ffa_id': player.ffa_id,
                'team': player.team,
                "mobile": player.mobile,
                "email": player.email
            })

def add_players(players: List[Player]):
    lname = input("Enter Players Last Name: ")
    fname = input("Enter Players First Name: ")
    ffa_id = input("Enter Players unique FFA no: ")
    team = input("Enter Player allocated team: ")
    mobile = input("Enter Players contact phone number: ")
    email = input("Enter Players contact email address: ")
    new_player = Player(lname, fname, ffa_id, team, mobile, email)
    players.append(new_player)
    print(f"New player has been added: {new_player}")

def update_player(players: List[Player]):
    ffa_id_update = input("Enter players FFA ID no to update player details: ")
    for player in players:
        print(f"curret details of {player}")
        lname = input(f"Change players last name: (current last name: {player.lname}): ") or player.lname
        fname = input(f"Change players first name: (current first name: {player.fname}): ") or player.fname
        team = input(f"Change players allocated team: (current team: {player.team}): ") or player.team
        mobile = input(f"Change players contact mobile number: {player.mobile}: ") or player.mobile
        email = input(f"Change players email address: {player.email}: ") or player.email
        player.lname = lname
        player.fname = fname
        player.team = team
        player.mobile = mobile
        player.email = email
        print(f"Player details have been updated for {player}")
        return
    print("Player selection as not found!")

def list_players(players: List[Player]):
    if players:
      print("n\Total Player List")
      for player in players:
        print(player)
    else:
       print("There are no players in this list. ")

def find_player(players: List[Player]):
    search_player = input("Enter player lname to find player: ")
    for player in players:
        if player.lname == search_player:
            print(f"Player from search: {player}")
            return
    print("Player you are searching for is not in the list. ")

def main():
   
    filename = 'players.csv'
    players = load_players(filename)

    while True:
        print("n\Player Database System")
        print("1. Add a New Player")
        print("2. Update a Players Current Details")
        print("3. Full Player list")
        print("4. Search for a specific Player")
        print("5. Save and Exit Database")
        print("6. Exit without saving")

        select = input("n\Enter your selection: ")

        if select == '1':
          add_players(players)
        elif select == '2':
            update_player(players)
        elif select == '3':
            list_players(players)
        elif select =='4':
            find_player(players)
        elif select == '5':
            save_players(filename, players)
            print("Players details have been saved to the database.")
            break
        elif select == '6':
            print("Caution you will exit without saving your files.")
            break
        else:
            print("Invalid selection. Please select an option between 1 and 6")


#Setting up the list for all the stored data to load from the Json data file.
    #players = []
#Setting up the variable to store the users input.
    #selection = 0

#User input selections to loop through options to add player, find player, print a team list, print a full player list, and exit.
    #while selection != 5:
    #    print("\nPlayer Database")
    #    print("1. Add a Player")
    #    print("2. Find a Player")
    #    print("3. Print a team list")
    #    print("4. Print a full player list")
    #    print("5. Exit")
        #selection = int(input("Enter your selection:  "))

    #    try:
    #        selection = int(input("Make a selection: "))
    #    except ValueError:
    #        print("Please enter a valid number between 1 and 5")
    #        continue

#Asking for the user to input the Player data into the database.
    #    if selection == 1:
    #        print("Adding a Player")
    #        lname = input("Enter Players Last Name: ")
    #        fname = input("Enter Players First Name: ")
    #        ffa_id = input("Enter Players unique FFA no: ")
    #        team = input("Enter Player allocated team: ")
    #        mobile = input("Enter Players contact phone number: ")
    #        email = input("Enter Players contact email address: ")
    #        players.append([lname, fname, ffa_id, team, mobile, email])
           
#The user can choose to search for a specific player by searching their last name.
    #    elif selection == 2:
    #         print("Searching for a player")
    #         search_name = input("Enter either player first or last name: ")
    #         for team in players:
    #            if search_name in player[0] or search_name in player[1] or search_name in player[2] or search_name in player[3] or search_name in player[4] or search_name in player[5]: #finds the player last name in all columns.
    #                print(player)
                               

#The user can print a full team list based on the team allocation.
    #    elif selection == 3:
    #        print("Print a Team list")
    #        search_team = input("Enter Team name: ")
    #        for player in players:
    #            if search_team in player[0] or search_team in player[1] or search_team in player[2] or search_team in player[3] or search_team in player[4] or search_team in player[5]: #finds the team allocation in all columns.
    #                print(player)

#The user can print a full player list of everyone in the database.
    #    elif selection == 4:
    #        print("Print full Player list")
    #        for player in players:
    #            print(player)

#If the user no longer wants to use the application, then they can exit out.   
    #    elif selection == 5:
    #        print("Exiting program")
    #        break

    #    else:
    #        print("Your selection is not valid. Please select a menu number between 1 and 5: ")
    
    #print("Program terminated by the user.")

# This will call main.py to print.
if __name__ == "__main__":
    main()