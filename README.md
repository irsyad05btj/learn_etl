# Data Processing and Integration

## Prequisite
```
1. Python: Loop, data type, file manipulation, class-method
2. Database sql
3. Docker installation
```

## Definisi
Proses menarik data dari sumber menjadi informasi pada penyimpanan

## ETL (Extract Transform Load)

- Extract: Menarik Data dari sumber
- Transform: Mengubah Data mentah sehingga sesuai dengan kebutuhan
- Load: Menempatkan data pada penyimpanan, sehingga bisa lgsg diakses dalam proses internal server

### Extract
3 Hal utama yg perlu diperhatikan:
1. Akses
    - butuh izin akses seperti vpn?
    - tipe akses: api, ssh, sftp, database, file

    Contoh:
    ```python
    # API
    import requests
    url = "https://api.publicapis.org/entries"
    res_data = requests.get(url, params={},data={}).json()

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

    ```

2. Scheduler
    Penjadwalan jalan nya suatu program
    
3. Worker
    Program yang bertugas menjalankan task/fungsi

    Contoh scheduler-worker:
    ```python
        from time import sleep
    from apscheduler.schedulers.background import BlockingScheduler

    # Creates a default Background Scheduler
    sched = BlockingScheduler()

    def prompt():
        print("Executing Task...")

    sched.add_job(prompt,'interval', seconds=5)

    sched.start()
    ```
