import json, boto3, os

dynamodb_client = boto3.client('dynamodb')

table_name = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    try:
        user = event['context']

        response = dynamodb_client.get_item(
            TableName = table_name,
            Key = {
                "email": {"S": user['email']}
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps(response["Item"])
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
        "context": {
            "email": 'saheedlawanson47@gmail.com'
        }
    }
    result = lambda_handler(event, None)
    pprint(result)