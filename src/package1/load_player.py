
import csv
import os.path
from typing import List
from rich.console import Console
#from players import load_players, save_players, add_players, update_player, list_players, find_player, team_player

#Initialise
console = Console()

# Defining the Player Class

class Player:
    def __init__(self, lname: str, fname: str, ffa_id: str, team: str, mobile: str, email: str):
        #if not lname or not fname or not ffa_id or not team or not mobile or not email:
            #raise ValueError("All fields must have an entry. ")
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
                    lname=row['lname'],
                    fname=row['fname'],
                    ffa_id=row['ffa_id'],
                    team=row['team'],
                    mobile=row['mobile'],
                    email=row['email']
                )
                players.append(player)
    return players


#Define the save_player function to save the player details to write to the csv file
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

#Define the add_player function to add new players to the csv file and write to the file
def add_players(players: List[Player]):
    while True:
        lname = input("Enter Players Last Name: ")
        fname = input("Enter Players First Name: ")
        ffa_id = input("Enter Players unique FFA Id no (must be 8 numbers): ")
        team = input("Enter Player allocated team: ")
        mobile = input("Enter Players contact phone number: ")
        email = input("Enter Players contact email address: ")
        new_player = Player(lname, fname, ffa_id, team, mobile, email)
        players.append(new_player)
        console.print(f"New player has been added, make sure you [bold magenta]Save[/bold magenta] select 6. in the menu to save to add to the Database. {new_player}")
        break


from typing import List


#Define the function for displaying a full list of players in the csv file database.
def list_players(players: List[Player]):
    if players:
        print("Complete Player List")
        print(" ")
        for player in players:
            print(player)
    else:
 #Error message for no players in the list.       
        print("There are no players in this list. ")

 
