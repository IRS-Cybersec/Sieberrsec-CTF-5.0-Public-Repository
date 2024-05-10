from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def list_titles():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        query = "SELECT title FROM songs"
        cur.execute(query)
        found = cur.fetchall()
        for i in range(len(found)):
            found[i] = found[i][0]
        return found


def select(title):
    # query the database
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        query = f"SELECT link FROM songs WHERE title='{title}'"
        
        try:
            cur.execute(query)
            found = cur.fetchone()[0]
        except:
            return 'an error occured'

        return found

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        link = select(title)
        titles = list_titles()
        if link == 'an error occured':
            return render_template("index.html", error=link,titles=titles)
        return render_template("index.html", link=link,titles=titles)
    titles = list_titles()
    return render_template("index.html",titles=titles)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
