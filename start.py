from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:qwerty1234@localhost-VirtualBox/demo'
db = SQLAlchemy(app)


class Client (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)


class Agreement (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey(""))


@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")

@app.route("/main", methods=["GET"])
def main():
    return render_template("main.html", clients=clients)

@app.route("/add_client", methods=["POST"])
def add_client():
    name = request.form["name"]
    agreement = request.form["agreement"]

    clients.append(Client(name, agreement))

    return redirect(url_for("main"))
