import json, boto3, os

dynamodb_client = boto3.client('dynamodb')
cognito_client = boto3.client('cognito-idp')

table_name = os.environ['TABLE_NAME']
cognito_client_id = os.environ['CLIENT_ID']

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        password = body.pop('password')
        attributes = [
            "email", "first_name", "last_name",
            "fullname", "phone_number", "address",
            "dob", "gender", "username"
        ]
        custom_attributes = [
            "image_id", "date_created", "is_recurring",
            "profile_type", "balance", "tenant_id",
            "promo_code", "formatted_date", "account_number",
            "father_name", "status", "city", "rating",
            "state", "country", "delete_flag", "last_logged_in",
            "last_modified", "bvn", "pin", "question_1",
            "question_2", "question_3", "answer_1", "answer_2",
            "answer_3", "docType", "date_joined", "is_superuser",
            "is_staff", "is_active", "countryCode",
            "receive_notification"
        ]

        response = cognito_client.sign_up(
            ClientId = cognito_client_id,
            Username = body["email"],
            Password = password,
            UserAttributes = [
                {
                    'Name': 'email', 'Value': body["email"]
                },
                {
                    'Name': 'given_name', 'Value': body['first_name']
                },
                {
                    'Name': 'family_name', 'Value': body['last_name']
                },
                {
                    'Name': 'name', 'Value': body['fullname']
                },
                {
                    'Name': 'phone_number', 'Value': body['phone_number']
                },
                {
                    'Name': 'address', 'Value': body['address']
                },
                {
                    'Name': 'birthdate', 'Value': body['dob']
                },
                {
                    'Name': 'gender', 'Value': body['gender']
                },
                {
                    'Name': 'preferred_username', 'Value': body['username']
                }
            ] + [
                {
                    'Name': f'custom:{attr}', 'Value': body[attr]
                } for attr in custom_attributes
            ],
            ValidationData = [
                {
                    'Name': 'email', 'Value': body['email']
                }
            ]
        )

        db_response = dynamodb_client.put_item(
            TableName = table_name,
            Item = {
                attribute: {'S': body[attribute]} for attribute in attributes
            } | {
                attribute: {'S': body[attribute]} for attribute in custom_attributes
            },
            ConditionExpression = "attribute_not_exists(#email)",
            ExpressionAttributeNames = {
                "#email": "email"
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Successfully signed in, a confirmation code has been sent to {response['CodeDeliveryDetails']['Destination']}",
                "data": None
            })
        }

    except SystemError:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "An error occurred",
                "data": None
            })
        }

if __name__ == "__main__":
    event = {
        "body": json.dumps({
            "email": "saheedlawanson47@gmail.com",
            "first_name": "saheed",
            "last_name": "lawanson",
            "fullname": "saheed lawanson",
            "username": "seedy",
            "gender": "male",
            "dob": "2000-05-18",
            "phone_number": "+2349084549068",
            "address": "17, Moleye Street",
            "password": "Seedboy13#"
        })
    }

    from pprint import pprint
    result = lambda_handler(event, None)
    # pprint(json.loads(result['body']))
    pprint(result)