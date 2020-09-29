from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/connectyou'
db=SQLAlchemy(app)
suscribers=[]

class blogger(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text,default="Name",unique=False,nullable=False)
    title=db.Column(db.Text,default="Title",unique=False,nullable=False)
    subtitle=db.Column(db.Text,default="Subtitle",unique=False,nullable=False)
    discription=db.Column(db.Text,default="Discription",unique=False,nullable=False)
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
        if not name or not title or not subtitle or not description:
            message="please fill all forms field"
            return render_template("vlogger.html",message=message,name=name,title=title,subtitle=subtitle,description=description)
        else:
            entry=blogger(name=name,title=title,subtitle=subtitle,discription=description)
            db.session.add(entry)
            db.session.commit()
            return redirect("/")
    else:
        return render_template("vlogger.html")

@app.route("/delete/<int:id>")
def delete(id):
    delete=blogger.query.get_or_404(id)
    db.session.delete(delete)
    db.session.commit()
    return redirect("/") 


@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    vlogger=blogger.query.get_or_404(id)
    if request.method=="POST":
        vlogger.name=request.form.get('name')
        vlogger.title=request.form.get('title')
        vlogger.subtitle=request.form.get('subtitle')
        vlogger.discription=request.form.get('description')
        db.session.commit()
        return redirect("/")
    else:
        return render_template("update.html",vlogger=vlogger)






if __name__=="__main__":
    app.run(debug=True)