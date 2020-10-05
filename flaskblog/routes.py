from flask import render_template,redirect,request,url_for,session,flash
from flaskblog.form import resister_form,login_form,update_form
from flaskblog.models import user,posts
from flaskblog import app,db
from flask_login import login_user,current_user,logout_user,login_required
import secrets
import os

@app.route("/")
def main():
    return render_template("main.html")



def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(app.root_path,'static',picture_fn)
    form_picture.save(picture_path)
    return picture_fn


@app.route("/resister",methods=["GET","POST"])
def resister():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
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
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    l=login_form()
    if l.validate_on_submit():
        use=user.query.filter_by(username=l.username.data).first()
        pas=user.query.filter_by(password=l.password.data).first()
        if use and pas:
            login_user(use,pas)
            next_page=request.args.get('next') 
            #flash("You just logged in !!")
            return redirect(next_page) if next_page else  redirect(url_for('main'))
        else:
            message="invalid username or password"
            return render_template("login.html",l=l,message=message)
    else:
        return render_template("login.html",l=l)

@app.route("/logout")
def logout():
    logout_user() 
    return redirect(url_for('main'))


@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    sign_up=update_form()
    image_file=url_for('static',filename=current_user.image_file)
    if sign_up.validate_on_submit():
        if sign_up.picture.data:
            picture_fn=save_picture(sign_up.picture.data)
            current_user.image_file=picture_fn
        current_user.username=sign_up.username.data
        current_user.email=sign_up.email.data
        db.session.commit()
        flash("Your account has been updated !")
        return redirect(url_for('account'))
    elif request.method=='GET':
        sign_up.username.data=current_user.username
        sign_up.email.data=current_user.email
    image_file=url_for('static',filename=current_user.image_file)
    return render_template('account.html',image_file=image_file,sign_up=sign_up)