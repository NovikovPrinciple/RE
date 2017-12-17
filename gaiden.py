from flask import Flask, url_for, render_template
import csv

column_translate = {   
                    'A':55,
                    'B':105,
                    'C':155,
                    'D':205,
                    'E':255,
                    'F':305,
                    'G':355,
                    'H':405,
                    'I':455,
                    'J':505,
                    'K':555,
                    'L':605,
                    'M':655,
                    'N':705,
                    'O':755,
                    'P':805,
                    'Q':855,
                    'R':905,
                    'S':955,
                    'T':1005,
                    'U':1055,
                    'V':1105,
                    'W':1155,
                    'X':1205,
                    'Y':1255,
                    'Z':1305,
                    'AA':1355
                    
                }
row_translate = {
                    '1':55,
                    '2':105,
                    '3':155,
                    '4':205,
                    '5':255,
                    '6':305,
                    '7':355,
                    '8':405,
                    '9':455,
                    '10':505,
                    '11':555,
                    '12':605,
                    '13':655,
                    '14':705,
                    '15':755,
                    '16':805,
                    '17':855,
                    '18':905,
                    '19':955,
                    '20':1005,
                    '21':1055,
                    '22':1105,
                    '23':1155,
                    '24':1205
                }

name_list = []
column_letter = []
row_number = []
Max = []
Current = []
Strength = []
Magic = []
Skill = []
Speed = []
Luck = []
Defense = []
Resistance = []
Movement = []
sprite_list = []
Equipped = []
Item_uses = []
Atk = []
Hit = []
Crit = []
Avo = []
CEva = []
Skills = []

def translate(columns, rows):
    for i in range(0, len(columns)):
        columns[i] = column_translate[columns[i]]
        
    for i in range(0, len(rows)):
        rows[i] = row_translate[rows[i]]
        
    return columns, rows
    
    
with open('static/stats1-1.csv', 'rb') as csvfile:
    rowreader = csv.reader(csvfile)
    for row in rowreader:
        if row[12] == '' or row[12] == 'Column':
            continue
            
        name_list.append(row[0])
        sprite_list.append(row[1] + '.gif')
        Max.append(row[2])
        Current.append(row[3])
        Strength.append(row[4])
        Magic.append(row[5])
        Skill.append(row[6])
        Speed.append(row[7])
        Luck.append(row[8])
        Defense.append(row[9])
        Resistance.append(row[10])
        Movement.append(row[11])
        column_letter.append(row[12])
        row_number.append(row[13])
        Equipped.append(row[14])
        Item_uses.append(row[15])
        Atk.append(row[16])
        Hit.append(row[17])
        Crit.append(row[18])
        Avo.append(row[19])
        CEva.append(row[20])
        Skills.append(tuple(row[21:28]))
    
    columns, rows = translate(column_letter, row_number)

 
@gaiden.route('/gaiden')
def show_gaiden():
    return render_template( 'map.html', 
                            map='Extra rescaled.png',
                            character_list=name_list,
                            sprite=sprite_list,
                            MAX=Max,
                            CURRENT=Current,
                            STRENGTH=Strength,
                            MAGIC=Magic,
                            SKILL=Skill,
                            SPEED=Speed,
                            LUCK=Luck,
                            DEFENSE=Defense,
                            RESISTANCE=Resistance,
                            MOVE=Movement,
                            row=rows,
                            column=columns,
                            USES=Item_uses,
                            ATK=Atk,
                            HIT=Hit,
                            CRIT=Crit,
                            AVO=Avo,
                            CEVA=CEva,
                            EQUIPPED=Equipped,
                            SKILLS=Skills)