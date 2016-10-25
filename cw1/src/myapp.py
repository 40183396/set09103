from flask import Flask
from flask import Flask, flash, session, redirect, url_for, abort, request, render_template
import os

app = Flask(__name__)

dict =[['EastOfEden.jpg','East Of Eden','John Steinbeck'],
        ['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway'],
        ['Catch22.jpg','Catch-22','Joseph Heller'],
        ['TheGrapesOfWrath.jpg', 'The Grapes of Wrath', 'John Steinbeck']]

# route for catalogue of books
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('catalogue.html', root = dict)

@app.route('/book/')
@app.route('/book/<name>')
def book(name=None):
    return render_template('book.html', name=name)

# route for log in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.form['username'] == 'admin' or request.form['password'] =='admin': 
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()

# redirect for 404
@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)
