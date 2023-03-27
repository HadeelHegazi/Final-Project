
import os
import io
import boto3
from PIL import Image

s3_client = boto3.client('s3')
sqs_clint = boto3.client('sqs')

def text2pdf(event):
    # Set the bucket name and key of the image to be compressed
    bucket_name = "your-bucket-name"
    source_key = "path/to/image.jpg"

    # Set the name of the compressed file
    compressed_key = "path/to/compressed_image.jpg"

    # Initialize the S3 client
    s3 = boto3.client("s3")

    # Download the image file from S3
    response = s3.get_object(Bucket=bucket_name, Key=source_key)
    image_content = response["Body"].read()

    # Load the image file into Pillow
    image = Image.open(io.BytesIO(image_content))

    # Compress the image
    image = image.resize((image.width // 2, image.height // 2))

    # Save the compressed image to a buffer
    compressed_image_buffer = io.BytesIO()
    image.save(compressed_image_buffer, format="JPEG")

    # Upload the compressed image file to S3
    s3.upload_fileobj(
        compressed_image_buffer,
        bucket_name,
        compressed_key,
        ExtraArgs={"ContentType": "image/jpeg", "ACL": "public-read"},
    )

    # Delete the original image file from S3
    s3.delete_object(Bucket=bucket_name, Key=source_key)

# Get the URL of the SQS queue
queue_url = 'https://sqs.us-east-1.amazonaws.com/437652894623/eventsq'

# Receive a message from the queue
response = sqs_clint.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=20
)

# Check if a message was received
if 'Messages' in response:
    # Get the first message from the response
    message = response['Messages'][0]

    text2pdf(message['Body'])

    # Print the message body
    print(message['Body'])

    # Delete the message from the queue
    receipt_handle = message['ReceiptHandle']
    sqs_clint.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
else:
    print('No messages in queue')
