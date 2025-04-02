# app/api/v1/auth/login.py
from flask import Blueprint, request, jsonify
from app.services.aws_session import store_credentials

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    aws_access_key_id = data.get("aws_access_key_id")
    aws_secret_access_key = data.get("aws_secret_access_key")
    region = data.get("aws_region", "us-west-2")

    if not all([aws_access_key_id, aws_secret_access_key]):
        return jsonify({"error": "Missing credentials"}), 400

    try:
        expires_at = store_credentials(aws_access_key_id, aws_secret_access_key, region)
        return jsonify({"expires_at": expires_at.isoformat()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500