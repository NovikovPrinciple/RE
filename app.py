from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/team_o.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

engine = create_engine('sqlite:///tmp/team_o.db')
session = sessionmaker()
session.configure(bind=engine)



inventory = db.Table('inventory', 
    db.Column('id_Character', db.Integer, db.ForeignKey('character.id')),
    db.Column('id_Item', db.Integer, db.ForeignKey('item.id'))
    )
    
    
CharacterSkill = db.Table('CharacterSkill',
    db.Column('id_Character', db.Integer, db.ForeignKey('character.id'), primary_key=True),
    db.Column('id_Skill', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
    )    


class TerrainUnitType(db.Model):
    __tablename__ = 'terrain_unittype'
    id = db.Column(db.Integer, primary_key=True)
    id_Terrain = db.Column(db.Integer, db.ForeignKey('terrain.id'), unique=False, nullable=False)
    id_Unit_Type = db.Column(db.Integer, db.ForeignKey('unit_type.id'), unique=False, nullable=False)
    cost = db.Column(db.Integer, unique=False, nullable=False)
    
    
class TerrainMap(db.Model):
    __tablename__ = 'terrainmap'
    id = db.Column(db.Integer, primary_key=True)
    id_Terrain = db.Column(db.Integer, db.ForeignKey('terrain.id'), unique=False, nullable=False)
    id_Map = db.Column(db.Integer, db.ForeignKey('map.id'), unique=False, nullable=False)
    tile_column = db.Column(db.Integer, unique=False, nullable=False)
    tile_row = db.Column(db.Integer, unique=False, nullable=False)
    
    occupants = db.relationship('Character', backref='on_tile')


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    gold = db.Column(db.Integer, unique=False, nullable=False)
    
    characters = db.relationship('Character', backref='player')
    
    
class Unit_Type(db.Model):
    __tablename__ = 'unit_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    
    characters = db.relationship('Character', backref='is_type')
    terrain_cost = db.relationship('TerrainUnitType', backref='for_unit')
    
    
class Terrain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    avo_bonus = db.Column(db.Integer, unique=False, nullable=False)
    def_bonus = db.Column(db.Integer, unique=False, nullable=False)
    res_bonus = db.Column(db.Integer, unique=False, nullable=False)
    heal_per_turn = db.Column(db.String(15), unique=False, nullable=False)
    
    costs = db.relationship('TerrainUnitType', backref='on_terrain')
    tile = db.relationship('TerrainMap', backref='tile_terrain')
    
    
class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    total_columns = db.Column(db.Integer, unique=False, nullable=True)
    total_rows = db.Column(db.Integer, unique=False, nullable=True)
    
    tile = db.relationship('TerrainMap', backref='source_map')
    

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True, nullable=True)

    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    type = db.Column(db.String(15), unique=False, nullable=True)
    attack_stat = db.Column(db.String(15), unique=False, nullable=True)
    rank = db.Column(db.String(5), unique=False, nullable=True)
    might = db.Column(db.Integer, unique=False, nullable=True)
    uses = db.Column(db.Integer, unique=False, nullable=True)
    hit = db.Column(db.Integer, unique=False, nullable=True)
    crit = db.Column(db.Integer, unique=False, nullable=True)
    crit_percent_mod = db.Column(db.String(15), unique=False, nullable=True)
    crit_damage_mod = db.Column(db.String(15), unique=False, nullable=True)
    avo = db.Column(db.Integer, unique=False, nullable=True)
    ceva = db.Column(db.Integer, unique=False, nullable=True)
    range = db.Column(db.String(15), unique=False, nullable=True)
    hp_mod = db.Column(db.Integer, unique=False, nullable=True)
    str_mod = db.Column(db.Integer, unique=False, nullable=True)
    mag_mod = db.Column(db.Integer, unique=False, nullable=True)
    skl_mod = db.Column(db.Integer, unique=False, nullable=True)
    spd_mod = db.Column(db.Integer, unique=False, nullable=True)
    lck_mod = db.Column(db.Integer, unique=False, nullable=True)
    def_mod = db.Column(db.Integer, unique=False, nullable=True)
    res_mod = db.Column(db.Integer, unique=False, nullable=True)
    e_spd_off = db.Column(db.Integer, unique=False, nullable=True)
    e_spd_def = db.Column(db.Integer, unique=False, nullable=True)
    gem_slots = db.Column(db.Integer, unique=False, nullable=True)
    reverse_WT = db.Column(db.String(15), unique=False, nullable=True)
    double_WT = db.Column(db.String(15), unique=False, nullable=True)
    ineffective = db.Column(db.String(15), unique=False, nullable=True)
    cost = db.Column(db.Integer, unique=False, nullable=True)
    effect = db.Column(db.String(100), unique=False, nullable=True)
    in_shop = db.Column(db.String(15), unique=False, nullable=True)
    stock_in_shop = db.Column(db.Integer, unique=False, nullable=True)
    in_convoy = db.Column(db.String(15), unique=False, nullable=True)
    stock_in_convoy = db.Column(db.Integer, unique=False, nullable=True)

    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    class_name = db.Column(db.String(30), unique=False, nullable=False)
    level = db.Column(db.String(15), unique=False, nullable=True)
    id_Player = db.Column(db.Integer, db.ForeignKey('player.id'), unique=False, nullable=True)
    id_Unit_Type = db.Column(db.Integer, db.ForeignKey('unit_type.id'), unique=False, nullable=True)
    id_current_tile = db.Column(db.Integer, db.ForeignKey('terrainmap.id'), unique=False, nullable=True)
    guard_stance = db.Column(db.String(15), unique=False, nullable=True)
    statpack = db.Column(db.String(15), unique=False, nullable=True)
    max_HP = db.Column(db.Integer, unique=False, nullable=True)
    current_HP = db.Column(db.Integer, unique=False, nullable=True)
    strength = db.Column(db.Integer, unique=False, nullable=True)
    magic = db.Column(db.Integer, unique=False, nullable=True)
    skill = db.Column(db.Integer, unique=False, nullable=True)
    speed = db.Column(db.Integer, unique=False, nullable=True)
    luck = db.Column(db.Integer, unique=False, nullable=True)
    defense = db.Column(db.Integer, unique=False, nullable=True)
    resistance = db.Column(db.Integer, unique=False, nullable=True)
    movement = db.Column(db.Integer, unique=False, nullable=True)
    ore = db.Column(db.Integer, unique=False, nullable=True)
    atk = db.Column(db.Integer, unique=False, nullable=True)
    hit = db.Column(db.Integer, unique=False, nullable=True)
    crit = db.Column(db.Integer, unique=False, nullable=True)
    avo = db.Column(db.Integer, unique=False, nullable=True)
    ceva = db.Column(db.Integer, unique=False, nullable=True)
    
    items = db.relationship('Item', secondary=inventory, backref='characters')
    skills = db.relationship('Skill', secondary=CharacterSkill, backref='characters')    

    
from views import *

                        
if __name__ == "__main__":                        
    app.run(debug=True)