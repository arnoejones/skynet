import io
from flask import send_file
import dash
import flask
import tempfile
from flask import render_template
from werkzeug.utils import redirect
from app import queriesdictionary
from app.queriesdictionary import QueriesDictionary
from app import flask_server
from app import layout
from app import sqlconnect
from app.config import Config
from app.forms import RadioFormClass, SqlQuery, SqlDescription
import dash_bootstrap_components as dbc
import pandas as pd

dash_app = dash.Dash(__name__, server =flask_server, url_base_pathname='/dash/', external_stylesheets=[dbc.themes.BOOTSTRAP])

dash_app.layout = layout.server_layout
# dash_app.css.append_css({'external_url': 'static/styles.css'})
dash_app.css.append_css({'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'})


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
        # Config.description = Config.radio_query[0]
        # print('****---- is this the description? ', form.radio.choices)
        counter = 0
        query_list = QueriesDictionary.queries(queriesdictionary)
        for t in query_list:
            if Config.radio_query[-1] in t:
                sqlconnect.fill_qd(t[1])
                sqlconnect.fill_qraw(t[0])
                print('**********************************************************', t[1])

        #
        # for t in form.radio.choices:
        #     if Config.radio_query[-1] in t:
        #         print('**********************************************************',t.counter)
            counter +=1

        return redirect('/dash') # do this if a button was selected, otherwise
    return flask.render_template('radio.html', form=form)  # stay on the radio page until you get it right


@flask_server.route('/custom', methods=['GET','POST'])
def custom():
    # return redirect('/custom')
    return render_template('custom.html')


@flask_server.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

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



@flask_server.route('/raw_sql_query', methods=['GET','POST'])
def query_display():
    form = SqlQuery()
    return render_template('raw_sql_query.html', form=form)

@flask_server.route('/sql_description', methods=['GET','POST'])
def description_display():
    form = SqlDescription()
    return render_template('sql_description.html', form=form)
#
# qd = ['']
#
# def fill_qd(z):
#     qd[0] = z
#     print('**** qd: ', qd)
#
# def query_desc():
#     return qd