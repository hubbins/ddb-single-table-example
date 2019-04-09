import boto3
from boto3.dynamodb.conditions import Key

tablename = "northwind"
dynamodb = boto3.resource('dynamodb', region_name="us-east-2", endpoint_url='http://localhost:8000')
table = dynamodb.Table(tablename)

# h. List all products included in an order
response = table.query(KeyConditionExpression=Key('pk').eq('10260') & Key('sk').begins_with('products'))
print(response['Items'])

