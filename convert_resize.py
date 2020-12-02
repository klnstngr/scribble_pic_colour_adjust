import os, sys
from PIL import Image, ImageDraw

draw_size = (825, 624)

file = os.path.dirname(os.path.realpath(__file__))
origin_files = os.listdir(file + '/pics')
save_loc = file + '/jpg/'
gen_loc = file + '/gen/'

all_pics = [pic for pic in origin_files if "." in pic[-4:]]

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

