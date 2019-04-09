import boto3
from boto3.dynamodb.conditions import Key

tablename = "northwind"
dynamodb = boto3.resource('dynamodb', region_name="us-east-2", endpoint_url='http://localhost:8000')
table = dynamodb.Table(tablename)

# Find all the suppliers in Sao Paulo, Brazil
response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('SUPPLIER') & Key('data').begins_with('Brazil#NULL#Sao Paulo'))
print(response['Items'])
