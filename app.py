from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        return redirect(url_for('show',name=name))
    else:
        return render_template("login.html")


@app.route("/<name>")
def show(name):
    return f"<h1>{name}</h1>"

if __name__=="__main__":
    app.run(debug=True)