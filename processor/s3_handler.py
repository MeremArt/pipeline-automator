import boto3

s3 = boto3.client('s3')

def download_file_from_s3(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].read().decode('utf-8')

def upload_file_to_s3(bucket, key, content, content_type='text/plain'):
    s3.put_object(Bucket=bucket, Key=key, Body=content, ContentType=content_type)
