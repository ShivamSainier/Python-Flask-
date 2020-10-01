from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class resister_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=6)])
    pasword=StringField("password",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    confirm_password=StringField("confirm_password",validators=[DataRequired(),EqualTo('pasword')])
    submit=SubmitField('sign up')


class login_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=6)])
    password=StringField("password",validators=[DataRequired()])
    submit=SubmitField("log in")