from wtforms import StringField , PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed 
from flaskblog.models import user,posts


class resister_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=2,max=12)])
    password=PasswordField("password",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    confirm_password=PasswordField("confirm_password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('submit')
    
    def validation_username(self,username):
        user=user.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("it is already exist try something new")
    def validation_email(self,email):
        userr=user.query.filter_by(email=email.data).first()
        if userr:
            raise ValidationError("it is already exist try something new")


class login_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=12)])
    password=StringField("password",validators=[DataRequired()])
    submit=SubmitField("log in")


class update_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=13)])
    email=StringField("email",validators=[DataRequired(),Email()])
    picture=FileField('update profile picture',validators=[FileAllowed(['jpg','png','gif','MPEG','HEIC'])])
    submit=SubmitField("UPDATE")

    def validation_username(self,username):
        if username.data !=current_user.username:
            raise ValidationError("it is already exist try something new")
    def validation_email(self,email):
        if email.data!=current_user.email:
            raise ValidationError("it is already exist try something new")

class post_form(FlaskForm):
    title=StringField('title',validators=[DataRequired()])
    content=TextAreaField('content',validators=[DataRequired()])
    submit=SubmitField('Post')