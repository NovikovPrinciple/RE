from app import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/main')
def show_main():
    Main_list = []
    s = session()
    
    for instance in s.query(Character).all():
        if (s.query(Character).get(instance.id).on_tile != None and
            s.query(Character).get(instance.id).on_tile.source_map.id == 2):
            Main_list.append(instance)
    
    return render_template('map.html',
                    character_list=Main_list,
                    title='Chapter 1-2: March',
                    MAPNAME='1-2.png')    

    
@app.route('/gaiden')
def show_gaiden():
    Gaiden_list = []
    s = session()
    
    for instance in s.query(Character).all():
        if (s.query(Character).get(instance.id).on_tile != None and
            s.query(Character).get(instance.id).on_tile.source_map.id == 1):
            Gaiden_list.append(instance)
    
    return render_template('map.html',
                    character_list=Gaiden_list,
                    title='Gaiden: Cabin in the Woods',
                    MAPNAME='1-1x.png')
                    

@app.route('/fog')
def show_fog():                    
    Fog_list = []
    s = session()

    for instance in s.query(Character).all():
        if (s.query(Character).get(instance.id).on_tile != None and
            s.query(Character).get(instance.id).on_tile.source_map.id == 3):
            Fog_list.append(instance)
    
    return render_template('map.html',
                    character_list=Fog_list,
                    title='Gaiden: Cat and Mouse',
                    MAPNAME='1-2x.png')