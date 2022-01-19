import json
import boto3

def lambda_handler(event, context):
    
    cloudwatch = boto3.client('cloudwatch')
    
    # Static API Key
    if 'api-key' not in event['headers']:
        return error_out()
    
    if event['headers']['api-key'] != "asdasdas":
        return error_out()
        
    payload_data = json.loads(event['body'])
    
    for payload in payload_data:
        
        response = cloudwatch.put_metric_data(
            MetricData = [
                {
                    'MetricName': payload['metric'],
                    'Dimensions': [
                        {
                            'Name': 'DEVICE',
                            'Value': payload['device']
                        },
                    ],
                    'Unit': 'Count',
                    'Value': float(payload['value'])
                },
            ],
            Namespace = 'Monitra'
        )
        
    return {
        'statusCode': 200,
        'body': str(len(payload_data)) + ' metrics logged'
    }
        
def error_out():
    return {
        'statusCode': 403,
        'body': json.dumps('Access not allowed!')
    }