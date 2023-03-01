import json
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'AF_bot_table'
results = dynamodb.scan(TableName=table_name, ProjectionExpression='apartments')

import requests
def lambda_handler(event, context):
    client = boto3.client("ses")
    subject = "test subject from lambda"
    body = "test body from lambda"
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    # response = client.send_email(Source = "tomas.nyberg7335@gmail.com",
    #            Destination = {"ToAddresses": ["tomas.nyberg7335@gmail.com"]}, Message = message)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hej hopp",
        }),
    }
