import boto3

# Get the service resource
client = boto3.client('ec2')

filters=[
        {
            'Name': 'group-id',
            'Values': ['sg-09d0c55a2a08dcadb']
        }
]

response = client.describe_security_group_rules(
    Filters = filters
)

print(response)
