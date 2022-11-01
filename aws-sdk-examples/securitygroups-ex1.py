'''
----------------------------------------------------------------------------------------------------------
This example shows how to create a security group and add some ingress rules.
The default egress rule is created automatically allowing all traffic/all protocols/all ports to 0.0.0.0/0.
-----------------------------------------------------------------------------------------------------------
'''
import boto3

# Get the service resource
client = boto3.client('ec2')

# Initalize parameters.
sg_name = 'Test SG'
sg_description = 'Test Security Group'
vpc_id = 'vpc-0291e1f27c8725ac4'

# Create security group. 
# The default egress rule is also created allowing all traffic/all protocols/all ports to 0.0.0.0/0.
# response = client.create_security_group(GroupName = sg_name, Description = sg_description, VpcId = vpc_id)

# cidr_ip = '1.2.3.4/32'
group_id =  'sg-09d0c55a2a08dcadb'
from_port = 80
to_port = 80
ip_protocol = 'tcp'

# Create one ingress security group rule. 
'''
response = client.authorize_security_group_ingress(
    GroupId = group_id,
    FromPort = from_port,
    ToPort = to_port,
    IpProtocol = ip_protocol,
    CidrIp = cidr_ip)
'''

# Create multiple ingress security  group rules.
ip_permissions = [
    {
        'FromPort': 80,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'HTTP from anywhere'}],
        'ToPort': 80
    },
    {
        'FromPort': 443,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'HTTPS from anywhere'}],
        'ToPort': 443
    },
    {
        'FromPort': 22,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '1.2.3.4/32', 'Description': 'SSH from restricted IP'}],
        'ToPort': 22
    }
]

response = client.authorize_security_group_ingress(
    GroupId = group_id,
    IpPermissions = ip_permissions
)

print(response)
