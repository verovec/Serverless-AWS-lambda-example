import os
import boto3


LAMBDA = boto3.client("lambda")

LAMBDA.invoke(
    FunctionName='hello',
    InvocationType='RequestResponse'
)
