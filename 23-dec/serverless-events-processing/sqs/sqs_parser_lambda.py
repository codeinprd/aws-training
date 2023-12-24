def lambda_handler(event, context):
    for message in event["Records"]:
        message_body = message["body"]
        reciepHandler = message["receiptHandle"]


