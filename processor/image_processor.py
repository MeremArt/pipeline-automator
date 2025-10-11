from PIL import Image
from io import BytesIO
from config import IMAGE_SIZES, IMAGE_QUALITY
from utils.s3_helper import S3Helper
from utils.sns_helper import SNSHelper

class ImageProcessor:
    def __init__(self):
        self.s3 = S3Helper()
        self.sns = SNSHelper()
    
    def process(self, bucket_name, file_key):
        """Process and resize images"""
        # Download image
        image_data = self.s3.download_binary(bucket_name, file_key)
        original_image = Image.open(BytesIO(image_data))
        
        # Get metadata
        original_format = original_image.format
        original_size = original_image.size
        
        # Resize to multiple sizes
        output_files = []
        for size_name, dimensions in IMAGE_SIZES.items():
            resized_image = self._resize_image(original_image, dimensions)
            output_key = self._generate_output_key(file_key, size_name)
            
            # Upload to S3
            self._upload_image(bucket_name, output_key, resized_image, original_format)
            
            output_files.append({
                'size': size_name,
                'dimensions': resized_image.size,
                'location': output_key
            })
        
        # Send notification
        self.sns.send_image_notification(file_key, original_size, original_format, 
                                        output_files, bucket_name)
        
        return {
            'statusCode': 200,
            'body': {'message': 'Image processed', 'outputs': output_files}
        }
    
    def _resize_image(self, image, dimensions):
        """Resize image maintaining aspect ratio"""
        resized = image.copy()
        resized.thumbnail(dimensions, Image.Resampling.LANCZOS)
        return resized
    
    def _generate_output_key(self, file_key, size_name):
        """Generate S3 key for output file"""
        file_name = file_key.split('/')[-1]
        name_without_ext = '.'.join(file_name.split('.')[:-1])
        extension = file_name.split('.')[-1]
        return f"processed/{name_without_ext}_{size_name}.{extension}"
    
    def _upload_image(self, bucket_name, key, image, format):
        """Upload processed image to S3"""
        buffer = BytesIO()
        
        if format == 'JPEG':
            image = image.convert('RGB')
        
        image.save(buffer, format=format or 'JPEG', quality=IMAGE_QUALITY)
        buffer.seek(0)
        
        self.s3.upload_binary(bucket_name, key, buffer.getvalue(), f'image/{key.split(".")[-1]}')