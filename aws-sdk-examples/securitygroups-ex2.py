'''
This example shows how to detect ingress rules that open access to port 3389 (RDP) or 22 (SSH) from anywhere on a security group.
'''
import boto3

sg_id = 'sg-09d0c55a2a08dcadb'

# Get the service resource
client = boto3.client('ec2')

filters=[
        {
            'Name': 'group-id',
            'Values': [sg_id]
        }
]

response = client.describe_security_group_rules(
    Filters = filters
)

offending_sg_rules = []

sg_rules = response['SecurityGroupRules']

for rule in sg_rules:
    # Only flag ingress rules with CidrIpv4 equal to anywhere.
    if (rule['IsEgress'] == False) and (rule['CidrIpv4'] == '0.0.0.0/0'):
        
        # Flag the rules that allow RDP or SSH access from anywhere.
        if (rule['FromPort'] == 3389) or (rule['FromPort'] == 22):
            print(f"Ingress rule {rule['SecurityGroupRuleId']} opens port {rule['FromPort']} from anywhere!" )
            offending_sg_rules.append(rule)

if len(offending_sg_rules) == 0:
    print('No offending rules found.')        

else:
    print(f"Offending rules: {offending_sg_rules}")


