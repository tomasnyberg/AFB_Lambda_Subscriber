import json
import boto3
import requests
from generate_email_msg import generate_email_html

def lambda_handler(event, context):
    msg = generate_email_html()
    if not msg:
        return "No new apartments"
    client = boto3.client("ses")
    subject = "test subject from lambda"
    body = msg
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "tomas.nyberg7335@gmail.com",
               Destination = {"ToAddresses": ["tomas.nyberg7335@gmail.com"]}, Message = message)
    return "Found new apartments, sending email"
