import boto3 #to configure with aws to make use of aws services
from botocore.exceptions import ClientError
from config import Config

class S3Storage:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_ACCESS_KEY
        )

        self.bucket = Config.AWS_BUCKET_NAME

    def upload_file(self, file_object, filename): # send file to s3 bucket
        try:
            self.s3.upload_fileobj(file_object,self.bucket, filename)
            return True
        except ClientError as e:
            print(f"Error uploading file:{e}")
            return False

    def get_file(self,filename): #get file from S3 bucket
        try:
            response= self.s3.get_object(Bucket=self.bucket, Key=filename)
            return response ['body']
        except ClientError as e:
            print(f"error retrieving file: {e}")
            return None

