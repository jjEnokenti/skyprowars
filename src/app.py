from flask import Flask, render_template, request, redirect, url_for

from src.arena import Arena
from src.classes import unit_classes
from src.equipment import Equipment
from src.unit import BaseUnit, PlayerUnit, EnemyUnit


def create_app():
    app_conf = Flask(__name__)
    return app_conf


heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit,
}

app = create_app()
arena = Arena()


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/fight/")
def start_fight():
    arena.start_game(
        player=heroes['player'],
        enemy=heroes['enemy']
    )
    return render_template('fight.html', heroes=heroes)


@app.route("/fight/hit")
def hit():
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    return render_template("index.html")


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    equipment = Equipment()
    if request.method == 'GET':
        result = {
            'header': 'Выберите персонажа',
            'classes': unit_classes,
            'weapons': equipment.get_weapons_names(),
            'armors': equipment.get_armors_names()
        }
        return render_template('hero_choosing.html', result=result)

    elif request.method == 'POST':
        name = request.form['name']
        unit_class = request.form['unit_class']
        armor_name = request.form['armor']
        weapon_name = request.form['weapon']
        player = PlayerUnit(name=name, unit_class=unit_classes[unit_class])
        player.equip_armor(equipment.get_armor(armor_name=armor_name))
        player.equip_weapon(equipment.get_weapon(weapon_name=weapon_name))
        heroes['player'] = player
        return redirect(url_for('choose_enemy'))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    equipment = Equipment()
    if request.method == 'GET':
        result = {
            'header': 'Выберите противника',
            'classes': unit_classes,
            'weapons': equipment.get_weapons_names(),
            'armors': equipment.get_armors_names()
        }
        return render_template('hero_choosing.html', result=result)

    elif request.method == 'POST':
        name = request.form['name']
        unit_class = request.form['unit_class']
        armor_name = request.form['armor']
        weapon_name = request.form['weapon']
        enemy = EnemyUnit(name=name, unit_class=unit_classes[unit_class])
        enemy.equip_armor(equipment.get_armor(armor_name=armor_name))
        enemy.equip_weapon(equipment.get_weapon(weapon_name=weapon_name))
        heroes['enemy'] = enemy
        return redirect(url_for('start_fight'))
