# API
import requests
url = "https://api.publicapis.org/entries"
res_data = requests.get(url, params={},data={}).json()

print(res_data)

# database
import MySQLdb
conn = MySQLdb.connect(
    host='',
    user='',
    passwd='',
    db='',
)
cursor = conn.cursor()
stmt = """
select * from tabel
"""
cursor.execute()
res_data = cursor.fetchall()

# ssh
import pysftp
hostname = ''
user_name = ''
pwd = ''
filename = ''
with pysftp.Connection(hostname, username=user_name, password=pwd) as sftp:
    sftp.get(filename)

# file
import csv
with open(filename) as file:
    res_data = csv.reader(file, delimiter=',')
