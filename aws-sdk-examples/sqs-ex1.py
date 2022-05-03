import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Local variables
common_tags_dictionary = dict()

# Inputs
sqs_name=input("Enter a name for the SQS queue: ")

sqs_delay_seconds=input("Enter delay in seconds: ")

user_input=""
while user_input != "exit":
    user_input = input('Tags - Enter key & value separated by ":" ')
    print(f"User input: {user_input}")
    
    # Need this test to avoid running the code below when user_input="exit" which results in 'list index out of range' error!
    if user_input != "exit":
        key_value = user_input.split(":")
        print(f"key_value: {key_value}") 
        
        # Adds key:value pair to the tags dictionary.
        common_tags_dictionary[key_value[0]]=key_value[1]
        print(f"common_tags_dictionary: {common_tags_dictionary}")    


# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName=sqs_name, Attributes={'DelaySeconds': sqs_delay_seconds}, tags=common_tags_dictionary)

# Outputs
print("SQS URL: " +queue.url)
print("SQS Delay Seconds: " +queue.attributes.get('DelaySeconds'))
