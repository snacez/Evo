from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Song model
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

# In-memory task list
tasks = []

@app.route('/')
def home():
    return redirect(url_for('add_task_page'))

@app.route('/tasks')
def task_list():
    return render_template('task_list.html')

@app.route('/add_task')
def add_task_page():
    return render_template('add_task.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['task']
    tasks.append({'description': task_description})
    return render_template('add_task.html', message="Task added successfully")

@app.route('/get_tasks')
def get_tasks():
    return jsonify(tasks)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
        greeting = 'Доброе утро'
    elif 12 <= now.hour < 18:
        greeting = 'Добрый день'
    elif 18 <= now.hour < 24:
        greeting = 'Добрый вечер'
    else:
        greeting = 'Доброй ночи'
    return render_template('index.html', greeting=greeting)

@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)



@app.route('/')
def choose_role():
    return render_template('choose_role.html')



@app.route('/123', methods=['GET', 'POST'])
def index123():
    if request.method == 'POST':
        role = request.form.get('role')
        return redirect(url_for('welcome', role=role))
    return render_template('index123.html')

@app.route('/welcome')
def welcome():
    role = request.args.get('role')
    abilities = {
        'admin': 'Полный доступ ко всем функциям.',
        'moderator': 'Может редактировать записи и комментарии.',
        'user': 'Может создавать записи от своего имени и просматривать френдленту.'
    }
    return render_template('welcome.html', role=role.capitalize(), abilities=abilities.get(role, 'Неизвестная роль'))

if __name__ == '__main__':
    app.run(debug=True)




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для заметок
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Создание таблицы в базе данных (если её нет)
db.create_all()

@app.route('/nott')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/note/<int:note_id>')
def note_detail(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', note=note)

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)