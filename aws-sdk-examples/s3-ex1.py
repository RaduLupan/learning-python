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

#try:
 #   access = s3.get_public_access_block(Bucket=bucket_name)
 #   print (access)
#except botocore.exceptions.ClientError as e:
#    if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
#        print('\t no Public Access')
#    else:
#        print("unexpected error: %s" % (e.response))

access = s3.get_public_access_block(Bucket=bucket_name)

bucket_properties['BlockPublicAcls']=access['PublicAccessBlockConfiguration']['BlockPublicAcls']
bucket_properties['IgnorePublicAcls'] = access['PublicAccessBlockConfiguration']['IgnorePublicAcls']
bucket_properties['BlockPublicPolicy'] = access['PublicAccessBlockConfiguration']['BlockPublicPolicy']
bucket_properties['RestrictPublicBuckets'] = access['PublicAccessBlockConfiguration']['RestrictPublicBuckets']

print(f"Bucket {bucket_name} has the following properties: {bucket_properties}")
# print (access)
#print(access['PublicAccessBlockConfiguration'])

#policy_status = s3.get_bucket_policy_status(Bucket=bucket_name)
#print(policy_status)

# bucket_acl = s3.get_bucket_acl(Bucket=bucket_name)
# print(bucket_acl)
