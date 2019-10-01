#  The Flask application instance is called app and is a member of the app package.
#  The from app import app statement imports the app variable that is a member of the app package.
from app import flask_server

if __name__ == '__main__':
    flask_server.run(debug=True, host='0.0.0.0' )  # lets me run http://10.213.81.6:8050/