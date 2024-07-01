import json

def load_players():
    
    try:
        with open('players.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("The file players.json does not exist")
        return[]

    except json.JSONDecodeError:
        print("The file player.json contains invalid JSON:")
        return[]
        
def save_players(players):
    with open('players.json', 'w') as file:
        json.dump(players, file)


#def get_player_lname(last_name):
#    players = load_players()
#    for player in players:
#        if player.get ['lname'] == last_name:
#            return player
#    return None

def main():

#Setting up the list for all the stored data.
    players = load_players()
#Setting up the variable to store the users input.
    selection = 0

#User input selections to loop through options to add player, find player, print a team list, print a full player list, and exit.
    while selection != 5:
        print("\nPlayer Database")
        print("1. Add a Player")
        print("2. Find a Player")
        print("3. Print a team list")
        print("4. Print a full player list")
        print("5. Exit")
        #selection = int(input("Enter your selection:  "))

        try:
            selection = int(input("Make a selection: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")
            continue

#Asking for the user to input the Player data into the database.
        if selection == 1:
            print("Adding a Player")
            lname = input("Enter Players Last Name: ")
            fname = input("Enter Players First Name: ")
            ffa_id = input("Enter Players unique FFA no: ")
            team = input("Enter Player allocated team: ")
            mobile = input("Enter Players contact phone number: ")
            email = input("Enter Players contact email address: ")
            players.append([lname, fname, ffa_id, team, mobile, email])
            save_players(players)

#The user can choose to search for a specific player by searching their last name.
        elif selection == 2:
            print("Search for a Player by Last Name")
            search_name = input("Enter Player Last Name: ")
            d = json.data[search_name]
            for player in players:
                if search_name in players[0]: #finds the player by searching for last name in last name column.
                    print(d)
         
            

#The user can print a full team list based on the team allocation.
        elif selection == 3:
            print("Print a Team list")
            search_name = input("Enter Team name: ")
            for player in players:
                if search_name in players[0] or search_name in players[1] or search_name in players[2] or search_name in players[3] or search_name in players[4] or search_name in players[5]: #finds the team allocation in all columns.
                    print(player)

#The user can print a full player list of everyone in the database.
        elif selection == 4:
            print("Print full Player list")
            for player in players:
                print(player)

#If the user no longer wants to use the application, then they can exit out.   
        elif selection == 5:
            print("Exiting program")
            break

        else:
            print("Invalid selection. Please select a menu number between 1 and 5: ")
    
    print("Program terminated by user.")

# This will call main.py to print.
if __name__ == "__main__":
    main()