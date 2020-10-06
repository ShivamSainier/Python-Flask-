from flask import render_template,redirect,request,url_for,session,flash,abort
from flaskblog.form import resister_form,login_form,update_form,post_form
from flaskblog.models import user,posts
from flaskblog import app,db
from flask_login import login_user,current_user,logout_user,login_required
import secrets
import os
from PIL import Image

@app.route("/")
def main():
    page=request.args.get('page',1,type=int)
    post=posts.query.order_by(posts.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template("main.html",post=post)



def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(app.root_path,'static',picture_fn)
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_fn)
    i.save(picture_path)
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

@app.route('/New_Post',methods=['GET','POST'])
def new_post():
    post=post_form()
    if post.validate_on_submit():
        flash("new post created")
        postss=posts(title=post.title.data,content=post.content.data,author=current_user)
        db.session.add(postss)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('New_Post.html',post=post,legend="new post")

@app.route('/userposts/<int:id>')
def userposts(id):
    post=posts.query.get_or_404(id)
    return render_template('user_posts.html',post=post)

@app.route("/userposts/<int:id>/update",methods=['GET','POST'])
@login_required
def update_post(id):
    p=posts.query.get_or_404(id)
    if p.author!=current_user:
        abort(403)
    post=post_form()
    if post.validate_on_submit():
        p.title=post.title.data
        p.content=post.content.data
        db.session.commit()
        flash("Update Successfully")
        return redirect(url_for('main',id=p.id))
    elif request.method=="GET":
        post.title.data=p.title
        post.content.data=p.content
        return render_template('New_Post.html',post=post,legend="update post")

@app.route('/userposts/<int:id>/delete',methods=["GET","POST"])
@login_required
def delete_post(id):
    post=posts.query.get_or_404(id)
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Delete Successfully")
    return redirect(url_for('main'))