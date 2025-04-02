# app/api/v1/dashboard/summary.py
from flask import Blueprint, request, jsonify
from app.services.aws_session import get_session

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/api/v1/dashboard/summary', methods=['GET'])
def summary():
    aws_access_key_id = request.headers.get('AWSAccessKeyId')
    region = request.headers.get('AWSRegion', 'us-west-2')

    session = get_session(aws_access_key_id, region)
    if not session:
        return jsonify({'error': 'Session expired or invalid'}), 401

    # Placeholder values for now
    return jsonify({
        "summary": {
            "ecs": {
                "total_clusters": 1,
                "total_services": 3,
                "total_tasks": 25,
                "unhealthy_services": 0
            },
            "s3": "Coming soon",
            "ebs": "Coming soon",
            "network": "Coming soon"
        }
    })