from flask import Flask, render_template, request, \
      redirect, url_for, session, flash, g
from flask_login import (LoginManager, current_user, login_required, \
                          login_user, logout_user, UserMixin, \
                          confirm_login, fresh_login_required)
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from form import LoginForm, RegisterForm
import bcrypt
#import sqlite3
#import sqlalchemy

# creates app object
app = Flask(__name__)
#bcrypt = bcrypt(app)

#app.secret_key = "-my-secret-key"
#app.database = "sample.db"
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'

# config
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
login_manager = LoginManager()
#login_manager.init_app(app)

from models import *
from form import LoginForm

#login_manager.login_view = "user.login"

valid_name = 'admin'
valid_password = 'admin'
def check_auth(name, password):
    if(name == valid_name and password == valid_password):
        return True
    return False

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
          valid_pwhash = bcrypt.hashpw(user.password, bcrypt.gensalt())
          if user is not None and request.form['password']==user.password:
          #bcrypt.hashpw(user.password.encode('utf-8'),valid_pwhash):
          #if check_auth(request.form['username'], request.form['password']):
                session['logged_in'] = True
               # login_user(user)
                flash('You have successfully logged in!')
                return redirect(url_for('root'))
          else:
                error = 'Invalid username or password. Please try again'

        else:
               render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form, error=error)

@app.route('/logout')
def logout():
   # logout_user()
    session.pop('logged_in', None)
    flash('You logged out successfully')
    return redirect(url_for('welcome'))

@login_manager.user_loader
def load_user(id):
   # return User.query.filter(User.id == int(user_id)).first()
    u = User.query.get(id)
    return Username(u.name, u.email, u.password)
#def connect_db():
 #   return sqlite3.connect(app.database)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        #login_user(user)
        return redirect(url_for('welcome'))
    return render_template('register.html', form = form)

@app.route('/user/<name>')
@login_required
def user(name):
    user = User.query.filter_by(name=name).first()
    if user == None:
        flash('User %s is not in database.' % name)
        return redirect(url_for('welcome'))
    posts = [
      {'author:': user, 'body': 'test post ~1'},
      {'author:': user, 'body': 'test post #2'}
    ]
    return render_template('user.html',
                          user=user,
                          posts=posts)
if __name__ == '__main__':
      app.run(host='0.0.0.0')
