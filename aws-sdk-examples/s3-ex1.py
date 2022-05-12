#------------------------------------------------------------------------------------------
# This exemple evaluates if a given S3 bucket is public due to public ACL or bucket policy.
# -----------------------------------------------------------------------------------------

# References:
#------------

# 1: https://www.slsmk.com/programmatically-set-public-block-on-aws-s3-buckets/
# 2: https://stackoverflow.com/questions/59002558/boto-find-if-bucket-is-public-or-private
# 3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html

import boto3
import botocore.session
from botocore.exceptions import ClientError

# Local variables.
bucket_properties=dict()
public_acl=False
public_policy=False

bucket_name = input ("Enter S3 bucket name:")
s3 = boto3.client('s3')

# Get public access block.
try:
    public_access_block = s3.get_public_access_block(Bucket=bucket_name)
    
    # Simply assign the PublicAccessBlockConfiguration to bucket_properties dict.
    bucket_properties = public_access_block['PublicAccessBlockConfiguration']

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
        print(f"Bucket {bucket_name} has never been configured for Public Access Block and all 4 flags are False by default.\n")
        bucket_properties['BlockPublicAcls']=False
        bucket_properties['IgnorePublicAcls']=False
        bucket_properties['BlockPublicPolicy']=False
        bucket_properties['RestrictPublicBuckets']=False
    else:
        print("Unexpected error: %s" % (e.response))


# IMPORTANT - Note from AWS Documentation
# --------------------------------------------------------------------------------------------------------------------------------------
# Calls to GET Bucket acl and GET Object acl always return the effective permissions in place for the specified bucket or object. 
# For example, suppose that a bucket has an ACL that grants public access, but the bucket also has the IgnorePublicAcls setting enabled.
# In this case, GET Bucket acl returns an ACL that reflects the access permissions that Amazon S3 is enforcing, rather than the actual 
# ACL that is associated with the bucket.
# ---------------------------------------------------------------------------------------------------------------------------------------

# Get bucket ACL.
try:
    bucket_acl = s3.get_bucket_acl(Bucket=bucket_name)
    
    bucket_properties['Owner']=bucket_acl['Owner']
    bucket_properties['Grants']=bucket_acl['Grants']

    # print(f"Bucket Grants: {bucket_acl['Grants']}\n")

    # Amazon S3 considers a bucket or object ACL public if it grants any permissions to members of the predefined AllUsers or AuthenticatedUsers groups.
    # See The meaning of "Public" section here: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html 
    for grant in bucket_acl['Grants']:
        if grant['Grantee']['Type'] == 'Group':
            if (grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers') or (grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers') :
                public_acl = True

except botocore.exceptions.ClientError as e:
    print("Unexpected error: %s" % (e.response))

# Get bucket policy status.
try:
    bucket_policy_status = s3.get_bucket_policy_status(Bucket=bucket_name)
    
    bucket_properties['PolicyStatus']=bucket_policy_status['PolicyStatus']
    
    # print(f"Bucket policy status is: {bucket_policy_status}\n")

    public_policy = bucket_policy_status['PolicyStatus']['IsPublic']

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
        print(f"Bucket {bucket_name} does not have a bucket policy.")
        bucket_properties['PolicyStatus']="NOT_APPLICABLE"
    else:
        print("Unexpected error: %s" % (e.response))


bucket_properties['PublicACL']=public_acl
bucket_properties['PublicPolicy']=public_policy

if public_acl or public_policy:
    print(f"Bucket {bucket_name} is public!\n")
else:
    print(f"Bucket {bucket_name} is not public.\n")

print(f"Bucket {bucket_name} properties:\n {bucket_properties}\n")



