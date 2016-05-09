from PIL import Image

x1,y1,x2,y2 = 98505,20635,98600,20756
x1 = 98550
#x2 = 98590
#creates a new empty image, RGB mode
new_im = Image.new('RGB',((x2 - x1) *256,(y2 - y1)*256))
# new_im = Image.new('RGB',(256*2,(y2 - y1)*256))
path = './gz/19'

for x in xrange(x1,x2):
    for y in xrange(y2,y1,-1):
        url = "%s/%s/%s.png"%(path,x,y)
        # print url
        im = Image.open(url)
        new_im.paste(im,((x-x1)*256,(y2 - y)*256))

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

with open('bd.png','wb') as p:
    new_im.save(p)