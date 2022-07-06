import json, boto3, os

dynamodb_client = boto3.client('dynamodb')
cognito_client = boto3.client('cognito-idp')

table_name = os.environ['TABLE_NAME']
cognito_client_id = os.environ['CLIENT_ID']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        user_email = body['user_email']
        code = body['confirmation_code']

        response = cognito_client.confirm_sign_up(
            ClientId = cognito_client_id,
            Username = user_email,
            ConfirmationCode = code
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Successfully confirmed signup",
                "data": None
            })
        }

    except SystemError:
        return {
            'statusCode': 400,
            "body": json.dumps({
                "message": "An error occurred",
                "data": None
            })
        }

if __name__ == "__main__":
    from pprint import pprint
    event = {
        "body": {
            "user_email": 'saheedlawanson47@gmail.com',
            "confirmation_code": "400074"
        }
    }
    result = lambda_handler(event, None)
    pprint(result)