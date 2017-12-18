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

rows_to_take = []
rows_to_take.append(battle_stats.row_values(2))

for i in range(4, 15):
    rows_to_take.append(battle_stats.row_values(i))
    
rows_to_take.append([])
rows_to_take.append(character_info.row_values(3))

for i in range(21, 27):
    rows_to_take.append(character_info.row_values(i))
    
for i in range(50, 58):
    rows_to_take.append(character_info.row_values(i))
    
rows_to_take.append([])
rows_to_take.append(enemy_stats.row_values(1))

for i in range(19, 25):
    rows_to_take.append(enemy_stats.row_values(i))
    
for i in range(46, 53):
    rows_to_take.append(enemy_stats.row_values(i))

with open('Stats Base.csv', 'wb') as test_file:
    list = rows_to_take
    writer = csv.writer(test_file)
    for row in list:
        row = [s.encode('utf-8') for s in row]
        writer.writerows([row])
