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



def translate(columns, rows):
    for i in range(0, len(columns)):
        try:
            if columns[i] == 'Column' or columns[i] == '':
                continue
            columns[i] = column_translate[columns[i]]
        except:
            if KeyError:
                continue

    for i in range(0, len(rows)):
        try:
            if rows[i] == 'Row' or rows[i] == '':
                continue
            rows[i] = row_translate[rows[i]]
        except:
            if KeyError:
                continue
    return columns, rows
    
    

# This one is for the main map:
with open('static/1-2.csv', 'rb') as csvfile:
    rowreader = csv.reader(csvfile)
    rowreader.next()
    Characters = rowreader.next()
    Class = rowreader.next()
    Max = rowreader.next()
    Current = rowreader.next()
    Str = rowreader.next()
    Mag = rowreader.next()
    Skl = rowreader.next()
    Spd = rowreader.next()
    Lck = rowreader.next()
    Def = rowreader.next()
    Res = rowreader.next()
    Move = rowreader.next()
    Atk = rowreader.next()
    Hit = rowreader.next()
    Crit = rowreader.next()
    Avo = rowreader.next()
    CEva = rowreader.next()
    Item1 = rowreader.next()
    Item2 = rowreader.next()
    Item3 = rowreader.next()
    Item4 = rowreader.next()
    Item5 = rowreader.next()
    Accessory = rowreader.next()
    Skill1 = rowreader.next()
    Skill2 = rowreader.next()
    Skill3 = rowreader.next()
    Skill4 = rowreader.next()
    Skill5 = rowreader.next()
    Skill6 = rowreader.next()
    Skill7 = rowreader.next()
    Skill8 = rowreader.next()
    Column = rowreader.next()
    Row = rowreader.next()
    Statpack = rowreader.next()
    is_PNG = rowreader.next()
    
columns, rows = translate(Column, Row)

'''Terrain_list = []

with open('static/terrain_gaiden.csv', 'rb') as terrainfile2:
    rowreader4 = csv.reader(terrainfile2)
    for i in range(0, 17):                                #use range(0, number of map rows)
        Terrain_list.append(rowreader4.next())'''
    
# This one's for the Gaiden:
with open('static/sample2.csv', 'rb') as csvfile2:
    rowreader = csv.reader(csvfile2)
    GCharacters = rowreader.next()
    GClass = rowreader.next()
    GMax = rowreader.next()
    GCurrent = rowreader.next()
    GStr = rowreader.next()
    GMag = rowreader.next()
    GSkl = rowreader.next()
    GSpd = rowreader.next()
    GLck = rowreader.next()
    GDef = rowreader.next()
    GRes = rowreader.next()
    GMove = rowreader.next()
    GAtk = rowreader.next()
    GHit = rowreader.next()
    GCrit = rowreader.next()
    GAvo = rowreader.next()
    GCEva = rowreader.next()
    GItem1 = rowreader.next()
    GItem2 = rowreader.next()
    GItem3 = rowreader.next()
    GItem4 = rowreader.next()
    GItem5 = rowreader.next()
    GAccessory = rowreader.next()
    GSkill1 = rowreader.next()
    GSkill2 = rowreader.next()
    GSkill3 = rowreader.next()
    GSkill4 = rowreader.next()
    GSkill5 = rowreader.next()
    GSkill6 = rowreader.next()
    GSkill7 = rowreader.next()
    GSkill8 = rowreader.next()
    GColumn = rowreader.next()
    GRow = rowreader.next()
    GStatpack = rowreader.next()
    Gis_PNG = rowreader.next()

Gcolumns, Grows = translate(GColumn, GRow)

Gterrain_list = []

with open('static/terrain_gaiden.csv', 'rb') as terrainfile2:
    rowreader4 = csv.reader(terrainfile2)
    for i in range(0, 17):                                #use range(0, number of map rows)
        Gterrain_list.append(rowreader4.next())

Gterrain_list[0][0] = 'Plains'
    
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
                            map='1-2 rescaled.png',
                            TITLE='Chapter 1-2',
                            character_list=Characters,
                            sprite='Anna',
                            CURRENT=Current,
                            MAX=Max,
                            STR=Str,
                            MAG=Mag,
                            SKL=Skl,
                            SPD=Spd,
                            DEF=Def,
                            RES=Res,
                            LCK=Lck,
                            MOV= Move,
                            ITEM1=Item1,
                            ITEM2=Item2,
                            ITEM3=Item3,
                            ITEM4=Item4,
                            ITEM5=Item5,
                            ACC=Accessory,
                            ATK=Atk,
                            HIT=Hit,
                            CRIT=Crit,
                            AVO=Avo,
                            CEVA=CEva,
                            SKILL1=Skill1,
                            SKILL2=Skill2,
                            SKILL3=Skill3,
                            SKILL4=Skill4,
                            SKILL5=Skill5,
                            SKILL6=Skill6,
                            SKILL7=Skill7,
                            SKILL8=Skill8,
                            ROW=Row,
                            COL=Column,
                            STATPACK=Statpack,
                            PNG='TRUE',
                            terrain_list=[])
                            
                            
@app.route('/gaiden')
def show_gaiden():
    return render_template( 'map.html', 
                            map='1x.png',
                            TITLE='Chapter 1x',
                            character_list=GCharacters,
                            sprite=GClass,
                            CURRENT=GCurrent,
                            MAX=GMax,
                            STR=GStr,
                            MAG=GMag,
                            SKL=GSkl,
                            SPD=GSpd,
                            DEF=GDef,
                            RES=GRes,
                            LCK=GLck,
                            MOV=GMove,
                            ITEM1=GItem1,
                            ITEM2=GItem2,
                            ITEM3=GItem3,
                            ITEM4=GItem4,
                            ITEM5=GItem5,
                            ACC=GAccessory,
                            ATK=GAtk,
                            HIT=GHit,
                            CRIT=GCrit,
                            AVO=GAvo,
                            CEVA=GCEva,
                            SKILL1=GSkill1,
                            SKILL2=GSkill2,
                            SKILL3=GSkill3,
                            SKILL4=GSkill4,
                            SKILL5=GSkill5,
                            SKILL6=GSkill6,
                            SKILL7=GSkill7,
                            SKILL8=GSkill8,
                            ROW=GRow,
                            COL=GColumn,
                            STATPACK=GStatpack,
                            PNG=Gis_PNG,
                            terrain_list=Gterrain_list)
                            
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, we don't have a page like that here."