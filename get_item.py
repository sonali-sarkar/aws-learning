import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    response = table.get_item(
       Key={
            'year': 2020,
            'title': 'Panga'
        }
    )
    return response['Item']
