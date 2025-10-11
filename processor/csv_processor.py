import csv
from io import StringIO
from datetime import datetime
from utils.s3_helper import S3Helper
from utils.sns_helper import SNSHelper
from utils.report_generator import ReportGenerator

class CSVProcessor:
    def __init__(self):
        self.s3 = S3Helper()
        self.sns = SNSHelper()
        self.report_gen = ReportGenerator()
    
    def process(self, bucket_name, file_key):
        """Process CSV file and generate report"""
        # Download from S3
        file_content = self.s3.download_text(bucket_name, file_key)
        
        # Parse CSV
        csv_reader = csv.DictReader(StringIO(file_content))
        rows = list(csv_reader)
        
        # Generate statistics
        total_rows = len(rows)
        columns = list(rows[0].keys()) if rows else []
        
        # Create report
        report = self.report_gen.generate_csv_report(rows, file_key, total_rows, columns)
        
        # Save to S3
        output_key = file_key.replace('uploads/', 'processed/').replace('.csv', '_report.txt')
        self.s3.upload_text(bucket_name, output_key, report)
        
        # Send notification
        self.sns.send_csv_notification(file_key, total_rows, columns, bucket_name, output_key)
        
        return {
            'statusCode': 200,
            'body': {'message': 'CSV processed', 'rows': total_rows}
        }