# Monitra
## AWS Infra

- API Gateway to be configured
- Lambda function retrieves data from HTTP calls by the client, and pushes them for storage and analytics on CloudWatch

The following policy must exist, via an IAM role, for the lambda script to be able to push data into CloudWatch

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-south-1:128187395606:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:ap-south-1:128187395606:log-group:/aws/lambda/Monitra:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*"
        }
    ]
}