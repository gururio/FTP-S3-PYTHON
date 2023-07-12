FTP to S3 Data Transfer Process

This script automates the transfer of files from an FTP server to an Amazon S3 bucket.

Methodology 

The FTP to S3 Data Transfer Process provides a reliable and efficient method to transfer files from an FTP server to an S3 bucket. By automating the process, it reduces manual intervention and ensures data integrity during the transfer.
The script will establish a connection with the FTP server, retrieve files from the landing directory, upload them to the S3 bucket, move the processed files to a processed folder, and delete the local copies.
 The process will run continuously, checking for new files in the FTP directory every 5 minutes. To stop the process, you can terminate the script execution.

 Setup and Configuration

Before running the script, ensure that you have the following components set up:

•	An FTP server with the necessary credentials and access rights. In my case I have created a FTP server in my local.

•	An Amazon S3 bucket to store the transferred files

•	AWS credentials with appropriate permissions to access the S3 bucket

Dependencies

The following dependencies are required to run the script:
Run the following command to install all the necessary pip packages to run the program: sudo pip install -r requirements.txt

•	ftplib: for establishing the FTP connection and file transfer 

•	boto3: for interacting with the S3 bucket

•	os: for handling local file operations

•	time: for adding delays between iterations




To run the FTP to S3 data transfer process:

1. Set the configuration parameters in the `config.py` file. Update the FTP and S3 connection details, file paths, and other required information.
2. Execute the `FTP-S3-File_Ingestion.py` script:
3. The script will establish a connection with the FTP server, retrieve files from the specified directory, upload them to the S3 bucket, move the processed files to a separate folder, and delete the local copies.
4. The process will run continuously, checking for new files in the FTP directory every 5 minutes. To stop the process, you can terminate the script execution.


Note: For establishing connection with FTP server my primary plan was to go with SSH File Transfer Protocol which is more secured since we are building a production level system, using paramiko python library. 
But I was encountering some firewall defender issues with my personal account. So, I used ftplib to establish connection with FTP server

