import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Inputs
sqs_name=input("Enter a name for the SQS queue: ")

sqs_delay_seconds=input("Enter delay in seconds: ")


# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName=sqs_name, Attributes={'DelaySeconds': sqs_delay_seconds}, tags={'environment': 'dev'})

# Outputs
print("SQS URL: " +queue.url)
print("SQS Delay Seconds: " +queue.attributes.get('DelaySeconds'))
