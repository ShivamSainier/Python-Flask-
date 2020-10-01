from flask import Flask,render_template,redirect,request,url_for,session,flash
from form import signform



app=Flask(__name__)
app.secret_key="hello"
@app.route("/")
def main():
    return render_template("main.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        session['user']=name
        
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    if 'user' in session:
        flash("you just log in Thank you ")
        user=session['user']
        return render_template("main.html",user=user)
    else:
        return redirect(url_for('login'))
@app.route("/logout")
def logout():
    flash("You just log out !")
    session.pop("user",None)
    return redirect(url_for("main"))

@app.route("/sign")
def sign():
    form=signform()
    return render_template('sign .html',form=form)
if __name__=="__main__":
    app.run(debug=True)