'''
This code creates an SQS client using boto3, creates a new queue called test and associates it with a dead-letter queue called test-dlq,
and defines two functions: send_message and receive_message.
The send_message function takes a message body as input and sends that message to the test queue.
The receive_message function retrieves a message from the test queue, deletes the message from the queue, and returns the message. If there are no messages in the queue, it returns None.
'''
import boto3, json

# Create an SQS client
sqs = boto3.client('sqs')

# Create the queue
queue_name = 'test'
dlq_name = 'test-dlq'
response = sqs.create_queue(
    QueueName=queue_name,
    Attributes={
        'RedrivePolicy': json.dumps({
            'deadLetterTargetArn': f'arn:aws:sqs:{sqs.meta.region_name}:{sqs.meta.account_id}:{dlq_name}',
            'maxReceiveCount': '5'
        })
    }
)
queue_url = response['QueueUrl']

# Send a message to the queue
def send_message(message_body):
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )

# Receive a message from the queue
def receive_message():
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=0
    )
    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete the message from the queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        return message
    return None
