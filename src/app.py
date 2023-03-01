import json
import boto3
import requests
from generate_email_msg import generate_email_html

# Get the current date in a string
def get_date():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d")

def lambda_handler(event, context):
    msg = generate_email_html()
    if not msg:
        return "No new apartments " + get_date()
    client = boto3.client("ses")
    subject = "Nya lägenheter!!"
    body = msg
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "tomas.nyberg7335@gmail.com",
               Destination = {"ToAddresses": ["tomas.nyberg7335@gmail.com", 'claralonnberg@gmail.com']}, Message = message)
    return "Found new apartments, sending email " + get_date()
