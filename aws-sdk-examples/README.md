# AWS-SDK-Examples folder
The code examples in this folder demonstrate using the Amazon Web Services (AWS) SDK for Python ("boto3") to call various AWS services. The examples are mostly based on the [Boto3 Docs Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html). 

## Pre-requisites

* [Amazon Web Services (AWS) account](http://aws.amazon.com/).
* Python 3.6 or later and boto3. Check out AWS [documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) on how to install boto3.

## Quick start

1. Configure your [AWS access 
keys](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) as 
environment variables:

Linux:
```
$ export AWS_ACCESS_KEY_ID=<Your AWS_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<Your AWS_SECRET_ACCESS_KEY>
$ export AWS_DEFAULT_REGION=<Your AWS_DEFAULT_REGION>
```

Windows:
```
PS $env:AWS_ACCESS_KEY_ID=<Your AWS_ACCESS_KEY_ID>
PS $env:AWS_SECRET_ACCESS_KEY=<Your AWS_SECRET_ACCESS_KEY>
PS $env:AWS_DEFAULT_REGION=<Your AWS_DEFAULT_REGION>
```

## References
[Boto3 Docs 1.22.4 Documentation - Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration)
