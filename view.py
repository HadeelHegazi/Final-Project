
import boto3
import io
from docx2pdf import convert

s3_client = boto3.client('s3')
sqs_clint = boto3.client('sqs')

def text2pdf(event):
    # Get the bucket name and file key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Download the file from S3
    file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = file_obj['Body'].read()

    # Convert the file to PDF
    pdf_bytes = io.BytesIO()
    convert(io.BytesIO(file_content), pdf_bytes)

    # Upload the PDF to S3
    pdf_key = file_key.split('.')[0] + '.pdf'
    s3_client.upload_fileobj(pdf_bytes, bucket_name, pdf_key)

    print(f'File {file_key} converted to {pdf_key} and uploaded to {bucket_name}')

    return {
        'statusCode': 200,
        'body': 'File converted and uploaded successfully'
    }

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