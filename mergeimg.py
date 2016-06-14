from PIL import Image
from time import strftime
import os

#x1,y1,x2,y2 = 98505,20635,98600,20756

x1,y1,x2,y2 = 98440,20644,98445,20638
#x1,y1,x2,y2 = 98440,20660,98467,20633

x2+=1;y2-=1
picName = strftime("%Y%m%d%H%M%S") + ".png"
#x1 = 98550
#x2 = 98590
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

# # new_im = Image.new('RGB', (400,400))
#
# #Here I resize my opened image, so it is no bigger than 100,100
# im.thumbnail((100,100))
# #Iterate through a 4 by 4 grid with 100 spacing, to place my image
# for i in xrange(0,500,100):
#     for j in xrange(0,500,100):
#         #I change brightness of the images, just to emphasise they are unique copies.
#         im=Image.eval(im,lambda x: x+(i+j)/30)
#         #paste the image at location i,j:
#         new_im.paste(im, (i,j))

# new_im.show()

with open(picName,'wb') as p:
    new_im.save(p)

print '合并完成，图片文件位于：%s' % os.path.abspath(picName)