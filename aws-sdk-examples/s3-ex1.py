#-------------------------------------------------------------------------------------------
# This exemple lists all the S3 buckets that have public access turned ON in an AWS account.
# #-----------------------------------------------------------------------------------------

# References:
#------------

# 1: https://www.slsmk.com/programmatically-set-public-block-on-aws-s3-buckets/
# 2: https://stackoverflow.com/questions/59002558/boto-find-if-bucket-is-public-or-private

import boto3
import botocore.session
from botocore.exceptions import ClientError

# Get the service resource
# s3 = boto3.resource('s3')

# Print out bucket names
#for bucket in s3.buckets.all():
#    print(bucket.name)

#buckets = list(s3.buckets.all())
# print(buckets)

bucket_name='letsencrypt-certbot-lambda-dev-uwiwzpe7prtu'
s3 = boto3.client('s3')


bucket_properties=dict()

try:
    access = s3.get_public_access_block(Bucket=bucket_name)
    
    # Loop through the PublicAccessBlockConfiguration dictionary and load all keys in bucket_properties.
    #for key in access['PublicAccessBlockConfiguration']:
    #    bucket_properties[key]=access['PublicAccessBlockConfiguration'][key]

    bucket_properties = access['PublicAccessBlockConfiguration']
    
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
        print(f"Bucket {bucket_name} has never been configured for Public Access Block and all 4 swithces are False by default.")
        bucket_properties['BlockPublicAcls']=False
        bucket_properties['IgnorePublicAcls']=False
        bucket_properties['BlockPublicPolicy']=False
        bucket_properties['RestrictPublicBuckets']=False
    else:
        print("Unexpected error: %s" % (e.response))


print(f"Bucket {bucket_name} has the following properties: {bucket_properties}")

#policy_status = s3.get_bucket_policy_status(Bucket=bucket_name)
#print(policy_status)

# bucket_acl = s3.get_bucket_acl(Bucket=bucket_name)
# print(bucket_acl)
