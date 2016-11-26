import ConfigParser
import os
import sqlite3
from flask import Flask, render_template, session, flash, redirect, g
app = Flask(__name__)
from forms import LoginForm
secret_key = 'my-secret-key'
prov = [{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
        {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
        {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
        {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

db_location = 'database.db'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mohs'} # example useri
    posts = [ # fake array posts
      {
        'author': {'nickname': 'Steven'},
        'body': 'Hello Edinburgh!'
      },
      {
        'author': {'nickname': 'Sophie'},
        'body': 'Going out tonight!'
      },
      {
        'author': {'nickname': 'Jen'},
        'body': 'Im so cold :('
      }
    ]
    return render_template('index.html',
                          title='Home',
                          user=user,
                          posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    config = ConfigParser.ConfigParser()
    config_location = "etc/defaults.cfg"
    config.read(config_location)
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openif.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                          title = 'Sign In',
                          form=form,
                          providers= prov)


def init(app):
    config = ConfigParser.ConfigParser()
    try:
        config_location = "etc/defaults.cfg"
        config.read(config_location)
        app.config['openid_providers'] = config.get("config", "OPENID_PROVIDERS")
        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print "Could not read configs from ", config_location
if __name__ == "__main__":
    init(app)
    app.run(
        host=app.config['ip_address'],
        port=int(app.config['port']))
