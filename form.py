from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class signform(FlaskForm):
    username=StringField('Username')
    password=PasswordField("password")
    submit=SubmitField('sign up')