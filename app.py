from flask import Flask, url_for, render_template
import csv

app = Flask(__name__)

column_translate = {   
                    'A':55,
                    'B':105,
                    'F':305,
                    'G':355,
                    'H':405,
                    'Q':855,
                    'S':955
                }
row_translate = {
                    '1':65,
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
                    '22':1105
                }

Strength=[1,2,3]
name_list = []
column_letter = []
row_number = []
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
        print row
        name_list.append(row[0])
        column_letter.append(row[12])
        row_number.append(row[13])
    
    columns, rows = translate(column_letter, row_number)

for i in range(0, len(name_list)):
    print "%s, at (%d, %d)" % (name_list[i], columns[i], rows[i])
    
def translate(columns, rows):
    for i in range(0, len(columns)):
        columns[i] = column_translate[columns[i]]
        
    for i in range(0, len(rows)):
        rows[i] = row_translate[rows[i]]
        
    return columns, rows
    

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/convoy')
def show_convoy():
    return 'This is where the convoy will be :)'
    
@app.route('/shop')
def show_shop():
    return 'Anna is opening up shop soon. Please wait a while.'
    
@app.route('/map')
def show_map():
    return render_template('map.html', 
                            map='Extra rescaled.png',
                            character_list=name_list,
                            sprite='Sprite.gif',
                            row=rows,
                            column=columns)
    
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, we don't have a page like that here."