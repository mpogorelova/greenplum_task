from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:qwerty1234@localhost-VirtualBox/demo'
db = SQLAlchemy(app)


class Client (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)

    def __init__(self, name, agreements):
        self.name = name.strip()
        self.agreements = [
            Agreement(title=agreement.strip()) for agreement in agreements.split(",")
        ]


class Agreement (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024), nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    client = db.relationship("Client", backref=db.backref("agreements", lazy=True))


db.create_all()


@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")


@app.route("/main", methods=["GET"])
def main():
    return render_template("main.html", clients=Client.query.all())


@app.route("/add_client", methods=["POST"])
def add_client():
    name = request.form["name"]
    agreement = request.form["agreement"]

    db.session.add(Client(name, agreement))
    db.session.commit()

    return redirect(url_for("main"))
