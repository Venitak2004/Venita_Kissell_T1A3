
from rich.console import Console
from players import load_players, save_players, add_players, update_player, list_players, find_player, team_player

#Initialise
console = Console()

#Main function for the program
def main():

#imprting the csv file from players.csv
    filename = 'players.csv'
    players = load_players(filename)

#User interface
    while True:
        console.print(" [bold blue]------------------------------------[/bold blue]")
        console.print("  [bold cyan]     Player Database System [/bold cyan]")
        console.print(" [bold blue]------------------------------------[/bold blue]")
        print("  ")
        print("1. Add a New Player")
        print("2. Update a Players Current Details")
        print("3. Full Player List")
        print("4. Search for a Specific Player")
        print("5. Generate a Team List, Select Team Name ")
        print("6. Save")
        console.print("[bold red]7. Exit Without Saving[/bold red]")
        print("  ")
        console.print(" [bold blue]------------------------------------[/bold blue]")

        select = console.input("[bold yellow]Enter your selection: [/bold yellow]")
        print("  ")

        if select == '1':    #If the user selects 1, then access the add_player function using the players variable to store the object.
            add_players(players)
        elif select == '2':  #If the user selects 2, then upate the object and store until saved in the variable.
            update_player(players)
        elif select == '3':  #If the user selects 3, then display the full list of all objects in the class.
            list_players(players)
        elif select == '4':  #If the user selects 4, then search the class for the user input and output to the terminal the specific object.
            find_player(players)
        elif select == '5':  #If the user selects 5, then search the class for the user input and output to the terminal the specific objects. 
            print("Insert Team Name eg. U16FQ ")
            team_player(players)
        elif select == '6':  #If the user selects 6, then save all append the entries to the class.
            save_players(filename, players)
            print("Players details have been saved to the database.")
            continue   #removed the break as I didn't want to exit the code after saving.
        elif select == '7':  #If the user selects 7, then break out to the program and don't save to the class.
            print("You have exited without saving your files.")
            break
        else:                #Error Handling for acceptable values.
            print("Invalid selection. Please select an option between 1 and 7")




if __name__ == "__main__":
    main()
