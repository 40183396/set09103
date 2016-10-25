from flask import Flask
from flask import Flask, flash, session, redirect, url_for, abort, request, render_template
import os

app = Flask(__name__)

books =[['EastOfEden.jpg','East of Eden','John Steinbeck'],
        ['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway'],
        ['Catch22.jpg','Catch-22','Joseph Heller'],
        ['TheGrapesOfWrath.jpg', 'The Grapes of Wrath', 'John Steinbeck']]

test = [['testCover', 'testName', 'testAuthor']]
eden = [['EastOfEden.jpg','East Of Eden','John Steinbeck']]
bell = [['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway']]
catch = [['Catch22.jpg','Catch-22','Joseph Heller']]
grape = [['TheGrapesOfWrath.jpg', 'The Grapes of Wrath', 'John Steinbeck']]

# route for catalogue of books
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('catalogue.html', root = books)

@app.route('/book/')
@app.route('/book/<name>')
def book(name):
    if name == "East of Eden":
          return render_template('book.html', name=name, root = eden)
    if name == "For Whom The Bell Tolls":
          return render_template('book.html', name=name, root = bell)
    if name == "Catch-22":
          return render_template('book.html', name=name, root = catch)
    if name == "The Grapes of Wrath":
          return render_template('book.html', name=name, root = grape)



    else:
          return render_template('book.html', name=name, root=test)
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
