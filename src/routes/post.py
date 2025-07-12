from flask import Flask, request, jsonify, Blueprint


api = Blueprint("api/post", __name__)

@api.route("/")
def get_post():
    return jsonify ("todos los posts")