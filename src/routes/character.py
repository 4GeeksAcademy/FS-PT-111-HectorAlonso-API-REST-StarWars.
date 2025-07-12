from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models. Character import Character

api = Blueprint("api/character", __name__)

@api.route("/")
def get_character():
        all_characters = Character.query.all()
        all_characters = list(map(lambda x: x.serialize(), all_characters))
        return jsonify ({"all_characters": all_characters})
    

@api.route("/<character_id>")
def get_character(character_id):
    character = character.query.get(character_id)
    return jsonify ({"usuario": character.serialize()})


@api.route("/create", methods=["POST"])
def resgister():
    body = request.get_json()
    nuevo_personaje = Character()
    nuevo_personaje.name = body["name"]
    nuevo_personaje.planet_origin = body["planet"]
    nuevo_personaje.is_active = True

    db.session.add(nuevo_personaje)
    db.session.commit()

    return jsonify({"personaje": nuevo_personaje.serialize()})
