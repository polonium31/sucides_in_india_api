from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://buakmnshklnegn:149d9e91d1ac0c5377cffdc86a619c67a5163c01a0b4602e4c68c8c9aa421d34@ec2-3-89-0-52.compute-1.amazonaws.com:5432/d8fk4958unmjc7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TABLE Configuration
class Suicides(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String)
    year = db.Column(db.Integer)
    type_code = db.Column(db.String)
    type = db.Column(db.String)
    gender = db.Column(db.String)
    age_group = db.Column(db.String)
    total = db.Column(db.Integer)


db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def get_all():
    suicides = db.session.query(Suicides).all()
    suicides_list = []
    for suicide in suicides:
        suicides_dict = {
            "id": suicide.id,
            "state": suicide.state,
            "year": suicide.year,
            "type_code": suicide.type_code,
            "type": suicide.type,
            "gender": suicide.gender,
            "age_group": suicide.age_group,
            "total": suicide.total,

        }
        suicides_list.append(suicides_dict)
    all_suicides = {"suicides": suicides_list}
    all_suicides_json = jsonify(suicides=all_suicides["suicides"])
    return all_suicides_json


@app.route("/search")
def search():
    state = request.args.get("state")
    suicides = db.session.query(Suicides).filter_by(state=state)

    suicides_list = []
    for suicide in suicides:
        suicides_dict = {
            "id": suicide.id,
            "state": suicide.state,
            "year": suicide.year,
            "type_code": suicide.type_code,
            "type": suicide.type,
            "gender": suicide.gender,
            "age_group": suicide.age_group,
            "total": suicide.total,

        }
        suicides_list.append(suicides_dict)
    if len(suicides_list) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have data for the given state."}), 404

    all_suicides = {"suicides": suicides_list}
    all_suicides_json = jsonify(suicides=all_suicides["suicides"])
    return all_suicides_json


@app.route("/gender")
def gender_search():
    gender = request.args.get("gen")

    suicides_by_gender = db.session.query(Suicides).filter_by(gender=gender)

    suicides_list_by_gender = []
    for suicide in suicides_by_gender:
        suicides_dict = {
            "id": suicide.id,
            "state": suicide.state,
            "year": suicide.year,
            "type_code": suicide.type_code,
            "type": suicide.type,
            "gender": suicide.gender,
            "age_group": suicide.age_group,
            "total": suicide.total,

        }
        suicides_list_by_gender.append(suicides_dict)
    if len(suicides_list_by_gender) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have data for the given Gender."}), 404

    all_suicides = {"suicides": suicides_list_by_gender}
    all_suicides_json = jsonify(suicides=all_suicides["suicides"])
    return all_suicides_json


@app.route("/year")
def find_year():
    year = request.args.get("year")

    suicides_by_year = db.session.query(Suicides).filter_by(year=year)

    suicides_list_by_year = []
    for suicide in suicides_by_year:
        suicides_dict = {
            "id": suicide.id,
            "state": suicide.state,
            "year": suicide.year,
            "type_code": suicide.type_code,
            "type": suicide.type,
            "gender": suicide.gender,
            "age_group": suicide.age_group,
            "total": suicide.total,

        }
        suicides_list_by_year.append(suicides_dict)
    if len(suicides_list_by_year) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have data for the given year."}), 404

    all_suicides = {"suicides": suicides_list_by_year}
    all_suicides_json = jsonify(suicides=all_suicides["suicides"])
    return all_suicides_json


@app.route("/type_code")
def type_code():
    type_code_for_death = request.args.get("type")

    suicides_by_type = db.session.query(Suicides).filter_by(type_code=type_code_for_death)

    suicides_list_by_type = []
    for suicide in suicides_by_type:
        suicides_dict = {
            "id": suicide.id,
            "state": suicide.state,
            "year": suicide.year,
            "type_code": suicide.type_code,
            "type": suicide.type,
            "gender": suicide.gender,
            "age_group": suicide.age_group,
            "total": suicide.total,

        }
        suicides_list_by_type.append(suicides_dict)
    if len(suicides_list_by_type) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have data for the given type."}), 404

    all_suicides = {"suicides": suicides_list_by_type}
    all_suicides_json = jsonify(suicides=all_suicides["suicides"])
    return all_suicides_json


@app.route("/age_group")
def by_age():
    age = request.args.get("age")
    if age == '60plus':
        age = '60+'
    if age == '0-100':
        age = '0-100+'

    suicides_by_age = db.session.query(Suicides).filter_by(age_group=age)

    suicides_list_by_age = []
    for suicide in suicides_by_age:
        suicides_dict = {
            "id": suicide.id,
            "state": suicide.state,
            "year": suicide.year,
            "type_code": suicide.type_code,
            "type": suicide.type,
            "gender": suicide.gender,
            "age_group": suicide.age_group,
            "total": suicide.total,

        }
        suicides_list_by_age.append(suicides_dict)
    if len(suicides_list_by_age) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have data for the given type."}), 404

    all_suicides = {"suicides": suicides_list_by_age}
    all_suicides_json = jsonify(suicides=all_suicides["suicides"])
    return all_suicides_json


if __name__ == '__main__':
    app.run()
