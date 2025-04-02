# app/api/v1/ecs/clusters.py
from flask import Blueprint, request, jsonify
from app.services.aws_session import get_session

ecs_blueprint = Blueprint('ecs', __name__)

@ecs_blueprint.route('/api/v1/ecs/clusters', methods=['GET'])
def list_clusters():
    aws_access_key_id = request.headers.get('AWSAccessKeyId')
    region = request.headers.get('AWSRegion', 'us-west-2')

    session = get_session(aws_access_key_id, region)
    if not session:
        return jsonify({'error': 'Session expired or invalid'}), 401

    ecs_client = session.client('ecs')
    clusters_info = []

    try:
        cluster_arns = ecs_client.list_clusters()['clusterArns']
        if cluster_arns:
            described = ecs_client.describe_clusters(clusters=cluster_arns)['clusters']
            for cluster in described:
                clusters_info.append({
                    'cluster_name': cluster['clusterName'],
                    'cluster_arn': cluster['clusterArn'],
                    'status': cluster['status'],
                    'registered_container_instances_count': cluster['registeredContainerInstancesCount'],
                    'running_tasks_count': cluster['runningTasksCount'],
                    'pending_tasks_count': cluster['pendingTasksCount'],
                })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'clusters': clusters_info})