# app/services/aws_session.py
import boto3
from datetime import datetime, timedelta

_sessions = {}

def store_credentials(aws_access_key_id, aws_secret_access_key, region):
    session_key = f"{aws_access_key_id}:{region}"
    now = datetime.utcnow()

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )

    _sessions[session_key] = {
        'session': session,
        'created_at': now
    }

    return now + timedelta(minutes=5)

def get_session(aws_access_key_id, region):
    session_key = f"{aws_access_key_id}:{region}"
    session_data = _sessions.get(session_key)

    if session_data:
        age = datetime.utcnow() - session_data['created_at']
        if age < timedelta(minutes=5):
            return session_data['session']
        else:
            _sessions.pop(session_key)
    return None