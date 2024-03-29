import json
import os
import csv
from datetime import datetime

fileJSON = open("Basketball_women2.json")
data = json.load(fileJSON)

players_field_names = ["_id", "firstName", "middleName", "lastName", "fullGivenName", "nameNick", "pos", "height","weight", "college", "birthDate", "birthCity", "birthCountry", "highSchool" , "hsCity" , "hsState", "hsCountry"]
teams_field_names = ["_id","year","tmID", "games","minutes","points","steals","blocks"]
awards_field_names = ["_id","award", "year" , "pos"]
players_teams_dict = []
awards_players_dict = []

for element in data:
    player_id = element['_id']
    # Check if 'players_teams' array is not empty
    if element.get('players_teams'):
        for entry in element['players_teams']:
            entry_with_id = {'_id' : element['_id']}
            entry_with_id.update(entry)
            players_teams_dict.append(entry_with_id)
    element.pop('players_teams')

    # Check if 'awards_players' array is not empty
    if element.get('awards_players'):
        for entry in element['awards_players']:
            entry_with_id = {'_id' : element['_id']}
            entry_with_id.update(entry)
            awards_players_dict.append(entry_with_id)
    element.pop('awards_players')

    if element['birthDate'] == '0000-00-00':
        # Replace with a default date or exclude the entry, as needed
        element['birthDate'] = '1789-07-14'
    else:
        # Convert 'birthDate' to a datetime object
        element['birthDate'] = datetime.strptime(element['birthDate'], '%Y-%m-%d').date()


with open('Players.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=players_field_names,extrasaction='ignore')
    writer.writeheader()
    writer.writerows(data)

with open('Teams.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=teams_field_names,extrasaction='ignore')
    writer.writeheader()
    writer.writerows(players_teams_dict)

with open('Awards.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=awards_field_names,extrasaction='ignore')
    writer.writeheader()
    writer.writerows(awards_players_dict)