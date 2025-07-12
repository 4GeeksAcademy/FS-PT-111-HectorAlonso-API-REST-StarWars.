from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models.User import User

api = Blueprint("api/user", __name__)

@api.route("/")
def get_users():
        all_users = User.query.all()
        all_users = list(map(lambda x: x.serialize(), all_users))
        return jsonify ({"all_users": all_users})
    

@api.route("/<user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify ({"usuario": user.serialize()})


@api.route("/create", methods=["POST"])
def resgister():
    body = request.get_json()
    nuevo_usuario = User()
    nuevo_usuario.email = body["email"]
    nuevo_usuario.password = body["password"]
    nuevo_usuario.is_active = True

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"usuario": nuevo_usuario.serialize()})
