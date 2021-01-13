import boto3

# create an STS client object that represents a live connection to the 
# STS service
sts_client = boto3.client('sts')

# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::780508645745:role/STS-Test-Role",
    RoleSessionName="Saurabh",
    DurationSeconds = 900
    )

# From the response that contains the assumed role, get the temporary 
# credentials that can be used to make subsequent API calls
credentials=assumed_role_object['Credentials']
print ("AccessKey: {} \nSecret_key: {} \nSessionToken: {}".format(credentials['AccessKeyId'],credentials['SecretAccessKey'],credentials['SessionToken']))

# Use the temporary credentials that AssumeRole returns to make a 
# connection to Amazon S3  
s3_resource=boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)

# # Use the Amazon S3 resource object that is now configured with the 
# # credentials to access your S3 buckets. 
for bucket in s3_resource.buckets.all():
    print(bucket.name)