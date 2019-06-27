import io
from flask import send_file
import dash
import flask
import tempfile
from flask import render_template
from werkzeug.utils import redirect

from app import flask_server
from app import layout
from app import sqlconnect
from app.config import Config
from app.forms import RadioFormClass

import pandas as pd

dash_app = dash.Dash(__name__, server =flask_server, url_base_pathname='/dash/')


dash_app.layout = layout.server_layout
dash_app.css.append_css({'external_url': 'static/styles.css'})


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

@dash_app.server.route("/download_excel/")
def download_excel():
    f = tempfile.NamedTemporaryFile(mode='w+b', delete=False)

    df = Config.df

    # Convert DF
    buf = io.BytesIO()
    excel_writer = pd.ExcelWriter(buf, engine="xlsxwriter")
    df.to_excel(excel_writer, sheet_name="sheet1")
    excel_writer.save()
    excel_data = buf.getvalue()
    buf.seek(0)

    return send_file(
        buf,
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        attachment_filename=f.name + ".xlsx",
        as_attachment=True,
        cache_timeout=0
    )
