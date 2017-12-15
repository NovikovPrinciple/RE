import csv

column_translate = {   
                    'A':105,
                    'B':155,
                    'F':355,
                    'G':405,
                    'H':455,
                    'Q':905,
                    'S':1005
                }
row_translate = {
                    '1':105,
                    '10':555,
                    '11':605,
                    '12':655,
                    '13':705,
                    '14':755,
                    '15':805,
                    '16':855,
                    '17':905,
                    '18':955,
                    '19':1005,
                    '20':1055,
                    '21':1105,
                    '22':1155
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