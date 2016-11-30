from flask import Flask, render_template, request, \
      redirect, url_for, session, flash, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

#from flask.ext.bcrypt import Bcrypt
#import sqlite3
#import sqlalchemy

# creates app object
app = Flask(__name__)
#bcrypt = Bcrypt(app)

#app.secret_key = "-my-secret-key"
#app.database = "sample.db"
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'

# config
app.config.from_object('config.DevelopmentConfig')
#db = SQLAlchemy(app)

from models import *
from form import LoginForm

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You must login')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def root():
    ##sqlie3 database queries
    #g.db = connect_db()
    #cursor = g.db.execute('select * from posts')
    #posts = [dict(title=row[0], description=row[1]) for row in cursor.fetchall()]
    #g.db.close()
    ##sqlAlchemy query is much easier
    posts = db.session.query(WallPost).all()
    return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
          user = User.query.filter_by(name=request.form['username']).first()
          if not user or not user.verify_password(password):
           # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid username or password. Please try again'
          else:
                session['logged_in'] = True
                flash('You have successfully logged in!')
                return redirect(url_for('root'))
        else:
            render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form, error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You logged out successfully')
    return redirect(url_for('welcome'))

#def connect_db():
 #   return sqlite3.connect(app.database)

if __name__ == '__main__':
      app.run(host='0.0.0.0')
