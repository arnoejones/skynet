from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, Label

from app import queriesdictionary, sqlconnect
from app.queriesdictionary import QueriesDictionary


class RadioFormClass(FlaskForm):
    query_list = QueriesDictionary.queries(queriesdictionary)
    radio = RadioField(label='MyRadio', choices=query_list)
    submit = SubmitField('Do the Query')

class SqlQuery(FlaskForm):
    query = sqlconnect.query_raw()
    label = Label(text=[query], field_id=0)



class SqlDescription(FlaskForm):
    query = sqlconnect.query_desc()
    label = Label(text=[query], field_id=0)
