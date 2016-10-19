from flask import Flask, redirect, url_for, abort, request, render_template
app = Flask(__name__)

# route for catalogue of books
@app.route("/home")
def root():
    dict =[['EastOfEden.jpg','East Of Eden','John Steinbeck'],
    ['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway'],
    ['Catch22.jpg','Catch-22','Joseph Heller']]
    return render_template('catalogue.html', root = dict)

# route for log in
#https://realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page/
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': error = 'Invalid Username or Password. Try again.'
        else:
              return redirect(url_for('root'))
    return render_template('login.html', error=error)

# redirect for 404
@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
