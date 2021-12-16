import json
import boto3
import time

s3 = boto3.client('s3')
client = boto3.client('iot-data', region_name='us-west-2')


def lambda_handler(event, context):
    print("lambda triggered")
    bucket = 'iot-data-aws-bucket'
    core_device_name = 'Panda_Greengrass'

    print(str(event['message']))
    message_text = "Client message is :  {0} received by core device : {1}, at  {2}.This message is forwarded upstream.".format(
            str(event['message']),
            core_device_name,
            time.ctime()
            )
    
    print(message_text)
    
    # Publish the formatted message
    response = client.publish(
            topic = 'PandaCoreData',
            qos = 0,
            payload=json.dumps(message_text)
        )
        
    file_name = 'coreData.json'
    
    uploadByteStream = bytes(json.dumps(message_text).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=file_name, Body=uploadByteStream)
    return response