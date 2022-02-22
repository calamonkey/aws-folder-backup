#!/use/bin/python3
from urllib import response
import boto3
import os
from datetime import datetime
import shutil

# Set AWS access for S3 Upload
aws_s3_bucket = os.environ.get("S3_BUCKET")
aws_s3_path = os.environ.get("S3_PATH")

# Set locations to be backed up within container:
local_backup_path = "/backup"
backup_time = datetime.now().strftime("%Y_%m_%d")
backup_tar_path = "/tar/" + backup_time

# Compress the folder

shutil.make_archive(backup_tar_path, 'tar', local_backup_path)

# Upload compressed folder to S3

client = boto3.client('s3',
    region_name='ca-central-1'
)
response = client.put_object(
    Bucket=aws_s3_bucket,
    Key=(aws_s3_path + "/" + backup_time + ".tar"),
    StorageClass='ONEZONE_IA',
    Body=backup_tar_path + ".tar",
    ServerSideEncryption='aws:kms'
)
