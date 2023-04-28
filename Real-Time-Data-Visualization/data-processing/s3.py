python
import boto3

# create an S3 client object
s3 = boto3.client('s3')

# define the bucket name
bucket_name = 'my-data-bucket'

def upload_to_s3(local_file_path, s3_key_name):
    """
    Uploads a local file to S3 bucket
    """
    s3.upload_file(local_file_path, bucket_name, s3_key_name)
    print("File uploaded successfully to S3!")

def download_from_s3(s3_key_name, local_file_path=None):
    """
    Downloads a file from an S3 bucket to a local file path
    """
    # if no local file path is specified, save to current working directory
    if not local_file_path:
        local_file_path = s3_key_name.split('/')[-1]

    s3.download_file(bucket_name, s3_key_name, local_file_path)
    print("File downloaded successfully from S3!")
