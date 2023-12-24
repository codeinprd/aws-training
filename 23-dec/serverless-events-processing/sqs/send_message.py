import boto3

sqs = boto3.client("sqs")

queue_url = "https://sqs.eu-central-1.amazonaws.com/094718664989/demo-23-12"

message_object = str({"Id": "1", "Name": "Aviral Vishnois"})
response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_object)
