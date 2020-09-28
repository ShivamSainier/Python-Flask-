from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/connectyou'
db=SQLAlchemy(app)
suscribers=[]

class blogger(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.Text,default="Name",unique=False,nullable=False)
    Title=db.Column(db.Text,default="Title",unique=False,nullable=False)
    Subtitle=db.Column(db.Text,default="Subtitle",unique=False,nullable=False)
    Discription=db.Column(db.Text,default="Discription",unique=False,nullable=False)
    Datetime=db.Column(db.DATETIME,default=datetime.utcnow)

@app.route("/")
def index():
    all_data = blogger.query.all()
    return render_template('index.html',all_data=all_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/vlogger",methods=["GET","POST"])
def vlogger():
    if request.method=="POST":
        name=request.form.get('name')
        title=request.form.get('title')
        subtitle=request.form.get('subtitle')
        description=request.form.get('description')
        entry=blogger(Name=name,Title=title,Subtitle=subtitle,Discription=description)
        db.session.add(entry)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("vlogger.html")

if __name__=="__main__":
    app.run(debug=True)