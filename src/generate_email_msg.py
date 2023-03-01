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
        for s in "11931 2023-02-24", "11992 2023-02-24":
            result.add(s)
        return result
    
def load_all_data():
    response = requests.get(url) ## TODO add auth
    return json.loads(response.text)

def find_apartments():
    d = load_all_data()
    already_sent = get_already_sent()
    apartments = []
    for p in d['product']:
        if p['type'] != "Lägenhet": continue
        if not (p['area'] in ['Dammhagen', 'Marathon', 'Magasinet']): continue
        seen_string = p['productId'] + " " + p['reserveFromDate']
        if seen_string in already_sent: continue
        # TODO write seen apartments to dynamodb
        apartments.append(p)
    return apartments

def generate_email_html():
    apartments = find_apartments()
    if not apartments:
        return False
    def generate_one_apartment_html(apartment):
        return f"""
<div>
    <h2>{apartment.get('area', '')} - {apartment.get('shortDescription', '')}</h2>
    <ul style="font-size: 20px">
        <li>{apartment.get('description', '')}</li>
        <li>{apartment.get('sqrMtrs', '')} m^2</li>
        <li>Våning {apartment.get('floor', '')}</li>
        <li>Inflyttningsdatum: {apartment.get('moveInDate', '')}</li>
        <li>Hyra: {apartment.get('rent', '')}</li>
        <li>Köplats: {apartment.get('queueNumber', '')}</li>
        <li>Sista ansökningsdatum: {apartment.get('reserveUntilDate', '')}</li>
    </ul>
</div>
    """
    template = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AFB email</title>
</head>
<body>
{"".join([generate_one_apartment_html(apartment) for apartment in apartments])}
</body>
</html>
"""
    return template

print(generate_email_html())
