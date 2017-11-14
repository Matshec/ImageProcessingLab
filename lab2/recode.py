from PIL import Image, ImageMath
import scipy.io as sio
import matplotlib.pyplot as ppl


def to_show(im):
    return ImageMath.eval("float(a)",a=im)

def append_to_pyplot(img):
    return ppl.imshow(to_show(img))

def recode_and_show_picture(pic, table):
    #funckcja point  działa jak lut w matlabie
    recoded = pic.point(table)
    ppl.subplot(221)
    ppl.plot(table)
    ppl.subplot(223)
    append_to_pyplot(pic)
    ppl.subplot(224)
    append_to_pyplot(recoded)
    ppl.show()


mat_lut_dict = sio.loadmat("pointbased/funkcjeLUT.mat")
#print(mat_lut_dict.keys())
lut_table = mat_lut_dict["kwadratowa"].flatten()
read_image = Image.open("pointbased/lena.bmp")
recode_and_show_picture(read_image, lut_table)
