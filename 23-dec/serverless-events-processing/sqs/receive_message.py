import boto3
import json
import ast

sqs = boto3.client("sqs")
queue_url = "https://sqs.eu-central-1.amazonaws.com/094718664989/demo-23-12"
# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=["SentTimestamp"],
    MaxNumberOfMessages=1,
    MessageAttributeNames=["All"],
    VisibilityTimeout=0,
    WaitTimeSeconds=0,
)
print(response)

message = response["Messages"][0]
print(message)
body = message["Body"]
body_dict = ast.literal_eval(body)
print(type(body_dict))
