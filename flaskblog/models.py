from flaskblog import db


class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Username=db.Column(db.String(20),nullable=False,unique=True)
    Email=db.Column(db.String(120),nullable=False,unique=True)
    Password=db.Column(db.String(20),nullable=False,unique=True)


class posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text,nullable=False)
    content=db.Column(db.Text,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False)