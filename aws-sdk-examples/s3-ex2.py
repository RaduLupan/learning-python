import boto3
import botocore.session
from botocore.exceptions import ClientError

def is_bucket_public (bucket_name):
    
    s3 = boto3.client('s3')

    public_acl=True
    public_policy = False
    bucket_properties = {'Name':bucket_name, 'Grants':'Some grants'}
    if public_acl or public_policy:
        return True


public_flag=is_bucket_public (bucket_name='test')
print(public_flag)
