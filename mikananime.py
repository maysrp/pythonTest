import requests
from pyquery import PyQuery as pq
import pymysql
# import jieba
db=pymysql.connect('127.0.0.1','root','root','ac')
cursor=db.cursor();
'''
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
'''
for p in range(100):
    url='https://mikanani.me/Home/Classic/2'+str(p)
    html=requests.get(url)
    info=pq(html.text)
    tr=info('.table-striped').find('tr')
    all=[]
    for i in tr:
        dic={}
        xn=pq(i)
        name=xn('td:eq(2)').text();
        torrent=xn('td:eq(2)>a:eq(1)').attr('data-clipboard-text')
        size=xn('td:eq(3)').text()
        if name:
            dic['name']=name
            dic['torrent']=torrent
            dic['size']=size
            all.append(dic)    


    for one in all:
        HASH_SQL="SELECT * FROM mikananime WHERE torrent='%s'" %(one['torrent'])
        cursor.execute(HASH_SQL)
        hasx=cursor.fetchall()
        if not len(hasx):
            # SQL="INSERT INTO mikananime(NAME,TORRENT,SIZE) VALUES('%s','%s','%s')" %(one['name'],one['torrent'],one['size'])
            # inx=cursor.execute(SQL)
            SQL="INSERT INTO mikananime(NAME,TORRENT,SIZE) VALUES(%s,%s,%s)"
            inx=cursor.execute(SQL,(one['name'],one['torrent'],one['size']))
            # ob=jieba.cut(one['name'])
            # for x in ob:
            #     print(x)




