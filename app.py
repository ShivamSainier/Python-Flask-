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
    Image=db.Column(db.String(40),nullable=False)
    posts=db.relationship('posts',backref='author',lazy=True)

class posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.Text,nullable=False)
    Content=db.Column(db.Text,nullable=False)
    Date_posted=db.Column(db.DateTime,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/user")
def user():
    if 'user' in session:
        flash("you just log in Thank you ")
        user=session['user']
        return render_template("main.html",user=user)
    else:
        return redirect(url_for('login'))


@app.route("/resister",methods=["GET","POST"])
def resister():
    sign_up=resister_form()
    if sign_up.validate_on_submit():
    
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