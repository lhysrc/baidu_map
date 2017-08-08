import requests
import random
import time


counties = []
with open("./counties2.txt") as f:
    for l in f.readlines():
        counties.append(l[0:6])
# print(counties[0:100])

base_uri = 'https://lsp.wuliu.taobao.com/locationservice/addr/output_address_town_array.do?l1={}&l2={}&l3={}'

with open("./towns2.txt", "a+") as f:
    for i, c in enumerate(counties):
        print("%d: %s start!" % (i, c))

        l1 = "{}0000".format(c[0:2])
        l2 = "{}00".format(c[0:4])
        l3 = c
        r = requests.get(base_uri.format(l1, l2, l3)).text
        r = r[len("callback({success:true,result:["):-4]
        f.write(r + "\n")

        sec = random.random() * 5
        print(" %s end! sleep %d secs." % (c, sec))
        time.sleep(sec)
