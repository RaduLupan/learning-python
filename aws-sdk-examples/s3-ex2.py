import boto3
#---------------------------------------------------------------------------------------------------------
# This exemple expands on s3-ex1.py and uses a Python function to evaluate if a given S3 bucket is public.
# --------------------------------------------------------------------------------------------------------

import botocore.session
from botocore.exceptions import ClientError

bucket_properties = dict()

def evaluate_s3_public_access (bucket_name):
    
    s3 = boto3.client('s3')

    public_acl=True
    public_policy = False
    bucket_properties = {'Name':bucket_name, 'Grants':'Some grants'}
    
    return bucket_properties

bucket_properties=evaluate_s3_public_access (bucket_name='test')
print(bucket_properties)
