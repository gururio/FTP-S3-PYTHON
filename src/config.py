import os


SSH_CLIENT = None
SFTP_CLIENT = None
SSH_OK = False
SFTP_OK = False

# ftp credentials
FTP_IP = "Your FTP"
FTP_PORT = "Your FTP_PORT"
FTP_USERNAME = "Your FTP_USERNAME"
FTP_PASSWORD = "Your FTP_PASSWORD"

# s3 parameters
S3_BUCKET = "Your S3_BUCKET Bucket name"

os.environ['AWS_ACCESS_KEY_ID'] = 'Your AWS_ACCESS_KEY_ID ID'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'Your AWS_SECRET_ACCESS_KEY'

# ftp directory paths
PARENT_DIR_PATH = "Your File Landing Path ID"
PROCESSED_DIR_PATH = "Your File Processed Folder ID"