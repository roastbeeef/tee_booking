# insertion works!

# from tee_booking.src.vars import (
#     TRANSACTIONS_TABLE_OBJECT
#     )
# import json


# table_data = TRANSACTIONS_TABLE_OBJECT.scan()

# len(table_data['Items'])

# this weekend! 
# 1) nav bar
# https://dev.to/brunooliveira/flask-series-part-9-adding-a-navbar-by-using-template-inheritance-2e5o
# https://arshovon.com/snippets/flask-bootstrap-navbar/
# https://www.techwithtim.net/tutorials/flask/adding-bootstrap/
# 2) jquery table
# https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates
# 3) lambda function to book
# 4) scheduling
# 5) authentication - just really basic for now until hosted



# hosting - fully serverless!
# website on elastic beanstalk
# database on dynamodb
# scheduling on stepfunctions
# booking on lambda


import boto3
from boto3.dynamodb.conditions import Attr
from src.secrets import (
    aws_region,
    access_key,
    secret_access_key
)
TABLE_NAME = "teebooking-transactions"
dynamo_client = boto3.resource(
    service_name = 'dynamodb',
    region_name = aws_region,
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key
    )

table = dynamo_client.Table(TABLE_NAME)

response = table.scan(FilterExpression=Attr('username').eq('testing'))
print(response['Items'])