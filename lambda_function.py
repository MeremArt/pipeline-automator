import json
from processors.csv_processor import CSVProcessor
from processors.image_processor import ImageProcessor

def lambda_handler(event, context):
    """Main entry point for Lambda function"""
    try:
        # Extract event details
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        # Validate file location
        if not file_key.startswith('uploads/'):
            return {'statusCode': 200, 'body': 'File skipped'}
        
        # Route to appropriate processor
        file_extension = file_key.lower().split('.')[-1]
        
        if file_extension == 'csv':
            processor = CSVProcessor()
            return processor.process(bucket_name, file_key)
        elif file_extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']:
            processor = ImageProcessor()
            return processor.process(bucket_name, file_key)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'Unsupported file type: {file_extension}'})
            }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}