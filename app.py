import string
import random
import sqlite3 as sql
from flask import Flask, render_template, request

app = Flask(__name__)

# Show home in page
home = True


def get_key():
    # Connect db
    con = sql.connect("EDMTDictionary.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    # Validate key
    while True:
        # Keyword
        key = ''.join((random.choice(string.ascii_uppercase)
                      for x in range(2)))
        # Get rows from database
        cur.execute("SELECT * FROM Word WHERE Word LIKE ?",
                    ("%" + key + "%",))
        rows = cur.fetchall()
        if rows:
            break
    return key


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/play', methods=['GET', 'POST'])
def play():

    if request.method == 'POST':
        # Get variables
        answer = request.form.get('answer')
        key = request.form.get('key')

        # Connect db
        con = sql.connect("EDMTDictionary.db")
        con.row_factory = sql.Row
        cur = con.cursor()

        # Get answer from database
        cur.execute("SELECT * FROM Word WHERE Word LIKE ?",
                    ("%" + key + "%",))
        rows = cur.fetchall()

        # Validate answer
        for row in rows:
            if answer.upper() == row["word"].upper():
                return render_template("result.html", home=home, result="You succeeded!")

        return render_template("result.html", home=home, result="You failed:(")

    else:
        # Get key
        key = get_key()
        return render_template("play.html", key=key, home=home)


@app.route('/failed')
def failed():
    return render_template("failed.html", home=home)


@app.route('/help')
def help():
    return render_template("help.html", home=home)
