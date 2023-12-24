import json
def lambda_handler(event, context):
    print(event)
    #TODO: Get key and bucketname
    record = event['Records'][0]
    key = record['s3']['object']['key']
    bucketname = record['s3']['bucket']['name']
    print(f"File {key} is uploaded to s3 bucket {bucketname}")