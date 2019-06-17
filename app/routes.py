import dash
import flask
from flask import render_template
from werkzeug.utils import redirect
import dash_core_components as dcc
import dash_html_components as html
from app import flask_server
from app import layout
from app import sqlconnect
from app.config import Config
from app.forms import RadioFormClass

dash_app = dash.Dash(__name__, server =flask_server, url_base_pathname='/dash/')
dash_app.layout = layout.server_layout

@flask_server.route('/', methods=['GET','POST'])
@flask_server.route('/home')
def home():
    return render_template('home.html')


@flask_server.route('/radio', methods=['GET','POST'])
def radio():
    form = RadioFormClass()
    if form.validate_on_submit():
        # HERE'S THE QUERY!!!'
        Config.radio_query.append(form.radio.data)
        Config.df = sqlconnect.getData(Config.radio_query[-1])

        return redirect('/dash') # do this if a button was selected, otherwise
    return flask.render_template('radio.html', form=form)  # stay on the radio page until you get it right

