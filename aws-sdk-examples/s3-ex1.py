#-------------------------------------------------------------------------------------------
# This exemple lists all the S3 buckets that have public access turned ON in an AWS account.
# #-----------------------------------------------------------------------------------------

import boto3

# Get the service resource
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
