import boto3
from boto3.dynamodb.conditions import Key

tablename = "northwind"
dynamodb = boto3.resource('dynamodb', region_name="us-east-2", endpoint_url='http://localhost:8000')
table = dynamodb.Table(tablename)

# Find all the orders containting product 70
response = table.query(IndexName='gsi_1', KeyConditionExpression=Key('sk').eq('products#70'))
print(response['Items'])

