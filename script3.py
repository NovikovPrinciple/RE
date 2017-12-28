from app import *
import csv

with open('Enemy Stats and Inventory.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for row in rowreader:
        
        temp = Character(
            name=row[0],
            class_name=row[1],
            movement=row[11],
            max_HP=row[2],
            current_HP=row[3],
            strength=row[4],
            magic=row[5],
            skill=row[6],
            speed=row[7],
            luck=row[8],
            defense=row[9],
            resistance=row[10],
            atk=row[12],
            hit=row[13],
            crit=row[14],
            avo=row[15],
            ceva=row[16])
        db.session.add(temp)
        db.session.commit()
        print row[0]
        for i in range(23, 31):
            print row[i]
            if row[i] == '' or row[i] == None:
                break
            else:
                temp.skills.append(Skill.query.get(Skill.query.filter_by(name=row[i]).first().id))
                db.session.commit()
            
        for i in range(17, 23):
            print row[i]
            if row[i] == '' or row[i] == None:
                break
            else:
                temp.items.append(Item.query.get(Item.query.filter_by(name=row[i]).first().id))
                db.session.commit()
            
print '10 - Enemies'