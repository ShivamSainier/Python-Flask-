from flask import render_template,redirect,request,url_for,session,flash
from flaskblog.form import resister_form,login_form
from flaskblog.models import user,posts
from flaskblog import app,db
from flask_login import login_user

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/resister",methods=["GET","POST"])
def resister():
    sign_up=resister_form()
    if sign_up.validate_on_submit():
        userr=user(username=sign_up.username.data,email=sign_up.email.data,password=sign_up.password.data)
        db.session.add(userr)
        db.session.commit()
        flash("You just Resistered!!")
        return redirect('/')
    return render_template('resister.html',sign_up=sign_up)


@app.route('/login',methods=["GET","POST"])
def login():
    l=login_form()
    if l.validate_on_submit():
        use=user.query.filter_by(username=l.username.data).first()
        pas=user.query.filter_by(password=l.password.data).first()
        if use and pas:
            login_user(use,pas)
            flash("You just logged in !!")
            return redirect("/")
        else:
            message="invalid username or password"
            return render_template("login.html",l=l,message=message)
    else:
        return render_template("login.html",l=l)
