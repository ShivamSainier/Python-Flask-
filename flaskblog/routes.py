from flask import render_template,redirect,request,url_for,session,flash
from flaskblog.form import resister_form
from flaskblog.models import user,posts
from flaskblog import app,db

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
