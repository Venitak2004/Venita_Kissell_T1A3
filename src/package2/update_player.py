from package1 import Player


from typing import List

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