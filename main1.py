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
    ffa_id = input("Enter Players unique FFA Id no (must be 8 numbers): ")
    team = input("Enter Player allocated team: ")
    mobile = input("Enter Players contact phone number: ")
    email = input("Enter Players contact email address: ")
    new_player = Player(lname, fname, ffa_id, team, mobile, email)
    players.append(new_player)
    print(f"New player has been added: {new_player}")


def update_player(players: List[Player]):
    ffa_id_update = input(
        "Enter players FFA ID number to update player details or hit enter to go back to menu: ")

    # Find the player whos FFA Id number matches the selection.
    found_player = None
    for player in players:
        if player.ffa_id == ffa_id_update:
            found_player = player
            break
    if found_player:

        print(f"Current details of {found_player.fname} {found_player.lname}")
        print(found_player)

        lname = input(
            f"Change players last name or hit enter to skip to next option: (current last name: {player.lname}): ") or player.lname
        fname = input(
            f"Change players first name: (current first name: {player.fname}): ") or player.fname
        team = input(
            f"Change players allocated team: (current team: {player.team}): ") or player.team
        mobile = input(
            f"Change players contact mobile number: {player.mobile}: ") or player.mobile
        email = input(
            f"Change players email address: {player.email}: ") or player.email
        found_player.lname = lname
        found_player.fname = fname
        found_player.team = team
        found_player.mobile = mobile
        found_player.email = email

        print(
            f"Player details have been updated for {found_player.fname} {found_player.lname}")

    else:
        print("Player not found!")


def list_players(players: List[Player]):
    if players:
        print("Total Player List")
        print(" ")
        for player in players:
            print(player)
    else:
        print("There are no players in this list. ")


def find_player(players: List[Player]):
    search_player = input(
        "Enter player lname to find player: ").strip().lower()
    found_players = [
        player for player in players if player.lname.lower() == search_player]

    if found_players:
        print(f"Players found with the last name: '{search_player}:")
        for player in found_players:
            print(player)
            # if player.lname.lower() == search_player:  ##This code only returned one player from the search input,
        # print(f"Player from search: {player}") ##Changed to code to display multiple if any were there.
    else:
        print("Player you are searching for is not in the list. ")


def team_player(players: List[Player]):
    search_player = input(
        "Enter team name to output team list: ").strip().lower()
    found_players = [
        player for player in players if player.team.lower() == search_player]

    if found_players:
        print(f"Players found with the team allication of: '{search_player}:")
        for player in found_players:
            print(player)
            # if player.lname.lower() == search_player:  ##This code only returned one player from the search input,
        # print(f"Player from search: {player}") ##Changed to code to display multiple if any were there.
    else:
        print("Team you are searching for is not in the list. ")


def main():

    filename = 'players.csv'
    players = load_players(filename)

    while True:
        print("------------------------------------")
        print("      Player Database System")
        print("------------------------------------")
        print("  ")
        print("1. Add a New Player")
        print("2. Update a Players Current Details")
        print("3. Full Player list")
        print("4. Search for a specific Player")
        print("5. Generate a team list, select team name: ")
        print("6. Save and Exit Database")
        print("7. Exit without saving")
        print("  ")
        print("------------------------------------")

        select = input("Enter your selection: ")
        print("  ")

        if select == '1':
            add_players(players)
        elif select == '2':
            update_player(players)
        elif select == '3':
            list_players(players)
        elif select == '4':
            find_player(players)
        elif select == '5':
            team_player(players)
        elif select == '6':
            save_players(filename, players)
            print("Players details have been saved to the database.")
            break
        elif select == '7':
            print("Caution you will exit without saving your files.")
            break
        else:
            print("Invalid selection. Please select an option between 1 and 7")




if __name__ == "__main__":
    main()
