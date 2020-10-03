from wtforms import StringField , PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from flask_wtf import FlaskForm



class resister_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=6)])
    pasword=PasswordField("password",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    confirm_password=PasswordField("confirm_password",validators=[DataRequired(),EqualTo('pasword')])
    submit=SubmitField('submit')

    def validation_username(self,username):
        use=user.query.filter_by(Username=username.data).first()
        if use:
            raise ValidationError("it is already exist try something new")


class login_form(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=3,max=6)])
    password=StringField("password",validators=[DataRequired()])
    submit=SubmitField("log in")