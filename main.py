#! usr/bin/python3

from ftplib import FTP

'''[Storing env variables inside scripts leads to vulnerabilities
once configured setting up env variables can be done using the following
api's]'''

# from dotenv import load_dotenv
# from pathlib import Path

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

host = None # enter host name
user = None # enter user name 
password = None # enter password once initialized 


with FTP(host) as ftp:
    ftp.login(user=user, password=password)
    print(ftp.getwelcome())
    
# options - 
#1 Filezilla
#2 Openstack 

    # with open('test.txt', 'wb') as f: 
    #     '''[retrieves a created file on the server]'''
    #     ftp.retrbinary("RETR", 'mytest.txt', f.write, 1024)
    
    
        