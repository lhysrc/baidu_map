# coding=utf-8
import requests

url = 'http://wap.guahao.gov.cn/deptdocpb.xhtml'  # 获取医生信息

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.6",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://wap.guahao.gov.cn/select_doc.xhtml",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",

}

data = {
    'index': 1,
    'count': 8,
    'searchtype': '',
    'name': '',
    'HIS_CD': '104501',
    'DEP_ID': '218',
    'REG_DT': '2016-05-19',
    'MAX_REG_DT': '7',
    'IS_TODAY': 'null',
    'DOC_ID': '',
    'TM_FLG': '1',
    'DOC_NM_BLUR': '',
    'operid': '',
}

ss = requests.session()
ss.headers.update(headers)

from email.mime.text import MIMEText
from email.header import Header
import smtplib
from common.secret_const import email_addr,email_pwd,smtp_server
def sendEmail(toMail,title,content):
    msg = MIMEText(str(content))
    msg['From'] = Header('Auto','utf-8').encode()
    msg['To'] = Header(toMail,'utf-8').encode()
    msg['Subject'] = Header(title,'utf-8').encode()

    server = smtplib.SMTP(**smtp_server)
    server.set_debuglevel(1)
    server.login(email_addr,email_pwd)
    server.sendmail(email_addr,[toMail],msg.as_string())
    server.quit()

from datetime import date,timedelta
import time
while(True):
    for i in range(1,8):
        data['REG_DT'] = str(date.today() + timedelta(i))


        j = ss.post(url,data).json()

        print data['REG_DT']
        for doc in j['REC']:
            if len(doc['DOC_NM']) <= 3 and int(doc['REG_LV_CNT']) > 0:
                title = '%s,%s has %s'%(data['REG_DT'],doc['DOC_NM'],doc['REG_LV_CNT'])
                sendEmail('hyiit@qq.com', title, '')
                print data['REG_DT']
                print '\t',doc['DOC_NM'],doc['REG_LV_CNT']
    time.sleep(30)
        #print '\t',doc['DOC_NM'],doc['REG_LV_CNT']

