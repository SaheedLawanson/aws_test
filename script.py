import json, boto3, sys
from flask import Flask, request
app = Flask(__name__)

dynamodb_client = boto3.client('dynamodb')
cognito_client = boto3.client('cognito-idp')
sys.path.append('functions/')

def authorizer(request):
    bearer_auth = request.headers.get('Authorization')
    token = bearer_auth.split(" ")[1]
    event = {"authorizationToken": token}

    from authorizer import lambda_handler
    print(lambda_handler(event, None))
    return {"email": lambda_handler(event, None)['user']['email']}

@app.route('/')
def hello_world():
    return json.dumps({"message": 'Hello, World!'})

@app.route('/sign_up', methods = ['POST'])
def sign_up():
    from signup import lambda_handler
    event = {"body": request.get_data()}

    response = lambda_handler(event, None)
    return response

@app.route('/confirm_sign_up', methods = ['POST'])
def confirm_sign_up():
    from confirm_user import lambda_handler
    event = {"body": request.get_data()}

    response = lambda_handler(event, None)
    return response


@app.route('/login', methods = ['POST'])
def login():
    from login import lambda_handler

    event = {"body": request.data}
    response = lambda_handler(event, None)
    return response

@app.route('/user', methods = ['GET'])
def get_user():
    from get_user import lambda_handler

    event = {"context": authorizer(request)}
    response = lambda_handler(event, None)
    return response


if __name__ == '__main__':
    app.run(debug=True)