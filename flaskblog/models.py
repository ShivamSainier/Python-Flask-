from flaskblog import db,login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False,unique=True)
    email=db.Column(db.String(120),nullable=False,unique=True)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(20),nullable=False)
    post=db.relationship('posts',backref='author',lazy=True)

    def __repr__(self):
        return f"user('{self.username}','{self.email}','{self.image_file}')"


class posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text,nullable=False)
    content=db.Column(db.Text,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=True)
    def __repr__(self):
        return f"user('{self.title}','{self.date_posted}')"