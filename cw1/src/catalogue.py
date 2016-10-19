from flask import Flask, redirect, url_for, abort, request, render_template
app = Flask(__name__)

@app.route("/")
def root():
    dict =[['EastOfEden.jpg','East Of Eden','John Steinbeck'],
    ['ForWhomTheBellTolls.jpg','For Whom The Bell Tolls','Ernest Hemingway'],
    ['Catch22.jpg','Catch-22','Joseph Heller']]
    return render_template('catalogue.html', root = dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
