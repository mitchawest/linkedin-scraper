import boto3
import os

access_id = os.environ['AWS_APP_ID']
access_key = os.environ['AWS_APP_SECRET']


def upload_to_aws_s3(data, bucket, s3_filename):
    s3 = boto3.client('s3', aws_access_key_id=access_id,
                      aws_secret_access_key=access_key)

    try:
        s3.put_object(Body=data, Bucket=bucket, Key=s3_filename)
        print("Upload Successful")
        return True
    except Exception as e:
        print('Exception: ' + e)
