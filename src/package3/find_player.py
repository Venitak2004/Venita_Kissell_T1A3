from package1 import Player


from typing import List


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
        print("Player you are searching for is not in the list. Check the spelling and try again. ")
