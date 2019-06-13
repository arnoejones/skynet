from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField

from app import queriesdictionary
from app.queriesdictionary import QueriesDictionary


class RadioFormClass(FlaskForm):
    query_list = QueriesDictionary.queries(queriesdictionary)
    radio = RadioField(label='MyRadio', choices=query_list)
    submit = SubmitField('Do the Query')