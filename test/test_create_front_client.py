import os
import boto3

LAMBDA = boto3.client(
    "lambda",
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', None),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', None),
    region_name=os.environ.get('AWS_DEFAULT_REGION', "eu-west-1")
)

LAMBDA.invoke(
    FunctionName='hello',
    InvocationType='RequestResponse'
)
