from flask import Flask, url_for, render_template
import csv

app = Flask(__name__)

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
    
    columns, rows = translate(column_letter, row_number)
    
    
convoy_rows = []
with open('static/convoy.csv', 'rb') as csvfile2:
    rowreader2 = csv.reader(csvfile2)
    rowreader2.next()
    for row in rowreader2:
        convoy_rows.append(row)
    

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/convoy')
def show_convoy():
    return render_template( 'convoy.html',
                            ROWS=convoy_rows)
    
@app.route('/shop')
def show_shop():
    return 'Anna is opening up shop soon. Please wait a while.'
    
@app.route('/map')
def show_map():
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
                            column=columns)
    
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, we don't have a page like that here."