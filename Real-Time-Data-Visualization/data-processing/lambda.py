 python
import json
import boto3

def handler(event, context):
    records = event['Records']
    for record in records:
        payload = json.loads(record['Sns']['Message'])
        # process payload data using AWS services and store results in S3
        # ...

    return {'statusCode': 200, 'body': 'Data processed successfully!'}
