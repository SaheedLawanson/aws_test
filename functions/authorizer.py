import json, boto3, os

dynamodb_client = boto3.client('dynamodb')
cognito_client = boto3.client('cognito-idp')

table_name = os.environ['TABLE_NAME']
cognito_client_id = os.environ['CLIENT_ID']

def lambda_handler(event, context):
    try:
        token = event['authorizationToken']

        response = cognito_client.get_user(
            AccessToken = token
        )

        user_attributes = response['UserAttributes']
        user = {attribute['Name']: attribute['Value'] for attribute in user_attributes}

        return {"status": True, "user": user}

    except Exception:
        return {"status": False, "user": None}


if __name__ == "__main__":
    from pprint import pprint
    event = {
        "authorizationToken": ''
    }
    result = lambda_handler(event, None)
    pprint(result)