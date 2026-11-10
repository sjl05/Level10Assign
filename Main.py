"""
Level #10 Assignment
IS 303 – Hilton
Create a Python program that allows a user to explore college football results from
the provided CSV file.
Your program should ask the user which season they would like to analyze. It
should then organize the teams from that season into four categories:
• 10 or more wins
• 8–9 wins
• 6–7 wins
• Fewer than 6 wins
Display the teams in each category clearly for the user. Your program should:
• Read the football data from cfb.csv using Pandas.
• Allow the user to select a season.
• Use a dictionary to organize the teams into the four win categories.
• Use loops and selection to process the teams.
• Let the user know if the requested season is not found.
• Work with any season included in the CSV file.
• Avoid hard-coding the team names or results.
Sample Session:
Enter a season to analyze: 2020
College Football Results for 2020
10 or more wins:
Alabama
Coastal Carolina
BYU
Clemson
Notre Dame
8–9 wins:
App State
Liberty
Louisiana
Army West Point
Cincinnati
...
6–7 wins:
SMU
UTSA
San Jose St.
Oklahoma St.
Georgia
...
Fewer than 6 wins:
Arkansas
Vanderbilt
Kansas
Arizona
...
NOTE: The exact teams displayed will depend on the data in cfb.csv.
Submit your PUBLIC GitHub link through Canvas.
"""
#imports 
import pandas as pd
#global variables
category_dict = {
    "10+":[],
    "8-9":[],
    "6-7":[],
    "6-":[]
}
seasons = []
#functions
def output_season_win_data(swd):
    """Takes the dictionary for categories, prints all appropriate data"""
    print("10+ wins:")
    for team in swd["10+"]:
        print(team)
    print("--------------------")
    print("8-9 wins:")
    for team in swd["8-9"]:
        print(team)
    print("--------------------")
    print("6-7 wins:")
    for team in swd["6-7"]:
        print(team)
    print("--------------------")
    print("Less than 6 wins:")
    for team in swd["6-"]:
        print(team)
    print("--------------------")

#main code block
#get the data from the file
df = pd.read_csv("cfb.csv")
for season in df["Season"]:
    if season not in seasons:
        seasons.append(season)
#Welcome the user
print("Welcome to the Football Analysis tool!")
print("Enter q at any time to quit")
#ask the user for input
while True:
    try:
        user_season = input("Which season would you like data for? ").strip()
        if user_season.lower() == 'q':
            break
        elif int(user_season) in seasons: #only the requested seasons can be accessed (don't hardcode)
            user_season = int(user_season)
            #analyze the data based on user input
            data_for_year = df.loc[df["Season"] == user_season]
            category_dict["10+"].extend(data_for_year.query("Win >= 10")["Team"].tolist())
            category_dict["8-9"].extend(data_for_year.query("Win <= 9 and Win >= 8")["Team"].tolist())
            category_dict["6-7"].extend(data_for_year.query("Win <= 7 and Win >= 6")["Team"].tolist())
            category_dict["6-"].extend(data_for_year.query("Win < 6")["Team"].tolist())
            output_season_win_data(category_dict) #display accordingly (10 or more wins, 8-9 wins, 6-7 wins, less than 6 wins)
        elif int(user_season) not in seasons:
            print("We don't have data for that season.")
        else:
            print("Invalid input, please try again")
        category_dict = {
            "10+":[],
            "8-9":[],
            "6-7":[],
            "6-":[]
        }
    except ValueError:
        print("Please enter the season an an iteger (ex. 2018)\n Otherwise enter 'q' to quit.")
    except:
        print("Something went wrong, please try again")
print("Thank you for using our football analysis tool. Goodbye!")