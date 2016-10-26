from flask import Flask
from flask import Flask, flash, session, redirect, url_for, abort, request, render_template
import os

app = Flask(__name__)

books =[['EastOfEden.jpg','East of Eden','John Steinbeck','601','Classics'],
        ['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway','480','Classics'],
        ['Catch22.jpg','Catch-22','Joseph Heller','453','Classics'],
        ['TheGrapesOfWrath.jpg', 'The Grapes of Wrath', 'John Steinbeck','479','Classics'],
        ['TheMartian.jpg', 'The Martian', 'Andy Weir', '369', 'Science Fiction'],
        ['TheCountOfMonteCristo.jpg', 'The Count of Monte Cristo', 'Alexandre Dumas','1276','Classics'],
        ['TheStranger.jpg', 'The Stranger', 'Albert Camus', '123', 'Philosophy'],
        ['TheGreatGatsby.jpg', 'The Great Gatsby', 'F. Scott Fitzgerald','180', 'Classics'],
        ]

test = [['testCover', 'testName', 'testAuthor']]
eden  = [['EastOfEden.jpg','East of Eden','John Steinbeck','601','Classics']]
bell =  [['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway','480','Classics']]
catch = [['Catch22.jpg','Catch-22','Joseph Heller','453','Classics']]
grape = [['TheGrapesOfWrath.jpg', 'The Grapes of Wrath', 'John Steinbeck','479','Classics']]
martian = [['TheMartian.jpg', 'The Martian', 'Andy Weir', '369', 'Science Fiction']]
cristo = [['TheCountOfMonteCristo.jpg', 'The Count of Monte Cristo', 'Alexandre Dumas','1276','Classics']]
stranger = [['TheStranger.jpg', 'The Stranger', 'Albert Camus', '123','Philosophy']]
gatsby  = [['TheGreatGatsby.jpg', 'The Great Gatsby', 'F. Scott Fitzgerald','180', 'Classics']]
        

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
    if name == "The Martian":
          return render_template('book.html', name=name, root = martian)
    if name == "The Count of Monte Cristo":
          return render_template('book.html', name=name, root = cristo)
    if name == "The Stranger":
          return render_template('book.html', name=name, root = stranger)
    if name == "The Great Gatsby":
          return render_template('book.html', name=name, root = gatsby)

    else:
          return render_template('book.html', name=name, root=test)

# route for log in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('home'))
    if request.form['username'] == 'admin' or request.form['password'] =='admin': 
        session['logged_in'] = True
        return redirect(url_for('home'))
    else:
        flash('wrong password')
    return home()

# redirect for logout
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

# redirect for 404
@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)
