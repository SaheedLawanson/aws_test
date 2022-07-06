import json, boto3, os

dynamodb_client = boto3.client('dynamodb')
cognito_client = boto3.client('cognito-idp')

table_name = os.environ['TABLE_NAME']
cognito_client_id = os.environ['CLIENT_ID']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        user_email = body['user_email']
        password = body.pop('password')

        response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user_email,
                'PASSWORD': password
            },
            ClientId = cognito_client_id
        )

        return {
            "statusCode": 200,
            "body": json.dumps(response['AuthenticationResult'])
        }

    except cognito_client.exceptions.UserNotConfirmedException:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "message": "This account has not been activated",
                "data": None
            })
        }

    except cognito_client.exceptions.NotAuthorizedException:
        return {
            "statusCode": 402,
            "body": json.dumps({
                "message": "Incorrect username or password",
                "data": None
            })
        }

    except Exception:
        return {
            "statusCode": 400,
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
            "password": "Seedboy13#"
        }
    }
    result = lambda_handler(event, None)
    pprint(result)