# Serverless AWS lambda example

![](https://img.shields.io/badge/AWS-Serverless-red)
![](https://img.shields.io/badge/AWS-lambda-blue)
![](https://img.shields.io/badge/python-3.9-green)
![](https://img.shields.io/badge/node-16-white)

## Description :

This project shows how to deploy function to AWS lambda with Serverless framework

## How To

For the followings steps you need to configure AWS CLI: [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

- Create bucket on AWS S3: [documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
- Define secret variables
```bash
# You choose the value for API_KEY_SERVERLESS
aws ssm put-parameter --name API_KEY_SERVERLESS --value ${API_KEY_SERVERLESS} --type SecureString
# Need to be the name of your newly created bucket
aws ssm put-parameter --name S3_BUCKET --value ${S3_BUCKET} --type SecureString
```
- Deploy your function
```bash
npm install -g serverless
sls plugin install -n serverless-python-requirements
sls create_domain
sls deploy --verbose --conceal
```

# Files Structure

```
Serverless-AWS-lambda-example
 │
 ├── src
 │   └── hello
 │        └── hello.py
 │
 ├── test
 │    └── hello.py
 │
 ├── requirements.txt
 |
 └── serverless.yml
```
