import boto3

class S3Helper:
    def __init__(self):
        self.client = boto3.client('s3')
    
    def download_text(self, bucket, key):
        """Download text file from S3"""
        response = self.client.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    
    def download_binary(self, bucket, key):
        """Download binary file from S3"""
        response = self.client.get_object(Bucket=bucket, Key=key)
        return response['Body'].read()
    
    def upload_text(self, bucket, key, content):
        """Upload text content to S3"""
        self.client.put_object(
            Bucket=bucket,
            Key=key,
            Body=content,
            ContentType='text/plain'
        )
    
    def upload_binary(self, bucket, key, data, content_type):
        """Upload binary content to S3"""
        self.client.put_object(
            Bucket=bucket,
            Key=key,
            Body=data,
            ContentType=content_type
        )