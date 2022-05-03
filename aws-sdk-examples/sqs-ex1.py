import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Local variables
common_tags_dictionary = dict()
sqs_attributes_dictionary = dict()

config_file_name = "sqs-ex1.config"
config_file_lines = []

# Inputs
sqs_name=input("Enter a name for the SQS queue: ")

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


# Read all lines from the config file.
with open(config_file_name,'r') as f:
    config_file_lines = f.readlines()

# Split all lines read from the config file in key:value and populate the attributes dictionary. Make sure you strip the new line character.
count = 0
for line in config_file_lines:
    count += 1
    line=line.strip('\n')
    key_value=line.split(":")
    sqs_attributes_dictionary[key_value[0]]=key_value[1]

print(sqs_attributes_dictionary)

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName=sqs_name, Attributes=sqs_attributes_dictionary, tags=common_tags_dictionary)

# Outputs
print("SQS URL: " +queue.url)
print("SQS Delay Seconds: " +queue.attributes.get('DelaySeconds'))
