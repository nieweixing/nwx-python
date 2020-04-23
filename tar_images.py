import os,sys,subprocess
from boto3.session import Session

aws_key = "AKIATRMLTGCFIY5WRHGG"
aws_secret = "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"

session = Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret,region_name="cn-northwest-1")

s3 = session.resource("s3")
client = session.client("s3")

s3.Bucket(kg-api-production).put_object(Key="test",Body=data)


def pull_images(*image_name):
  for name in image_name:
    cmd_pull = 'docker pull image {}'.format(image_name)
    os.system(cmd_pull)
    print(name) 

pull_images(sys.argv[1:])



