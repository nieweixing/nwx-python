import os,sys,subprocess
from boto3.session import Session

image_name = []

aws_key = "AKIATRMLTGCFIY5WRHGG"
aws_secret = "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"

session = Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret,region_name="cn-northwest-1")
s3 = session.resource("s3")
client = session.client("s3")


def pull_images(image_name):
  for name in image_name:
    print(name)
    cmd_pull = 'docker pull {}'.format(name)
    os.system(cmd_pull)

  all_image = " ".join(image_name)
  print(all_image)
  image_tag = subprocess.Popen(['date +"%Y%m%d-%H%M%S"'],stdout=subprocess.PIPE,shell=True).communicate()
  cmd_tar_images = 'docker save {} -o images-{}.tar'.format(all_image,image_tag[0].replace("\n", ""))
  tar_name = 'images-{}.tar'.format(image_tag[0].replace("\n", ""))
  os.system(cmd_tar_images)
  print(cmd_tar_images)
  data = open(tar_name, "rb")
  s3.Bucket("kg-api-production").put_object(Key=tar_name ,Body=data)

pull_images(sys.argv[1:])


