import constants
import copy

teams_copy = copy.deepcopy(constants.TEAMS)
team_1 = []
team_2 = []
team_3 = []

# Function for cleaning data
def clean_data():
    cleaned = []
    for player in constants.PLAYERS:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = player['height'].split(" ")[0]
        fixed['height'] = int(fixed['height'])
        cleaned.append(fixed)
    return cleaned
roster = clean_data()

# Function for adding players and team balancing
def create_teams():

    exp_players = [n for n in roster if n['experience'] == True]
    nexp_players = [n for n in roster if n['experience'] == False]

    while exp_players:
        team_1.append(exp_players.pop())
        team_2.append(exp_players.pop())
        team_3.append(exp_players.pop())

    while nexp_players:
        team_1.append(nexp_players.pop())
        team_2.append(nexp_players.pop())
        team_3.append(nexp_players.pop())
    return team_1, team_2, team_3


# team_1 = sorted(team_1, key=lambda k: k['height'])
# team_2 = sorted(team_2, key=lambda k: k['height'])
# team_3 = sorted(team_3, key=lambda k: k['height'])
 


# Function for start-up menu or welcome message
def welcome_menu():
    print("\nWelcome to Team Treehouse's Project #2: Basketball Team Stats Tool")

    while True:
        print("\n\n--- MAIN MENU ---\n\nPlease make a selection below:\n\n1) Display team stats.\n2) Exit the program.")
        try:
            welcome_select = int(input("\n"))
            if welcome_select == 1:
                team_menu()
            elif welcome_select == 2:
                print("\nSorry to hear that. Take care!\n")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("That's not a valid option. Please enter either 1 or 2.")
            continue

# Function for selecting team
def team_menu():
      
    while True:
        print(f"\nChoose an available team to view:\n\n1) {teams_copy[0]} \n2) {teams_copy[1]} \n3) {teams_copy[2]}\n")
        try:
            team_select = int(input(""))
            if team_select == 1:
                create_stats('Panthers', team_1)
                input("Press 'Enter' to continue...")
                welcome_menu()
            elif team_select == 2:
                create_stats('Bandits', team_2)
                input("Press 'Enter' to continue...")
                welcome_menu()
            elif team_select == 3:
                create_stats('Warriors', team_3)
                input("Press 'Enter' to continue...")
                welcome_menu()
            else:
                raise ValueError
        except ValueError:
            print("That's not a valid option. Try selecting an available team.")
            continue

# Function for sorting team players by height ascending, total players, total exp players, total inexp players, average height of players, player names, and guardian names
def create_stats(arg_1, arg_2):
   
    arg_2 = sorted(arg_2, key=lambda k: k['height'])

    total = 0
    for index in arg_2:
        var = index['height']
        total = total + var
        avg_height = total / len(arg_2)

    player_list = [n['name'] for n in arg_2]
    player_list = ', '.join(player_list)

    guard_list = [n['guardians'] for n in arg_2]
    guard_list = [', '.join(n) for n in guard_list]
    guard_list = ', '.join(guard_list)
 
    print(f"""
You selected the {arg_1}!\n
Total Players = {len(arg_2)}
Experienced Players: {(len([index['experience'] for index in arg_2 if index['experience'] == True]))}
Inexperienced Players: {(len([index['experience'] for index in arg_2 if index['experience'] == False]))}
Average Height: {round(avg_height)}

Players: {player_list}

Guardians: {guard_list}
    """)

if __name__ == '__main__':
    create_teams()
    welcome_menu()