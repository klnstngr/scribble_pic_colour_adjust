''' This function returns an image with the colors that can be used in 
    scribbl.io
    {white, light_grey, red, terracotta, yellow, light_green, light_blue, blue, light_purple, pale_pink, light_brown}
    {black, dark_grey, dark_red, dark_terracotta, dirty_yellow, dark_green, muddy_blue, dark_blue, dark_purple, grey_pink, dark_brown}
    scribbl.io draw size == (835, 624)
    Brush-sizes: 6*6, 16*16, 44*44
    {white == (255,255,255), light_grey == (193,193,193), red == (240, 19, 11), terracotta == (255, 113, 1), yellow == (255, 228, 0), light_green == (1, 204, 0), light_blue == (1, 178, 255), blue == (35, 32, 211), light_purple == (173, 0, 185), pale_pink == (211, 124, 169), light_brown == (160, 82, 44)}
    {black == (0,0,0), dark_grey == (76, 76, 76), dark_red == (116, 11 , 7), dark_terracotta == (195, 56, 1), dirty_yellow == (231, 162, 0), dark_green == (0, 85, 17), muddy_blue == (0, 85, 158), dark_blue == (13, 8, 100), dark_purple == (84, 0 , 104), grey_pink == (166, 85, 117), dark_brown == (98, 48, 13)}
'''

# TODO: Implement a cache function, that compares downloaded pictures in pics, .jpg's in jpg and generated pictures in gen
# TODO: Compare every pixel to a scribbl.io colour and create the new picture with scribbl.io colours

import os, sys
import time
from PIL import Image, ImageDraw

draw_size = (825, 624)

file = os.path.dirname(os.path.realpath(__file__))
origin_loc = os.listdir(file + '/pics')
save_loc = file + '/jpg/'
gen_loc = file + '/gen/'

all_pics = [pic for pic in origin_loc if "." in pic[-4:]]

for im in all_pics:
    print(im)
    im1 = str(im[:-4])
    print(im1)
    img = Image.open(file + '/pics/{}'.format(im))
    img = img.copy().convert('RGB').save(save_loc + '{}.jpg'.format(im1), 'jpeg')
    img = Image.open(save_loc + '{}.jpg'.format(im1))

    size_hor, size_ver = img.size
    prop_hor, prop_ver = round(size_hor/draw_size[0],2), round(size_ver/draw_size[1],2)
    
    if prop_ver >= 1 or prop_hor >= 1:
        img.thumbnail(draw_size)
        print(save_loc + '{}.jpg'.format(im1), 'jpeg')
        img.save(save_loc + '{}.jpg'.format(im1), 'jpeg')
    else:
        # print("    {} x {}".format(size_hor, size_ver))
        # print("    {} or {}".format(prop_hor, prop_ver))
        if prop_hor >= prop_ver:
            prop = prop_hor
        else:
            prop = prop_ver
        
        draw_size_prop = (round(size_hor / prop),round(size_ver / prop))
        picture = img.resize(draw_size_prop)
        print(save_loc + '{}.jpg'.format(im1))
        picture.save(save_loc + '{}.jpg'.format(im1), 'jpeg')


active_loc = save_loc
active_pics = [pic for pic in active_loc if "." in pic[-4:]]

for data_set in active_pics:
    print(data_set)




"""
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
"""