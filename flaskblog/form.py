from wtforms import StringField , PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from flask_wtf import FlaskForm
from flaskblog.models import user,posts


class resister_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=6)])
    password=PasswordField("password",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    confirm_password=PasswordField("confirm_password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('submit')
    def validation_username(self,username):
        userr=user.query.filter_by(username=username.data).first()
        if userr:
            raise ValidationError("it is already exist try something new")
    def validation_email(self,email):
        userr=user.query.filter_by(email=email.data).first()
        if userr:
            raise ValidationError("it is already exist try something new")


class login_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=6)])
    password=StringField("password",validators=[DataRequired()])
    submit=SubmitField("log in")