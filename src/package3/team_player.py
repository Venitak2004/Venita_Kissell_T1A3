from package1 import Player 

from typing import List



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
