import boto3
from datetime import datetime
from config import SNS_TOPIC_ARN

class SNSHelper:
    def __init__(self):
        self.client = boto3.client('sns')
        self.topic_arn = SNS_TOPIC_ARN
    
    def send_csv_notification(self, file_key, total_rows, columns, bucket, output_key):
        """Send CSV processing notification"""
        message = f"""
📊 CSV Processing Complete!

Original File: {file_key}
Total Rows: {total_rows}
Columns: {', '.join(columns)}
Report: s3://{bucket}/{output_key}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        self.client.publish(
            TopicArn=self.topic_arn,
            Subject='✅ CSV Processing Complete',
            Message=message
        )
    
    def send_image_notification(self, file_key, original_size, format, output_files, bucket):
        """Send image processing notification"""
        resize_details = '\n'.join([
            f"  - {f['size'].title()}: {f['dimensions'][0]}x{f['dimensions'][1]}px"
            for f in output_files
        ])
        
        message = f"""
🖼️ Image Processing Complete!

Original: {file_key}
Size: {original_size[0]}x{original_size[1]}px
Format: {format}

Resized Versions:
{resize_details}

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        self.client.publish(
            TopicArn=self.topic_arn,
            Subject='✅ Image Processing Complete',
            Message=message
        )
    
    def send_error_notification(self, error_message):
        """Send error notification"""
        self.client.publish(
            TopicArn=self.topic_arn,
            Subject='❌ Processing Failed',
            Message=f"Error occurred:\n{error_message}"
        )