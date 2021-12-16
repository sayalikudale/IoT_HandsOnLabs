import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'iot-data-aws-bucket'
    
    file_name = 'raw_data.json'
    
    uploadByteStream = bytes(json.dumps(event).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=file_name, Body=uploadByteStream)
    print('save raw data')
    
    # check the age of panda
    if int(event['age']) < 8:
        adultOrBaby = "Baby"
    else :
        adultOrBaby = "adult"
    
    # decide category of panda
    if int(event['weight']) < 150:
        category = "Normal"
    else:
        category = "Giant"
    
    message_text = "Message is for {0} , with color {1}, and age {2}. This panda is {3} panda according to its age.Due to weight of the panda it is categorised as {4} panda ".format(
            str(event['panda']),
            str(event['color']),
            str(event['age']),
            adultOrBaby,
            category
        )
    
    print(message_text)
    
    file_name1 = 'processed_data.json'
    
    uploadByteStream1 = bytes(json.dumps(message_text).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=file_name1, Body=uploadByteStream1)
    
    print('save processed data')