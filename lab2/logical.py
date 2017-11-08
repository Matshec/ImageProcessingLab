from PIL import Image,ImageMath

def im_not(im1):
    return ImageMath.eval("~B",B=im1)

def im_and(im1, im2):
    return ImageMath.eval("A & B",A=im1,B=im2)

def im_or(im1, im2):
    return ImageMath.eval("A | B",A=im1,B=im2)

def im_xor(im1, im2):
    return ImageMath.eval("A ^ B",A=im1,B=im2)

lena_im = Image.open("pointbased/lena.bmp")
jet_im = Image.open("pointbased/jet.bmp")
lena_im.show()
jet_im.show()
res = im_and(lena_im,jet_im)
res.show()