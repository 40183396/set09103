from flask import Flask, redirect, url_for, abort, request, render_template
app = Flask(__name__)

@app.route("/")
def root():
    dict = {'East Of Eden':'John Steinbeck',
    'For Whom The Bell Tolls':'Ernest Hemingway',
    'Catch-22':'Joseph Heller'}
    return render_template('catalogue.html', root = dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
