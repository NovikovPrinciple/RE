import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import csv

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('RE:Team O')
battle_stats = sheet.worksheet("Battle Stats")
character_info = sheet.worksheet("Character Info")
enemy_stats = sheet.worksheet("Enemy Stats")
skill_list = sheet.worksheet("Skill List")
terrain = sheet.worksheet("Terrain")

'''
# Gather skills
rows_to_take = []
for i in range(2, 168):
    rows_to_take.append(skill_list.row_values(i))

with open('Skill List.csv', 'wb') as skill_file:
    list = rows_to_take
    writer = csv.writer(skill_file)
    for row in list:
        row = [s.encode('utf-8') for s in row]
        writer.writerows([row])


#gather Terrain        
rows_to_take = []
for i in range(1, 10):
    rows_to_take.append(terrain.row_values(i))
    
with open('Terrain and Unit Types', 'wb') as terrain_file:
    list = rows_to_take
    writer = csv.writer(terrain_file)
    for row in list:
        row = [s.encode('utf-8') for s in row]
        writer.writerows([row])
       

#gather Character bases        
rows_to_take = []
rows_to_take.append(character_info.row_values(1))       #user
rows_to_take.append(character_info.row_values(3))       #character
rows_to_take.append(character_info.row_values(5))       #class
rows_to_take.append(character_info.row_values(9))       #level
rows_to_take.append(character_info.row_values(19))      #move
rows_to_take.append(character_info.row_values(28))      #ore
for i in range(11, 19):                                 #stats
    rows_to_take.append(character_info.row_values(i))
for i in range(50, 58):                                 #skills
    rows_to_take.append(character_info.row_values(i))
for i in range(21, 27):                                 #items
    rows_to_take.append(character_info.row_values(i))
    
with open('Character Stats and Inventory.csv', 'wb') as character_file:
    list = rows_to_take
    writer = csv.writer(character_file)
    for row in list:
        row = [s.encode('utf-8') for s in row]
        writer.writerows([row])
'''