from flask import Flask,render_template,redirect,request,url_for,session,flash
from form import resister_form,login_form
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/users'
db=SQLAlchemy(app)

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Username=db.Column(db.String(20),nullable=False)
    Email=db.Column(db.String(120),nullable=False)
    Password=db.Column(db.String(20),nullable=False)


class posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text,nullable=False)
    content=db.Column(db.Text,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False)


@app.route("/")
def main():
    return render_template("main.html")



@app.route("/resister",methods=["GET","POST"])
def resister():
    sign_up=resister_form()
    if sign_up.validate_on_submit():
        userr=user(Username=sign_up.username.data,Email=sign_up.email.data,Password=sign_up.pasword.data)
        db.session.add(userr)
        db.session.commit()
    
        flash("You just Resistered!!")
        return redirect('/')
    return render_template('resister.html',sign_up=sign_up)

@app.route('/login',methods=["GET","POST"])
def login():
    l=login_form()
    if l.validate_on_submit():
        flash("You just logged in !!")
        return redirect("/")
    else:
        return render_template("login.html",l=l)


if __name__=="__main__":
    app.run(debug=True)