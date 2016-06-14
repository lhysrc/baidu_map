# coding=gbk
import math,random
from time import strftime
import os
from PIL import Image



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
    
    print("请输入左上角，右下角坐标，以空格分开（例如：98440 20660 98467 20633）。\n请确保x1<x2，y1>y2：")
    strs = raw_input()    
    nums = strs.split()    
    x1,y1,x2,y2 = map(int,nums)
    
    #x1,y1,x2,y2 = 98467,20660,98467,20633
    x2+=1;y2-=1
    # x1,y1,x2,y2 = 98461,20657,98467,20536
    # x1,y1,x2,y2 = 98461,20657,98467,20536
    cnt = 0
    for x in range(x1, x2):
        for y in range(y1, y2,-1):
            makeImg(x,y,19,"./gz")
            cnt+=1
    print "下载完成，共有%d个图像需要合并。"%cnt
    
    picName = strftime("%Y%m%d%H%M%S") + ".png"

    #creates a new empty image, RGB mode
    new_im = Image.new('RGB',(abs(x2 - x1) *256,abs(y2 - y1)*256))
    # new_im = Image.new('RGB',(256*2,(y2 - y1)*256))
    path = './gz/19'

    for x in xrange(x1,x2):
        for y in xrange(y1,y2,-1):
            url = "%s/%s/%s.png"%(path,x,y)
            # print url
            im = Image.open(url)
            print "%s已合并"%url
            new_im.paste(im,((x-x1)*256,(y1 - y)*256))

    with open(picName,'wb') as p:
        new_im.save(p)

    print '合并完成，图片文件位于：%s' % os.path.abspath(picName)