from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy as sql

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run()