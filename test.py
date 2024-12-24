import dmPython

#print(dir(dmPython))
try:
    conn = dmPython.connect(user='IES_MS', password='iES_db1984', server='192.168.154.128',port='5236')
    cursor = conn.cursor()
    print('python: conn success!')
    print('您成功连接主机')
    conn.close()
except (dmPython.Error, Exception) as err:
    print(err)