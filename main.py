def main():

#Setting up the list for all the stored data.
    players = []
#Setting up the variable to store the users input.
    selection = 0

#User input selections to loop through options to add player, find player, print a team list, print a full player list, and exit.
    while selection != 5:
        print("Player Database")
        print("1. Add a Player")
        print("2. Find a Player")
        print("3. Print a team list")
        print("4. Print a full player list")
        print("4. Exit")
        selection = int(input())

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
