from app import *
import csv

for type in ['Foot', 'Beast', 'Mage', 'Mounted1', 'Mounted2', 'Flier']:
    db.session.add(Unit_Type(name=type))
    
db.session.commit()
print '1 - Unit Types'


with open('Player List.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for Name, Gold in rowreader:
        db.session.add(Player(name=Name, gold=Gold))
        
    db.session.commit()
print '2 - Players'


with open('Terrain and Unit Types.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for row in rowreader:
        db.session.add(Terrain(
            name=row[0], 
            avo_bonus=row[1], 
            def_bonus=row[2], 
            res_bonus=row[3],
            heal_per_turn=row[4]))
            
    db.session.commit()
print '3 - Terrain'


db.session.add(Map(name='1x', total_columns=17, total_rows=17))
db.session.add(Map(name='1-2', total_columns=13, total_rows=19))
db.session.add(Map(name='1-2x', total_columns=19, total_rows=17))
print '4 - Map'


with open('Skill List.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for Name, Description in rowreader:
        db.session.add(Skill(name=Name, description=Description))
        
    db.session.commit()
print '5 - Skills'


with open('Item List.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for row in rowreader:
        db.session.add(Item(
            name=row[0],
            type=row[1],
            attack_stat=row[2],
            rank=row[3],
            might=row[4],
            uses=row[5],
            hit=row[6],
            crit=row[7],
            crit_percent_mod=row[8],
            crit_damage_mod=row[9],
            avo=row[10],
            ceva=row[11],
            range=row[12],
            hp_mod=row[13],
            str_mod=row[14],
            mag_mod=row[15],
            skl_mod=row[16],
            spd_mod=row[17],
            lck_mod=row[18],
            def_mod=row[19],
            res_mod=row[20],
            e_spd_off=row[21],
            e_spd_def=row[22],
            gem_slots=row[23],
            reverse_WT=row[24],
            double_WT=row[25],
            ineffective=row[26],
            cost=row[27],
            effect=row[28],
            in_shop=row[29],
            stock_in_shop=row[30],
            in_convoy=row[31],
            stock_in_convoy=row[32]))
            
    db.session.commit()
print '6 - Items'


with open('Character Stats and Inventory.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for row in rowreader:
        player_id = ''
        if Player.query.filter_by(name=row[0]).first() != None:
                player_id=Player.query.filter_by(name=row[0]).first().id,
                
        temp = Character(
            player=Player.query.get(player_id),
            name=row[1],
            class_name=row[2],
            level=row[3],
            movement=row[4],
            ore=row[5],
            max_HP=row[6],
            current_HP=row[7],
            strength=row[8],
            magic=row[9],
            skill=row[10],
            speed=row[11],
            luck=row[12],
            defense=row[13],
            resistance=row[14])
        db.session.add(temp)
        db.session.commit()
        for i in range(15, 23):
            if row[i] == '' or row[i] == None:
                break
            else:
                temp.skills.append(Skill.query.get(Skill.query.filter_by(name=row[i]).first().id))
                db.session.commit()
            
        for i in range(23, 29):
            if row[i] == '' or row[i] == None:
                break
            else:
                temp.items.append(Item.query.get(Item.query.filter_by(name=row[i]).first().id))
                db.session.commit()
            
print '7 - Characters'