from flask import Flask, redirect, url_for, abort, request, render_template
app = Flask(__name__)

@app.route("/")
def root():
    dict = {'East Of Eden':'John Steinbeck'}
    return render_template('catalogue.html', root = dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
