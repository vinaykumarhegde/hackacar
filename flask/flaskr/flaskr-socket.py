from gevent import monkey 
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect

#import requests , json
from socketIO_client import SocketIO, LoggingNamespace
#import requests
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

def location_fuel():
    # placeholder for requests 
    # json 

    # "ObserverHub "

    headers = {'MojioAPIToken': '6ae1f07c-6db7-4a49-b458-2a1ffdfdc52e'} 
    r = requests.get("https://api.moj.io:443/v1/Events/", headers=headers)

    l= r.json()[u'Data'][0]
    print l
    location = l['Location']
    latitude =  l[u'Location'][u'Lat']
    longitude =  l[u'Location'][u'Lng' ]
    fuel = u'FuelLevel'
    j = { u'Lat': latitude, u'Lng' : str(longitude) , u"FuelLevel" : str(l[fuel]) }
    return str(j) #flask.jsonify(**j)

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0


    while True:
        time.sleep(5)
        count += 1
        socketio.emit('my response',
                      {'data': str(location_fuel()), 'count': count},
                      namespace='/test')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')


@socketio.on('my event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('close room', namespace='/test')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', namespace='/test')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('disconnect request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


### our data
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





## end our data


if __name__ == '__main__':
    socketio.run(app)