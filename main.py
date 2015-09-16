from bottle import Bottle
from bottle import template
from bottle import route, request
# import sqlite3

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@bottle.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@bottle.route('/hello/<name>')
def greet(name='Stranger'):
    if (name=="secret"):
        return 'You guessed it'
    else:
        return template('Hello {{name}}, how are you?', name=name)


@bottle.route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@bottle.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    if (username == "1"):
        return True
    else:
        return False

@bottle.route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'
