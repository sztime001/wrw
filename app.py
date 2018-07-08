from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
db.session.add(User(username = 'admin', email = 'admin@admin.com'))
db.session.add(User(username = 'user1', email = 'user1@admin.com'))
db.session.commit()

@app.route('/add')
def adduser():
    name = request.args['name']
    email = request.args['email']
    db.session.add(User(username = name, email = email))
    db.session.commit()
    return "User {} has been added to database".format(name)

@app.route("/")
def helloworld():
    return "helloworld"

@app.route('/haha')
def haha():
    c = User.query.count()
    return "numbers of user in database is {}".format(c)
