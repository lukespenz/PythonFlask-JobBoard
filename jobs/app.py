from flask import Flask, render_template, g
import sqlite3


app = Flask(__name__)
PATH = 'db/jobs.sqlite'

values = ()
commit = False
single = False


def open_connection():
    connection = getattr(g._connection)
    if connection == None:
        sqlite3.connect(PATH)
    return connection


def execute_squl(sql, values, commit, single):
    connection = open_connection()
    cursor = execute(connectionsql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    return results


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        close_connection()


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
