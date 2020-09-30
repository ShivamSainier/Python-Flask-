from flask import Flask,render_template,redirect,request,url_for,session


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
        user=session['user']
        return render_template("main.html",user=user)
    else:
        return redirect(url_for('login'))
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("main"))

if __name__=="__main__":
    app.run(debug=True)