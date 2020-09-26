from flask import Flask ,render_template,redirect,url_for

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    names=['Shivam','Shubham','rohit']
    return render_template("about.html",names=names)


if __name__=="__main__":
    app.run(debug=True)