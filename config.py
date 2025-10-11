SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')
IMAGE_SIZES = {
    'thumbnail': (150, 150),
    'medium': (500, 500),
    'large': (1200, 1200)
}

MAX_CSV_ROWS = 10000
IMAGE_QUALITY = 90
REPORT_PREVIEW_ROWS = 5