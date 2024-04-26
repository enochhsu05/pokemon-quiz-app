import eventlet
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import pokeapi as api
import time

app = Flask(__name__)
app.secret_key = "123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Scoreboard.sqlite3'
methods = {}
generate_async_question = False
pause_between_questions = 1

db = SQLAlchemy(app)


class Scoreboard(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    category = db.Column('category', db.String(100))
    score = db.Column('score', db.Integer)
    total = db.Column('total', db.Integer)

    def __init__(self, category, score, total):
        self.category = category
        self.score = score
        self.total = total


@app.route('/')
def menu():
    db.create_all()
    if 'total' in session:
        prev = Scoreboard.query.filter_by(category=session['mode']).first()
        if prev:
            db.session.delete(prev)
        new_score = Scoreboard(session['mode'], session['score'], session['total'])
        db.session.add(new_score)
        db.session.commit()
    session.clear()
    global methods
    mons_and_none = api.mons.copy()
    mons_and_none.insert(0, 'None')
    methods = {'generation': {'question': question_generation, 'answer': static_answer,
                              'options': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'html': 'dropdown'},
               'pokemon': {'question': question_pokemon, 'answer': static_answer,
                           'options': api.mons, 'html': 'dropdown'},
               'typing': {'question': question_typing, 'answer': answer_typing,
                          'options': mons_and_none, 'html': 'dropdown'},
               'moveset': {'question': question_moveset, 'answer': answer_moveset, 'options': api.mons,
                           'html': 'dropdown'},
               'matchup': {'question': question_matchup, 'answer': answer_matchup, 'options': ['0x', '0.5x', '1x', '2x'],
                           'html': 'multiple_choice'},
               'damage': {'question': question_damage, 'answer': static_answer, 'options': [1, 2, 3, 4, '5+'],
                          'html': 'multiple_choice_2'}}
    return render_template('difficulty_select.html')


@app.route('/menu')
def to_menu():
    return redirect(url_for('menu'))


@app.route('/difficulty/<difficulty>', methods=['POST'])
def difficulty_select(difficulty):
    session['difficulty'] = difficulty
    return render_template('quiz_select.html')


@app.route('/scoreboard', methods=['POST'])
def scoreboard():
    return render_template('scoreboard.html', scoreboard=list(reversed(Scoreboard.query.all())))


@app.route('/<title>')
def index(title):
    return render_template(f'{methods[session["mode"]]["html"]}.html', options=methods[session['mode']]['options'], methods=methods,
                           hi=generate_async_question)


@app.route('/generation', methods=['POST'])
def generation():
    session['mode'] = 'generation'
    question()
    return redirect(url_for('index', title=session['mode']))


@app.route('/pokemon', methods=['POST'])
def pokemon():
    session['mode'] = 'pokemon'
    question()
    return redirect(url_for('index', title=session['mode']))


@app.route('/typing', methods=['POST'])
def typing():
    session['mode'] = 'typing'
    question()
    return redirect(url_for('index', title=session['mode']))


@app.route('/moveset', methods=['POST'])
def moveset():
    session['mode'] = 'moveset'
    question()
    return redirect(url_for('index', title=session['mode']))


@app.route('/matchup', methods=['POST'])
def matchup():
    session['mode'] = 'matchup'
    question()
    return redirect(url_for('index', title=session['mode']))


@app.route('/damage', methods=['POST'])
def damage():
    session['mode'] = 'damage'
    question()
    return redirect(url_for('index', title=session['mode']))


def question():
    session['answer'] = ''
    session['result'] = ''
    return methods[session['mode']]['question']()


@app.route('/answer', methods=['POST'])
def answer(user_input=None):
    global generate_async_question
    if not generate_async_question:
        generate_async_question = True
        session['question'] = ''
        if user_input is None:
            return methods[session['mode']]['answer']()
        else:
            return methods[session['mode']]['answer'](user_input)
    else:
        return redirect(url_for('index', title=session['mode']))


@app.route('/answer/<user_input>', methods=['GET', 'POST'])
def answer_input(user_input: None):
    return answer(user_input)


def static_answer(user_input=None):
    if user_input is None:
        user_input = request.form['user_input']
    if 'score' not in session.keys():
        session['score'] = 0
    session['total'] = session['total'] + 1 if 'total' in session.keys() else 1
    if str(session['answer']) == user_input:
        session['result'] = "That's right!"
        session['score'] += 1
    else:
        session['result'] = f"That's wrong... it's actually {session['answer']}."
    return redirect(url_for('index', title=session['mode']))


def answer_typing():
    user_input = request.form['user_input']
    if 'score' not in session.keys():
        session['score'] = 0
    session['total'] = session['total'] + 1 if 'total' in session.keys() else 1
    if user_input == 'None':
        if session['answer'] is None:
            session['result'] = "That's right!"
            session['score'] += 1
        else:
            session['result'] = f"That's wrong... it's actually {session['answer']}."
            session['image'] = api.get_pokemon_sprite(session['answer'])
        return redirect(url_for('index', title=session['mode']))
    actual_typings = api.get_type_from_pokemon_name(user_input)
    if all(mon_typing in actual_typings for mon_typing in list(session['generated'])):
        session['result'] = "That's right!"
        session['score'] += 1
        session['image'] = api.get_pokemon_sprite(user_input)
    else:
        session['result'] = f"That's wrong... it's actually {session['answer']}."
        session['image'] = api.get_pokemon_sprite(session['answer'])
    return redirect(url_for('index', title=session['mode']))


def answer_moveset():
    user_input = request.form['user_input']
    if 'score' not in session.keys():
        session['score'] = 0
    session['total'] = session['total'] + 1 if 'total' in session.keys() else 1
    if user_input in session['generated']:
        if user_input == session['answer']:
            session['result'] = "That's right!"
        else:
            session['result'] = f"The specific pokemon is {session['answer']}, but close enough!"
        session['score'] += 1
    else:
        session['result'] = f"That's wrong... it's actually {session['answer']}."
    session['image'] = api.get_pokemon_sprite(session['answer'])
    return redirect(url_for('index', title=session['mode']))


def answer_matchup(user_input):
    if 'score' not in session.keys():
        session['score'] = 0
    session['total'] = session['total'] + 1 if 'total' in session.keys() else 1
    if user_input == session['answer']:
        session['result'] = "That's right!"
        session['score'] += 1
    else:
        session['result'] = f"That's wrong... it's actually {session['answer']}."
    return redirect(url_for('index', title=session['mode']))


def question_generation():
    generated = api.pokemon_generation_quiz()
    return create_question(f"Which generation is {generated['name']} from?", generated['gen'],
                           api.get_pokemon_sprite(generated['name']))


def question_pokemon():
    generated = api.generate_random_pokemon_name()
    return create_question(f"Name the pokemon!", generated, api.get_pokemon_sprite(generated))


def question_typing():
    typings = api.generate_random_typing()
    return create_question(f"Name a {typings[0]}/{typings[1]} pokemon!",
                           answer=api.type_combinations[typings],
                           generated=typings)


def question_moveset():
    generated = api.generate_moveset_question()
    moves = ''
    for move in generated['moveset']:
        moves += '<br>' + move
    return create_question(f"Which pokemon can learn all of these moves through leveling up? {moves}",
                           answer=generated['mon'], generated=generated['line'])


def question_matchup():
    generated = api.generate_matchup_question()
    return create_question(f"What is the effectiveness of {generated['offensive_type']} type against {generated['defensive_type']} type?",
                           answer=generated['matchup'])


def question_damage():
    generated = api.generate_damage_question()
    return create_question(f"What is the minimum number of hits it takes for {generated['attacking_mon']} to knock out {generated['defending_mon']} using {generated['move']}?",
                           answer=generated['hits'])


def create_question(question, answer=None, image=None, generated=None):
    session['question'] = question
    session['answer'] = answer
    session['result'] = ''
    session['image'] = image
    session['generated'] = generated
    return redirect(url_for('index', title=session['mode']))


@app.route('/async_question')
def async_question():
    def long_running_task():
        time.sleep(pause_between_questions)

    eventlet.spawn(long_running_task).wait()
    question()
    global generate_async_question
    generate_async_question = False
    return jsonify(result=session)


@app.route('/data')
def get_data():
    return jsonify(result=generate_async_question)


if __name__ == '__main__':
    app.run(debug=True)
