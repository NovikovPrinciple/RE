from app import *
import pytest

@pytest.fixture(scope='function')
def player():
    global Novi
    global Appa
    Novi = Player(name='Novikov_Principle', gold=5000)
    Appa = Player(name='Appa', gold=15000)
    db.session.add(Novi)
    db.session.add(Appa)
    db.session.commit()
    yield Novi, Appa
    db.session.delete(Novi)
    db.session.delete(Appa)
    db.session.commit()

    
def test_one_player_name(player):
    assert Novi.name == 'Novikov_Principle'
    
def test_another_player_name(player):
    assert Player.query.get(2).name == 'Appa'

def test_player_gold(player):
    assert Player.query.filter_by(name='Appa').first().gold == 15000
    

@pytest.fixture(scope='session')
def all():
    global Novi
    global Appa
    Novi = Player(name='Novikov_Principle', gold=5000)
    Appa = Player(name='Appa', gold=15000)
    db.session.add(Novi)
    db.session.add(Appa)
   
    db.session.add(Terrain(name='Plains', avo_bonus=0, def_bonus=0, res_bonus=0, heal_per_turn='0'))
    db.session.add(Terrain(name='Fort', avo_bonus=20, def_bonus=2, res_bonus=0, heal_per_turn='15%'))
    
    db.session.add(Unit_Type(name='Foot'))
    db.session.add(Unit_Type(name='Flier'))
    
    db.session.add(Map(name='1x', total_columns=17, total_rows=17))
    
    db.session.add(TerrainUnitType(id_Terrain=1, id_Unit_Type=1, cost=1))
    db.session.add(TerrainUnitType(id_Terrain=1, id_Unit_Type=2, cost=1))
    db.session.add(TerrainUnitType(id_Terrain=2, id_Unit_Type=1, cost=3))
    db.session.add(TerrainUnitType(id_Terrain=2, id_Unit_Type=2, cost=1))
    
    db.session.add(TerrainMap(id_Terrain=1, id_Map=1, tile_column=1, tile_row=1))
    db.session.add(TerrainMap(id_Terrain=2, id_Map=1, tile_column=1, tile_row=2))
    db.session.add(TerrainMap(id_Terrain=2, id_Map=1, tile_column=2, tile_row=1))
    db.session.add(TerrainMap(id_Terrain=1, id_Map=1, tile_column=2, tile_row=2))
    
    Stemp1 = Skill(name='La La La', description='Serra Emblem: Activate!')
    db.session.add(Stemp1)
    Stemp2 = Skill(name='Lethality', description='Ninja mode, on!')
    db.session.add(Stemp2)
    
    db.session.add(Item(name='Iron Sword'))
    db.session.add(Item(name='Bronze Lance'))
    db.session.add(Item(name='Steel Bow'))
    
    temp1 = Character(name='Jeffray', class_name='Monarch', id_Player=2, id_Unit_Type=2, id_current_tile=1)
    db.session.add(temp1)
    temp2 = Character(name='Glenn', class_name='Bow Knight', id_Player=2, id_Unit_Type=2, id_current_tile=2)
    db.session.add(temp2)
    temp3 = Character(name='Tamlen', class_name='Spearmaster', id_Player=1, id_Unit_Type=1, id_current_tile=3)
    db.session.add(temp3)
    temp4 = Character(name='Laven', class_name='Adventurer', id_Player=1, id_Unit_Type=1, id_current_tile=3)
    db.session.add(temp4)
    db.session.commit()
    temp1.skills.append(Stemp1)
    temp1.skills.append(Stemp2)
    db.session.commit()
    yield Novi, Appa
    
    
    db.session.delete(Character.query.get(1))
    db.session.delete(Character.query.get(2))
    db.session.delete(Character.query.get(3))
    db.session.delete(Character.query.get(4))
    db.session.delete(Item.query.get(1))
    db.session.delete(Item.query.get(2))
    db.session.delete(Item.query.get(3))
    db.session.delete(Skill.query.get(1))
    db.session.delete(Skill.query.get(2))
    db.session.delete(TerrainMap.query.get(1))
    db.session.delete(TerrainMap.query.get(2))
    db.session.delete(TerrainMap.query.get(3))
    db.session.delete(TerrainMap.query.get(4))
    db.session.delete(TerrainUnitType.query.get(1))
    db.session.delete(TerrainUnitType.query.get(2))
    db.session.delete(TerrainUnitType.query.get(3))
    db.session.delete(TerrainUnitType.query.get(4))
    db.session.delete(Map.query.get(1))
    db.session.delete(Unit_Type.query.get(1))
    db.session.delete(Unit_Type.query.get(2))
    db.session.delete(Terrain.query.get(1))
    db.session.delete(Terrain.query.get(2))
    db.session.delete(Player.query.get(1))
    db.session.delete(Player.query.get(2))
    db.session.commit()
    
    
    
def test_unit_type_1(all):
    assert Unit_Type.query.get(1).name == 'Foot'
    
def test_unit_type_2(all):
    assert Unit_Type.query.get(2).name == 'Flier'
    
def test_terrains(all):
    assert Terrain.query.get(1).name == 'Plains'
    assert Terrain.query.filter_by(name='Fort').first().heal_per_turn == '15%'
    
def test_movement_cost(all):
    assert Terrain.query.get(1).costs == [TerrainUnitType.query.get(1), TerrainUnitType.query.get(2)]
    assert Terrain.query.get(2).costs == [TerrainUnitType.query.get(3), TerrainUnitType.query.get(4)]
    assert Unit_Type.query.get(1).terrain_cost == [TerrainUnitType.query.get(1), TerrainUnitType.query.get(3)]
    assert Unit_Type.query.get(2).terrain_cost == [TerrainUnitType.query.get(2), TerrainUnitType.query.get(4)]
    
def test_terrain_per_tile(all):
    assert Terrain.query.get(1).tile == [TerrainMap.query.get(1), TerrainMap.query.get(4)]
    assert Terrain.query.get(2).tile == [TerrainMap.query.get(2), TerrainMap.query.get(3)]
    assert TerrainMap.query.get(1).tile_terrain.name == 'Plains'
    assert TerrainMap.query.get(2).tile_terrain.name == 'Fort'
    assert TerrainMap.query.get(3).source_map.name == '1x'
    
def test_character_skill_1(all):
    assert Character.query.get(1).skills[1].name == 'Lethality'

def test_character_skill_2(all):    
    assert Character.query.get(1).skills[0].name == 'La La La'
    #assert Character.query.get(1).skills.pop[0] == []