from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect("database.db")
print("Opened Database")
# connected to the database

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created')
# creating table - do something

# closing connection
connection.close()

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/new')
def new_post():
    return render_template("new.html")

@app.route('/addrecord', methods = ['POST'])
def addrecord():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    # function that lets us write in the database

    try:
        title = request.form['title']
        # creating new variable named title and gradding the title from the html
        post = request.form['post']
        # same as above
        cursor.execute('INSERT INTO posts (title,post) VALUES (?,?)', (title,post))
        # insert the form from html page
        connection.commit()
        # actually change the database
        message = "Record successfully added"

    except:
        connection.rollback()
        # don't do anything to the db if it throws an error
        message = "error in insert operation"
    finally:
        return render_template('result.html', message = message)
        connection.close()
