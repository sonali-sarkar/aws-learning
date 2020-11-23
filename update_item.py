import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    response = table.update_item(
       Key={
            'year': 2020,
            'title': 'Panga'
        },
        UpdateExpression= 'SET INFO =:val1',
        ExpressionAttributeValues= {':val1': {
                'plot': 'thriller',
                'rating': 4}}
    )
