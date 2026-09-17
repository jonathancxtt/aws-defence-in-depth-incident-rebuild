import boto3
import json
from datetime import datetime, timezone
import uuid
import os

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(os.environ['DYNAMODB_TABLE_NAME'])

def lambda_handler(event, context):
    try:
        ct = datetime.now(timezone.utc).isoformat()
        submission_payload = json.loads(event['body'])

        submission = {
        "submission_id" : str(uuid.uuid4()),
        "name" : submission_payload.get('name', ''),
        "email" : submission_payload.get('email', ''),
        "message" : submission_payload.get('message', ''),
        "timestamp" : ct
        }

        table.put_item(Item=submission)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Submission received."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Failed to create item",
                "error": str(e) 
            })
        }