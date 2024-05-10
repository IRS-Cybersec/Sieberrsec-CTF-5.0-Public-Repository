from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3
import jwt
import uuid
from playwright.sync_api import sync_playwright




def visit_page(note_id):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        context.add_cookies([{"name": 'flag', "value": 'sctf{{s4mp13_f149}}', "url": 'http://localhost:5000'}])

        page.goto('http://localhost:5000/notes/' + note_id)
        page.wait_for_timeout(5000)

        browser.close()


conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')

conn = sqlite3.connect('notes.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS notes (uuid TEXT PRIMARY KEY, title TEXT, content TEXT, username TEXT)')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createAccount', methods=['POST'])
def createAccount():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    if res is not None:
        return 'Username already exists'
    else:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return 'Account created'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    if res is not None:
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('token', token)
        return resp
    else:
        return 'Invalid username or password'

@app.route('/home', methods=['GET'])
def home():
    token = request.cookies.get('token')
    try:
        username = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        notes = c.execute('SELECT * FROM notes WHERE username = ?', (username['username'],)).fetchall()
        return render_template('home.html', username=username, notes=notes)
    except jwt.ExpiredSignatureError:
        return 'Expired token'
    except jwt.InvalidTokenError:
        return 'Invalid token'

@app.route('/new', methods=['POST'])
def new():
    title = request.form['title']
    content = request.form['content']
    banned = ['<', '>', '(', ')', "'", '`', 'img', 'onerror', 'onload', 'src', 'http', 'https', 'flag', 'SCTF', ',', '.', 'fetch', 'open', 'send','[',']', '\\', '#', '&', '?']
    for i in banned:
        if i in content.lower():
            return 'Invalid input'
    token = request.cookies.get('token')
    username = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['username']
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('INSERT INTO notes (uuid, title, content, username) VALUES (?, ?, ?, ?)', (str(uuid.uuid4()), title, content, username))
    conn.commit()
    return redirect(url_for('home'))    

@app.route('/notes/<string:note_id>')
def view_note(note_id):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    note = c.execute('SELECT * FROM notes WHERE uuid = ?', (note_id,)).fetchone()
    return render_template('note.html', note=note)


@app.route('/report', methods=['GET'])
def report():
    note_id = request.args.get('note_id')
    for i in note_id:
        if i not in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-':
            return 'Invalid note id'
    visit_page(note_id)
    return 'Note visited'

if __name__ == '__main__':
    app.run(port=5000)