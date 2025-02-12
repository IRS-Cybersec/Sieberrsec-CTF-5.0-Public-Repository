from flask import Flask, request, render_template_string, render_template, make_response, redirect, url_for
import base64
from tinydb import TinyDB, Query, table
import uuid 
import re

app = Flask(__name__)

db = TinyDB('db.json')


# I added this filter so I wont get hacked anymore! Mwahahahaha
def filter(s):
    banned = ['req', 'url', 'get', 'sec', '+']
    if not re.fullmatch(r'[a-z|A-Z]+',s):
        return False
    for ban in banned:
        if ban in s.lower():
            return False
    return True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new', methods=['POST'])
def create():
    title = base64.b64encode(request.json['title'].encode()).decode()
    content = base64.b64encode(request.json['content'].encode()).decode()
    id = uuid.uuid4()
    db.insert(table.Document({'id': str(id), 'content': content, 'title': title}, doc_id=id.int))
    return make_response(str(id),200)

@app.route('/view/<id>')
def retrieve(id):
    User = Query()
    res = db.search(User.id == id)
    if res != []:
        content = base64.b64decode(res[0]['content']).decode()
        title = base64.b64decode(res[0]['title']).decode()
        if not filter(content) or not filter(title):
            return make_response("Invalid content", 400)
        return render_template_string(f'''<html><body><h1>{{{{{title}}}}}</h1>{{{{{content}}}}}<body></html>''')
    else:
        return make_response("Paste Not found", 404)

if __name__ == "__main__":
    app.run(debug=True)
