from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models. Planet import Planet

api = Blueprint("api/planet", __name__)

@api.route("/")
def get_planet():
        all_planets = Planet.query.all()
        all_planets = list(map(lambda x: x.serialize(), all_planets))
        return jsonify ({"all_planets": all_planets})
    

@api.route("/<planet_id>")
def get_planet(planet_id):
    planet = planet.query.get(planet_id)
    return jsonify ({"usuario": planet.serialize()})


@api.route("/create", methods=["POST"])
def resgister():
    body = request.get_json()
    nuevo_planeta = Planet()
    nuevo_planeta.name = body["name"]
    nuevo_planeta.terrain = body["terrain"]
    nuevo_planeta.climate = body["climate"]
    nuevo_planeta.is_active = True

    db.session.add(nuevo_planeta)
    db.session.commit()

    return jsonify({"planeta": nuevo_planeta.serialize()})
