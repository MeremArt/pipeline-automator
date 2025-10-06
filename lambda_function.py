import os
import json
from datetime import datetime

from processor.s3_handler import download_file_from_s3, upload_file_to_s3
from processor.csv_processor import parse_csv, get_column_names
from processor.report_generator import generate_report
from processor.sns_notifier import send_sns_notification

def lambda_handler(event, context):
    try:
        sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
        if not sns_topic_arn:
            raise Exception("SNS_TOPIC_ARN environment variable not set")
        
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']

        print(f"Processing file: {file_key} from bucket: {bucket_name}")

        if not file_key.startswith('uploads/') or not file_key.endswith('.csv'):
            print(f"Skipping file: {file_key}")
            return {'statusCode': 200, 'body': json.dumps('Skipped')}
        
        file_content = download_file_from_s3(bucket_name, file_key)
        rows = parse_csv(file_content)
        total_rows = len(rows)
        columns = get_column_names(rows)
        
        report = generate_report(rows, file_key, total_rows, columns)
        output_key = file_key.replace('uploads/', 'processed/').replace('.csv', '_report.txt')
        upload_file_to_s3(bucket_name, output_key, report)
        
        message = f"""
Data Pipeline Processing Complete!
Original File: {file_key}
Total Rows Processed: {total_rows}
Columns: {', '.join(columns)}
Report Location: s3://{bucket_name}/{output_key}
Processing Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        send_sns_notification(sns_topic_arn, '✅ S3 Data Pipeline - Processing Complete', message)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File processed successfully',
                'input_file': file_key,
                'output_file': output_key,
                'rows_processed': total_rows
            })
        }

    except Exception as e:
        error_message = f"Error processing file: {str(e)}"
        print(error_message)
        try:
            send_sns_notification(sns_topic_arn, '❌ S3 Data Pipeline - Processing Failed', error_message)
        except:
            pass
        return {'statusCode': 500, 'body': json.dumps({'error': error_message})}
