from flask import Flask

app = Flask(__name__)
# this is my flask app
# two underscores are dunders
@app.route('/')
def index():
    # return 'Hello world!'
    return app.send_static_file('home.html')
    # this is a static file function built into flask
# setting up URL
# use export FLASK_APP=appname.py
@app.route('/about')
def about():
# name function whatever page is called
    # return "This is my about page!"
    return app.send_static_file('about.html')
@app.route('/contact')
def contact():
    # return '<h1>This is a big h1</h1>'
    return app.send_static_file("contact.html")
# takes this html and puts it right into the browser

# to add html put in static folder - must be called static
@app.route('/post/<postnum>')
def post1(postnum):
    return 'This is post ' + postnum
#this is similar to route params
#if you want interger for post num you can use <int:postnum>
