# Serverless AWS lambda example

![](https://img.shields.io/badge/AWS-Serverless-red)
![](https://img.shields.io/badge/AWS-lambda-blue)
![](https://img.shields.io/badge/python-3.9-green)
![](https://img.shields.io/badge/node-16-white)

## Description :

This project shows how to deploy function to AWS lambda from Serverless framework on custom domain

If you don't have any domain name and associated certificate you can
- Skip the first two initals put-parameter commands
- Skip serverless-domain-manager npm installation
- Remove it from plugins in serverless.yml
- Remove *customDomain* section under *custom* raw in serverless.yml

## How To

For the followings steps you need to configure AWS CLI: [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

- Create bucket on AWS S3: [documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
- Define secret variables
```bash
# The domain name on wich your lambda will be triggered
aws ssm put-parameter --name DOMAIN_NAME --value ${DOMAIN_NAME} --type SecureString
# The certificate associated with your domain name (can be the same value)
aws ssm put-parameter --name CERTIFICATE_NAME --value ${CERTIFICATE_NAME} --type SecureString

# You choose the value for API_KEY_SERVERLESS
aws ssm put-parameter --name API_KEY_SERVERLESS --value ${API_KEY_SERVERLESS} --type SecureString
# Need to be the name of your newly created bucket
aws ssm put-parameter --name S3_BUCKET --value ${S3_BUCKET} --type SecureString
```
- Deploy your function
```bash
npm install -g serverless
sls plugin install -n serverless-python-requirements
sls plugin install -n serverless-domain-manager
sls create_domain
sls deploy --verbose --conceal
```

# Files Structure

```
Serverless-AWS-transactional-mailer
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
