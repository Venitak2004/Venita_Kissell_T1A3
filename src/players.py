import csv
import os
from typing import List

# Defining the Player Class

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

#Define the load_player function to store the data

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
    lname = input("Enter Players Last Name: ")
    fname = input("Enter Players First Name: ")
    ffa_id = input("Enter Players unique FFA Id no (must be 8 numbers): ")
    team = input("Enter Player allocated team: ")
    mobile = input("Enter Players contact phone number: ")
    email = input("Enter Players contact email address: ")
    new_player = Player(lname, fname, ffa_id, team, mobile, email)
    players.append(new_player)
    print(f"New player has been added: {new_player}")

#Define update_player function to search the csv list file and locate the player from the list and loop through to update details.
def update_player(players: List[Player]):
    ffa_id_update = input(
        "Enter players FFA ID number to update player details or hit enter to go back to menu: ")

# Find the player unique FFA Id number that matches the user input and loop through until user input last name is found
    found_player = None
    for player in players:
        if player.ffa_id == ffa_id_update:
            found_player = player
            break
    if found_player:

#Print to screen the following prompts to change details for found player to update csv file.
        print(f"Current details of {found_player.fname} {found_player.lname}")
        print(found_player)

        lname = input(
            f"Change players last name or hit enter to skip to next option: (current last name: {player.lname}): ") or player.lname
        fname = input(
            f"Change players first name or hit enter: (current first name: {player.fname}): ") or player.fname
        team = input(
            f"Change players allocated team or hit enter: (current team: {player.team}): ") or player.team
        mobile = input(
            f"Change players contact mobile number or hit enter: {player.mobile}: ") or player.mobile
        email = input(
            f"Change players email address: {player.email}: ") or player.email
        found_player.lname = lname
        found_player.fname = fname
        found_player.team = team
        found_player.mobile = mobile
        found_player.email = email

        print(
            f"Player details have been updated for {found_player.fname} {found_player.lname}, to save your changes please select 6 from the menu.")
#Error message for player not found in the list.
    else:
        print("Player not found!")

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

#Define the function to find a specific player by their last name.
def find_player(players: List[Player]):
    search_player = input(
        "Enter player last name to find specific player: ").strip().lower()
    found_players = [
        player for player in players if player.lname.lower() == search_player]

    if found_players:
        print(f"Players found with the last name: '{search_player}:")
        for player in found_players:
            print(player)
# if player.lname.lower() == search_player:  ##This code only returned one player from the search input,
# print(f"Player from search: {player}") ##Changed to code to display multiple if any were there.
    else:
#Error message if searched player is not in the csv file.
        print("Player you are searching for is not in the list. ")

#Define team_player function to return a specific list of players that have user input specifics by looping through until found.
def team_player(players: List[Player]):
    search_player = input(
        "Enter team name to output team list: ").strip().lower()
    found_players = [
        player for player in players if player.team.lower() == search_player]

    if found_players:
        print(f"Players found with the team allocation of: '{search_player}:")
        for player in found_players:
            print(player)
# if player.lname.lower() == search_player:  ##This code only returned one player from the search input,
# print(f"Player from search: {player}") ##Changed to code to display multiple if any were there.
    else:
#Error message for team not in the list.
        print("Team you are searching for is not in the list. ")
