from PIL import Image, ImageMath, ImageOps
import matplotlib.pyplot as ppl
import numpy


def normalize(im):
    np_im = numpy.asarray(im,dtype=int)
    maxn = numpy.amax(np_im)
    return ImageMath.eval("float(I)/c",I=im,c=maxn/255)



def add_images(im1,im2):
    result = ImageMath.eval("a + b", a=im1, b=im2)
    return  normalize(result)

#[(a,b),(c,d)]
def lin_comb(lst):
    if len(lst) > 1:
        k2,A1 = lst[0]
        prev = ImageMath.eval("x*(float(B))",x=k2,B=A1)
        iterpics = iter(lst)
        next(iterpics)
        for el in lst:
            k2, A2 = el
            prev = ImageMath.eval("A+(y*float(C))",A = prev,y=k2,C=A2)
        return normalize(prev)
    else:
        raise Exception

def subtract(im1,im2):
    return ImageMath.eval("A-B",A=im1,B=im2)

def subtract_abs(im1,im2):
    return ImageMath.eval("abs(A-B)",A=im1,B=im2)

def mult(im1,im2):
    return normalize(ImageMath.eval("A*B", A=im1,B=im2))

def const_mult(c,im):
    return ImageMath.eval("k*float(A)",k=c,A=im)

def apply_mask(mask:Image,im:Image):
    bool_mask = convert_to_bool(mask)
    np_im = numpy.asarray(im)
    raw_res = numpy.multiply(bool_mask,np_im)
    return convert_from_bool(raw_res)


def convert_to_bool(im):
    """":returns numpy array"""
    return numpy.asarray(im,dtype=bool)

def convert_from_bool(im):
    return Image.fromarray(im)

def im_negative(im):
    return ImageOps.invert(im)

lena_im = Image.open("pointbased/lena.bmp")
jet_im = Image.open("pointbased/jet.bmp")
kolo_im  =Image.open("pointbased/kolo.bmp")
#res = lin_comb([(0.6,lena_im),(0.4,jet_im)])
res = mult(lena_im,jet_im)
res.show()
