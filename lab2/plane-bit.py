from PIL import Image,ImageMath
import numpy as np



def get_bit_plane(mask, img: Image):
    np_im = np.asarray(img,dtype=np.int8)
    for x in np.nditer(np_im,[],['readwrite']):
        x[...] = mask & x
    return Image.fromarray(np_im,mode="L")



def get_eight_bit_planes(img):
    ret = []
    curr_mask = 0b00000001
    for i in range(8):
        im = get_bit_plane(curr_mask,img)
        ret.append(im)
        curr_mask = curr_mask << 1
    return ret

#zerowy index w im_list to odpowiednik maski 00000001 każdy kolejny to jeden bitshift w lewo
# def restore_image(index_list,im_list):
#     if len(index_list) > 0 and len(im_list) == 8:
#         for i in index_list:
#             im = np.asarray(im_list[i],dtype=np.int8)
#
#
#     else:
#         raise  Exception




# hays_im = Image.open("pointbased/100zloty.jpg").convert("L")
# ls = get_eight_bit_planes(hays_im)
# for i in ls:
#     i.show()
