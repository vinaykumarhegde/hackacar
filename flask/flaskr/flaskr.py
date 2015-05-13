# all the imports
import sqlite3, json, requests,time
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
#http://flask.pocoo.org/docs/0.10/tutorial/setup/#tutorial-setup
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


 #setting up the database: 
 #http://flask.pocoo.org/docs/0.10/tutorial/dbinit/#tutorial-dbinit
 #sqlite3 /tmp/flaskr.db < schema.sql

#def init_db():
#   with closing(connect_db()) as db:
#        with app.open_resource('schema.sql', mode='r') as f:
#            db.cursor().executescript(f.read())
#        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
	# placeholder for requests 
	# json
    
    return "home page! "
	#http://docs.python-requests.org/en/latest/

@app.route('/json')
def json():
    # placeholder for requests 
    # json 



    headers = {'MojioAPIToken': '6ae1f07c-6db7-4a49-b458-2a1ffdfdc52e'} 
    r = requests.get("https://api.moj.io:443/v1/Events/", headers=headers)

    l= r.json()[u'Data'][0]
    print l
    location = l['Location']
    latitude =  l[u'Location'][u'Lat']
    longitude =  l[u'Location'][u'Lng' ]
    fuel = u'FuelLevel'
    j = { u'Lat': latitude, u'Lng' : str(longitude) , u"FuelLevel" : str(l[fuel]) }
    return flask.jsonify(**j)
    #http://docs.python-requests.org/en/latest/



@app.route('/speak',methods=['POST'])
def speak():
    # get input of file - wait for file input
    #Text to speech >> (SERVER) >> sent to the page, 
    # if yes , ( show something )
    return "decision is:  "
    # if no , continue 
# @app.route('/')
# def show_entries():
#     cur = g.db.execute('select title, text from entries order by id desc')
#     entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
#     return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/hello')
def hello():
		# show a template 
    return 'Hello World'

#login system - not sure if necessary

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
