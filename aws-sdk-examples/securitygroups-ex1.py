import boto3

# Get the service resource
client = boto3.client('ec2')

# Initalize parameters.
sg_name = 'Test SG'
sg_description = 'Test Security Group'
vpc_id = 'vpc-0291e1f27c8725ac4'

# Create security group.
response = client.create_security_group(GroupName = sg_name, Description = sg_description, VpcId = vpc_id)

print(response)
