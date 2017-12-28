from app import *
import csv

with open('Terrain and Unit Types.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    
    for row in rowreader:
        for i in range(5, 11):
            db.session.add(TerrainUnitType(
                id_Terrain = Terrain.query.filter_by(name=row[0]).first().id,
                id_Unit_Type = i-4,
                cost = row[i]))
    db.session.commit()
print '8 - TerrainUnitType'
         

with open('terrain_gaiden.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    j = 0
    
    for row in rowreader:
        j += 1
        i = 0
        for type in row:
            i += 1
            db.session.add(TerrainMap(
                id_Terrain=Terrain.query.filter_by(name=type).first().id,
                id_Map=1,
                tile_column=i,
                tile_row=j))
        db.session.commit()
        
        
with open('terrain_1-2.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    j = 0
    
    for row in rowreader:
        j += 1
        i = 0
        for type in row:
            i += 1
            db.session.add(TerrainMap(
                id_Terrain=Terrain.query.filter_by(name=type).first().id,
                id_Map=2,
                tile_column=i,
                tile_row=j))
        db.session.commit()
        
        
with open('terrain_fog.csv', 'rb') as file:
    rowreader = csv.reader(file)
    rowreader.next()
    j = 0
    
    for row in rowreader:
        j += 1
        i = 0
        for type in row:
            i += 1
            db.session.add(TerrainMap(
                id_Terrain=Terrain.query.filter_by(name=type).first().id,
                id_Map=3,
                tile_column=i,
                tile_row=j))
        db.session.commit()
print '9 - TerrainMap'