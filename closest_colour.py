''' This function returns an image with the colors that can be used in 
    scribbl.io
    {white, light_grey, red, terracotta, yellow, light_green, light_blue, blue, light_purple, pale_pink, light_brown}
    {black, dark_grey, dark_red, dark_terracotta, dirty_yellow, dark_green, muddy_blue, dark_blue, dark_purple, grey_pink, dark_brown}
    scribbl.io draw size == (835, 624)
'''

# TODO: Implement a cache function, that compares downloaded pictures in pics, .jpg's in jpg and generated pictures in gen
# TODO: Compare every pixel to a scribbl.io colour and create the new picture with scribbl.io colours

import os, sys
import time
from PIL import Image, ImageDraw

draw_size = (825, 624)

file = os.path.dirname(os.path.realpath(__file__))
folder_entries = os.listdir(file + '/pics')

all_pics = [pic for pic in folder_entries if "." in pic[-4:]]
save_loc = file + '/jpg/'

for im in all_pics:
    print(im)
    img = Image.open(file + '/pics/{}'.format(im))
    img = img.copy().convert('RGB')

    size_hor, size_ver = img.size
    prop_hor, prop_ver = round(size_hor/draw_size[0],2), round(size_ver/draw_size[1],2)
    
    if prop_ver >= 1 or prop_hor >= 1:
        img.thumbnail(draw_size)
    else:
        print("    {} x {}".format(size_hor, size_ver))
        print("    {} or {}".format(prop_hor, prop_ver))
        if prop_hor >= prop_ver:
            prop = prop_hor
        else:
            prop = prop_ver
        draw_size_prop = (round(size_hor / prop),round(size_ver / prop))
        print(draw_size_prop)
        picture = img.resize(draw_size_prop)
        print(picture.size)
        print(save_loc + '{}.jpg'.format(im)[:-4])
        img = picture
    img.save(save_loc + '{}.jpg'.format(im)[:-4], 'JPEG')






"""
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
"""