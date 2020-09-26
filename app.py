from flask import Flask ,url_for,render_template,redirect,url_for,request

app=Flask(__name__)

sucribe=[]

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    names=['Shivam','Shubham','rohit']
    return render_template("about.html",names=names)

@app.route("/form",methods=["POST"])
def form():
    first=request.form.get('firstname')
    email=request.form.get('email')
    sucribe.append((first,email))
    return render_template("form.html",sucribe=sucribe)

@app.route("/suscribe")
def suscribe():
    return render_template('suscribe.html')

if __name__=="__main__":
    app.run(debug=True)