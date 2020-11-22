import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    response = table.put_item(
       Item={
            'year': 2020,
            'title': 'Panga'
        }
    )
   
