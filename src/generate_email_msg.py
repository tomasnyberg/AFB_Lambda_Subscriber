import boto3
import json
import requests

url = "https://api.afbostader.se:442/redimo/rest/vacantproducts?lang=sv_SE&type=1"

def get_already_sent(production=False):
    if production:
        dynamodb = boto3.client('dynamodb')
        table_name = 'AF_bot_table'
        results = dynamodb.scan(TableName=table_name, ProjectionExpression='apartments')
        result = set()
        for res in results['Items']:
            result.add(res['apartments']['S'])
        return result
    else:
        result = set()
        for s in "11931 2023-02-24", "11992 2023-02-24", "3462 2023-03-01":
            result.add(s)
        return result
    
def load_all_data():
    response = requests.get(url) ## TODO add auth
    return json.loads(response.text)

print(load_all_data())
