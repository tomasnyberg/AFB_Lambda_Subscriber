import json
import boto3

msg = "" 

import requests

r = requests.get('https://swapi.dev/api/people/1/')
msg += (r.json()['name'])

def lambda_handler(event, context):
    client = boto3.client("ses")
    subject = "test subject from lambda"
    body = msg
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    # response = client.send_email(Source = "tomas.nyberg7335@gmail.com",
    #            Destination = {"ToAddresses": ["tomas.nyberg7335@gmail.com"]}, Message = message)
    print(body)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hej hopp",
        }),
    }
