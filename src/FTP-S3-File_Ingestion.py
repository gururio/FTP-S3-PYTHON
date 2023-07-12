import ftplib
import boto3
import os
import time
import config as cfg
import logger as logger



class ExtractLoad:

    def __init__(self):
        self.ftp_ip = cfg.FTP_IP
        self.ftp_user = cfg.FTP_USERNAME
        self.ftp_password = cfg.FTP_PASSWORD
        self.ftp_port = cfg.FTP_PORT
        self.s3_bucket = cfg.S3_BUCKET
        self.ftp_filepath = cfg.PARENT_DIR_PATH
        self.processed_folder = cfg.PROCESSED_DIR_PATH
        self.s3 = boto3.client('s3')

    print('Establishing connection with FTP Server')
    def connect_ftp(self):
        try:
            # Connect to FTP server
            ftp = ftplib.FTP(self.ftp_ip, self.ftp_user, self.ftp_password, self.ftp_port)
            ftp.encoding = 'utf-8'
            return ftp

        except Exception as e:
            logger.exception(f"Error in uploading data {str(e)}")
            print(e)

    print('Started File Upload to S3')
    def upload_file_from_ftp_to_s3(self, ftp, filename, s3_object_key):
        try:
            with open(filename, 'wb') as file:
                ftp.retrbinary(f'RETR {filename}', file.write)

            with open(filename, 'rb') as file:
                self.s3.upload_fileobj(file, self.s3_bucket, s3_object_key)

        except Exception as e:
            logger.exception(f"Error in uploading data {str(e)}")
            print(e)

    def move_file_to_processed_folder(self, ftp, source_filepath, processed_filepath):
        try:
            ftp.rename(source_filepath, processed_filepath)

        except Exception as e:
            logger.exception(f"Error in uploading data {str(e)}")
            print(e)

    def delete_local_file(self, filename):
        try:
            os.remove(filename)

        except Exception as e:
            logger.exception(f"Error in uploading data {str(e)}")
            print(e)

    def close_ftp_connection(self, ftp):
        try:
            ftp.quit()

        except Exception as e:
            logger.exception(f"Error in uploading data {str(e)}")
            print(e)


    def main(self):
        try:
            while True:
                ftp = self.connect_ftp()
                # Change directory to the "Input" folder
                ftp.cwd(self.ftp_filepath)
                # Get a list of files in the FTP "Input" folder
                files = ftp.nlst()

                # Iterate over each file and copy to S3
                for filename in files:
                    # Define the S3 object key
                    s3_object_key = f'default/{filename}'
                    self.upload_file_from_ftp_to_s3(ftp, filename, s3_object_key)
                    # Moving the copied file to processed folder
                    processed_filepath = f'{self.processed_folder}/{filename}'
                    self.move_file_to_processed_folder(ftp, filename, processed_filepath)
                    # Remove the local file
                    self.delete_local_file(filename)
                # Close FTP connection
                self.close_ftp_connection(ftp)
                time.sleep(300)

        except Exception as e:
            logger.exception(f"Error in uploading data {str(e)}")
            print(e)

if __name__ == "__main__":
    ftp_obj = ExtractLoad()
    ftp_obj.main()
