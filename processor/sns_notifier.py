import boto3

sns = boto3.client('sns')

def send_sns_notification(topic_arn, subject, message):
    sns.publish(TopicArn=topic_arn, Subject=subject, Message=message)
