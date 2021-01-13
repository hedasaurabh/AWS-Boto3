# Switching to an IAM Role (AWS API) using Boto3

# Requirements

You will need an IAM User(ARN:`arn:aws:iam::xxxxxxxxxxxx:user/sts-test-user`) with `sts:AssumeRole` & `sts:GetFederationToken` permissions. I created a custom policy for the same.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:GetFederationToken",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "*"
        }
    ]
}
```
Also, the IAM user should have an IAMReadOnlyAccess policy attached to it. 

You will also need a Role. Trust Relationship should be as listed below
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::xxxxxxxxxxxx:user/sts-test-user"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

# Usage
```bash
pip install boto3
python3 sts-assumepolicy.py
```
