# coding=utf-8
import math,random
def getBlockNum(num, level):
    mercator =int((num / math.pow(2, -(level - 18))) / 256)
    return int(math.ceil(mercator))

def makeImg(x,y,level,fileURL,type=""):
    testFileURL(fileURL)
    fileURL = "%s/%s"%(fileURL,type)
    testFileURL(fileURL)
    fileURL = "%s/%s"%(fileURL, level)
    testFileURL(fileURL)
    fileURL = "%s/%s"%(fileURL, x)
    testFileURL(fileURL)
    #　生成图片路径
    fileURL = "%s/%s.png"%(fileURL, y)#fileURL + "/" + y + ".png"
    if (os.path.exists(fileURL)):
        print ("图片已存在：%s"% fileURL)
        return
    else:
        server = random.randint(0,3)
        if type == 'street':
            url = "http://online{}.map.bdimg.com/onlinelabel/?qt=tile&x={}&y={}&z={}&styles=pl&udt=20160429&scaler=1&p=0".format(server,x,y,level)
        else:
            url = "http://shangetu{}.map.bdimg.com/it/u=x={};y={};z={};v=009;type=sate&fm=46".format(server,x,y,level)
        download(url, fileURL)
        if os.path.exists(fileURL):
            print ("下载完成：%s" % url)
        else:
            print ("!!\t下载失败：%s" % url)


import urllib2,urllib
def download(url,fileURL):
    resp = urllib2.urlopen(url)
    with open(fileURL,'wb') as f:
        f.write(resp.read())


def getImgToDownload(p, startLevel, endLevel, fileURL, type="") :
    checkFolder(fileURL)
    for i in range (startLevel,endLevel+1):
        startBlockX = getBlockNum(p[0], i)
        startBlockY = getBlockNum(p[1], i)
        endBlockX = getBlockNum(p[2], i)
        endBlockY = getBlockNum(p[3], i)
        if startBlockX == endBlockX and startBlockY == endBlockY:
            makeImg(startBlockX, endBlockX, i, fileURL, type)
        elif startBlockX == endBlockX and startBlockY < endBlockY:
            for j in range(startBlockY,endBlockY+1) :
                makeImg(startBlockX, j, i, fileURL, type)
        elif startBlockX < endBlockX and startBlockY == endBlockY:
            for j in range(startBlockY, endBlockY+1):
                makeImg(j, startBlockY, i, fileURL, type)
        elif startBlockX < endBlockX and startBlockY < endBlockY:
            for j in range(startBlockY, endBlockY+1):
                for k in range(startBlockX, endBlockX+1):
                    makeImg(k, j, i, fileURL, type)


import os
def checkFolder(fileURL):
    if os.path.exists(fileURL):
        print("文件夹存在")
    else:
        os.mkdir(fileURL)
        print("创建文件夹：%s" % fileURL)



def testFileURL(url):
    if not os.path.isdir(url):
        os.mkdir(url)
        print("创建文件夹：%s" % url)

if __name__ == '__main__':
    # p = (12575735.07, 2557788.85, 12697886.49, 2728067.86)
    # p = (12608670.712133333, 2641485.312542373, 12620795.3716, 2656817.638654661)
    # getImgToDownload(p,19,19,"./gz")

    # 98505, 98599
    # 20636, 20756

    for x in range(98532, 98600):
        for y in range(20636, 20757):
            makeImg(x,y,19,"./gz")