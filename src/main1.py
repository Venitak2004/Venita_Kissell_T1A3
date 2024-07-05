from players import load_players, save_players, add_players, update_player, list_players, find_player, team_player



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
        print("3. Full Player List")
        print("4. Search for a Specific Player")
        print("5. Generate a Team List, Select Team Name ")
        print("6. Save")
        print("7. Exit Without Saving")
        print("  ")
        print("------------------------------------")

        select = input("Enter your selection: ")
        print("  ")

        if select == '1':    #If the user selects 1, then access the add_player function usint the players variable to store the input data.
            add_players(players)
        elif select == '2':
            update_player(players)
        elif select == '3':
            list_players(players)
        elif select == '4':
            find_player(players)
        elif select == '5':
            print("Insert Team Name eg. U16FQ ")
            team_player(players)
        elif select == '6':
            save_players(filename, players)
            print("Players details have been saved to the database.")
            #break
        elif select == '7':
            print("Caution you will exit without saving your files.")
            break
        else:
            print("Invalid selection. Please select an option between 1 and 7")




if __name__ == "__main__":
    main()
