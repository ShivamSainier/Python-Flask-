from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/users'
db=SQLAlchemy(app)


from flaskblog import routes
