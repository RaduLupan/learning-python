import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Inputs
print("Enter a name for the SQS queue")
sqs_name=input()

print("Enter delay in seconds")
sqs_delay_seconds=input()


# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName=sqs_name, Attributes={'DelaySeconds': sqs_delay_seconds})

# Outputs
print("SQS URL: " +queue.url)
print("SQS Delay Seconds: " +queue.attributes.get('DelaySeconds'))
