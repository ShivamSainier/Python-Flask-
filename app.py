from flask import Flask,render_template,redirect,request,url_for,session,flash
from form import resister_form,login_form



app=Flask(__name__)
app.secret_key="hello"
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
        return redirect(url_for('main'))
    return render_template('resister.html',sign_up=sign_up)

@app.route('/login',methods=["GET","POST"])
def login():
    l=login_form()
    if l.validate_on_submit():
        flash("You just logged in !!")
        return redirect(url_for('main'))
    else:
        return render_template("login.html",l=l)


if __name__=="__main__":
    app.run(debug=True)